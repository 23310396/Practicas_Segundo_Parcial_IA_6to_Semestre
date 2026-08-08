import json, os, warnings
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, RepeatedKFold, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import shap
warnings.filterwarnings('ignore')
SEED=42
np.random.seed(SEED)
outdir=Path('analysis_results'); outdir.mkdir(exist_ok=True)
urls=[
'https://gist.githubusercontent.com/RHDZMOTA/71c7bfc23dbd13eb8a1dfb26f7399510/raw/c0274bcb736ba2f94c29aa3d1baf2136a75f02e5/dataset-lendingclub-custom-low-funding.csv',
'https://gist.githubusercontent.com/RHDZMOTA/71c7bfc23dbd13eb8a1dfb26f7399510/raw/c0274bcb736ba2f94c29aa3d1baf2136a75f02e5/dataset-lendingclub-custom-medium-funding.csv',
'https://gist.githubusercontent.com/RHDZMOTA/71c7bfc23dbd13eb8a1dfb26f7399510/raw/c0274bcb736ba2f94c29aa3d1baf2136a75f02e5/dataset-lendingclub-custom-large-funding.csv']
parts=[pd.read_csv(u) for u in urls]
part_shapes=[list(x.shape) for x in parts]
df=pd.concat(parts, ignore_index=True)
initial_shape=list(df.shape)
initial_dtypes={c:str(t) for c,t in df.dtypes.items()}
initial_nulls={c:int(v) for c,v in df.isnull().sum().items() if int(v)>0}
desc=df.describe(include=[np.number]).round(6).to_dict()
head=df.head(5).replace({np.nan:None}).to_dict(orient='records')
successful=['Fully Paid','Does not meet the credit policy. Status:Fully Paid']
work=df.copy()
work['loan_success']=work['loan_status'].isin(successful).astype(int)
work['term_months']=pd.to_numeric(work['term'].astype(str).str.extract(r'(\d+)')[0], errors='coerce')
emp=work['employment_length'].astype('string').str.strip()
emp=emp.replace({'< 1 year':'0 years','10+ years':'10 years'})
work['employment_length_num']=pd.to_numeric(emp.str.extract(r'(\d+)')[0], errors='coerce')
work['issue_date_dt']=pd.to_datetime(work['issue_date'], format='%b-%y', errors='coerce')
work['earliest_credit_dt']=pd.to_datetime(work['earliest_credit_line'], format='%b-%y', errors='coerce')
mask=(work['earliest_credit_dt'].notna() & work['issue_date_dt'].notna() & (work['earliest_credit_dt']>work['issue_date_dt']))
work.loc[mask,'earliest_credit_dt']=work.loc[mask,'earliest_credit_dt']-pd.DateOffset(years=100)
work['issue_year']=work['issue_date_dt'].dt.year
work['credit_history_years']=(work['issue_date_dt']-work['earliest_credit_dt']).dt.days/365.25
impute_cols=['annual_income','employment_length_num','credit_history_years','term_months','interest_rate','installment']
impute_values={}
for c in impute_cols:
    med=float(work[c].median())
    impute_values[c]=med
    work[c]=work[c].fillna(med)
categorical=['grade','sub_grade','home_ownership','verification_status','payment_plan','purpose','address_state']
for c in categorical:
    work[c]=work[c].fillna('Unknown').astype(str)
base_cols=['funded_amount','loan_success','annual_income','term_months','interest_rate','installment','employment_length_num','credit_history_years',*categorical]
model_raw=work[base_cols].copy()
model_raw=pd.get_dummies(model_raw, columns=categorical, drop_first=True, dtype=int)
scale_cols=['annual_income','term_months','interest_rate','installment','employment_length_num','credit_history_years']
model_scaled=model_raw.copy()
scaler=MinMaxScaler()
model_scaled[scale_cols]=scaler.fit_transform(model_scaled[scale_cols])
success_counts=work['loan_success'].value_counts().sort_index()
success_rate=float(work['loan_success'].mean())
funded_stats={k:float(v) for k,v in work['funded_amount'].describe().items()}
annual_stats={k:float(v) for k,v in work['annual_income'].describe().items()}
corr=float(work[['annual_income','funded_amount']].corr().iloc[0,1])
term_table=(work.groupby('term_months')['loan_success'].agg(['count','mean']).reset_index())
term_rates=[{'term_months':int(r.term_months),'count':int(r['count']),'success_rate':float(r['mean'])} for _,r in term_table.iterrows()]
hist_counts,hist_edges=np.histogram(work['funded_amount'].to_numpy(), bins=25)
eda_sample=work[['annual_income','funded_amount','loan_success','term_months']].sample(n=min(3000,len(work)), random_state=SEED)
eda_sample.to_csv(outdir/'eda_sample.csv',index=False)
X_simple=work[['annual_income']]
y=work['funded_amount']
Xs_train,Xs_test,ys_train,ys_test=train_test_split(X_simple,y,test_size=.20,random_state=SEED)
reg_simple=LinearRegression().fit(Xs_train,ys_train)
pred_simple=reg_simple.predict(Xs_test)
simple={'coef_annual_income':float(reg_simple.coef_[0]),'intercept':float(reg_simple.intercept_),
        'mse':float(mean_squared_error(ys_test,pred_simple)),'r2':float(r2_score(ys_test,pred_simple)),
        'train_n':int(len(ys_train)),'test_n':int(len(ys_test))}
X_reg=model_raw.drop(columns=['funded_amount','loan_success']); y_reg=model_raw['funded_amount']
Xr_train,Xr_test,yr_train,yr_test=train_test_split(X_reg,y_reg,test_size=.20,random_state=SEED)
reg_multi=LinearRegression().fit(Xr_train,yr_train)
pred_multi=reg_multi.predict(Xr_test)
coefs=pd.Series(reg_multi.coef_,index=X_reg.columns)
top_coef=coefs.reindex(coefs.abs().sort_values(ascending=False).index).head(20)
multi={'intercept':float(reg_multi.intercept_),'mse':float(mean_squared_error(yr_test,pred_multi)),'r2':float(r2_score(yr_test,pred_multi)),
       'train_n':int(len(yr_train)),'test_n':int(len(yr_test)),
       'top_coefficients':[{'feature':str(k),'coefficient':float(v)} for k,v in top_coef.items()]}
reg_sample=pd.DataFrame({'real':yr_test.to_numpy(),'simple_pred':reg_simple.predict(work.loc[yr_test.index,['annual_income']]),'multi_pred':pred_multi}).sample(n=min(2500,len(yr_test)),random_state=SEED)
reg_sample.to_csv(outdir/'reg_predictions_sample.csv',index=False)
X_cls=model_scaled.drop(columns=['funded_amount','loan_success']); y_cls=model_scaled['loan_success'].astype(int)
X_train,X_test,y_train,y_test=train_test_split(X_cls,y_cls,test_size=.30,random_state=SEED,stratify=y_cls)
cv_strategy=RepeatedKFold(n_splits=3,n_repeats=1,random_state=SEED)
def metrics(y_true,p):
    cm=confusion_matrix(y_true,p)
    return {'accuracy':float(accuracy_score(y_true,p)),'precision':float(precision_score(y_true,p,zero_division=0)),
            'recall':float(recall_score(y_true,p,zero_division=0)),'f1':float(f1_score(y_true,p,zero_division=0)),
            'confusion_matrix':cm.astype(int).tolist(),'negative_recall':float(cm[0,0]/cm[0].sum())}
logit=LogisticRegression(solver='liblinear',max_iter=1500,random_state=SEED).fit(X_train,y_train)
pred=logit.predict(X_test); m_log=metrics(y_test,pred)
log_coefs=pd.Series(logit.coef_[0],index=X_cls.columns)
m_log['top_positive_coefficients']=[{'feature':str(k),'coefficient':float(v)} for k,v in log_coefs.nlargest(10).items()]
m_log['top_negative_coefficients']=[{'feature':str(k),'coefficient':float(v)} for k,v in log_coefs.nsmallest(10).items()]
tree=DecisionTreeClassifier(max_depth=5,random_state=SEED).fit(X_train,y_train)
pred=tree.predict(X_test); m_tree=metrics(y_test,pred)
rf=RandomForestClassifier(random_state=SEED,n_jobs=-1)
rf_space={'n_estimators':[100,150,250],'max_depth':[None,8,12],'min_samples_split':[2,5,10],'min_samples_leaf':[1,2,4],'class_weight':[None,'balanced_subsample']}
rf_search=RandomizedSearchCV(rf,rf_space,n_iter=5,cv=cv_strategy,scoring='f1',random_state=SEED,n_jobs=-1,refit=True,verbose=1)
rf_search.fit(X_train,y_train)
best_rf=rf_search.best_estimator_; pred=best_rf.predict(X_test); m_rf=metrics(y_test,pred)
m_rf['best_params']={k:(v.item() if hasattr(v,'item') else v) for k,v in rf_search.best_params_.items()}; m_rf['best_cv_f1']=float(rf_search.best_score_)
mlp=MLPClassifier(random_state=SEED,early_stopping=True,validation_fraction=.1,n_iter_no_change=10)
mlp_space={'hidden_layer_sizes':[(40,),(70,),(50,30)],'activation':['relu','tanh'],'solver':['adam'],'alpha':[0.0001,0.001,0.01],'learning_rate_init':[0.001,0.003],'max_iter':[160]}
mlp_search=RandomizedSearchCV(mlp,mlp_space,n_iter=4,cv=cv_strategy,scoring='f1',random_state=SEED,n_jobs=-1,refit=True,verbose=1)
mlp_search.fit(X_train,y_train)
best_mlp=mlp_search.best_estimator_; pred=best_mlp.predict(X_test); m_mlp=metrics(y_test,pred)
m_mlp['best_params']={k:(list(v) if isinstance(v,tuple) else (v.item() if hasattr(v,'item') else v)) for k,v in mlp_search.best_params_.items()}; m_mlp['best_cv_f1']=float(mlp_search.best_score_); m_mlp['n_iter_']=int(best_mlp.n_iter_)
shap_sample=X_test.sample(n=min(400,len(X_test)),random_state=SEED)
explainer=shap.TreeExplainer(best_rf)
sv=explainer(shap_sample)
vals=np.asarray(sv.values)
base=np.asarray(sv.base_values)
if vals.ndim==3:
    pos_vals=vals[:,:,1]
    pos_base=base[:,1] if base.ndim==2 else np.repeat(base[1],len(shap_sample))
elif vals.ndim==2:
    pos_vals=vals
    pos_base=base if base.ndim==1 else np.repeat(float(base),len(shap_sample))
else:
    raise RuntimeError(f'Unexpected SHAP shape: {vals.shape}')
mean_abs=np.mean(np.abs(pos_vals),axis=0)
order=np.argsort(mean_abs)[::-1][:20]
shap_global=[{'feature':str(X_cls.columns[i]),'mean_abs_shap':float(mean_abs[i])} for i in order]
row=0
local_order=np.argsort(np.abs(pos_vals[row]))[::-1][:20]
shap_local={'base_value':float(pos_base[row]),'predicted_probability':float(best_rf.predict_proba(shap_sample.iloc[[row]])[0,1]),
            'predicted_class':int(best_rf.predict(shap_sample.iloc[[row]])[0]),'actual_class':int(y_test.loc[shap_sample.index[row]]),
            'contributions':[{'feature':str(X_cls.columns[i]),'feature_value':float(shap_sample.iloc[row,i]),'shap_value':float(pos_vals[row,i])} for i in local_order]}
classification={'Logistic Regression':m_log,'Decision Tree':m_tree,'Random Forest Optimized':m_rf,'MLP Optimized':m_mlp}
result={
 'part_shapes':part_shapes,'initial_shape':initial_shape,'initial_dtypes':initial_dtypes,'initial_nulls':initial_nulls,'describe_numeric':desc,'head':head,
 'cleaning':{'impute_values':impute_values,'final_shape_raw':list(model_raw.shape),'final_shape_scaled':list(model_scaled.shape),'feature_count_classification':int(X_cls.shape[1]),'remaining_nulls':int(model_scaled.isnull().sum().sum())},
 'eda':{'success_counts':{str(int(k)):int(v) for k,v in success_counts.items()},'success_rate':success_rate,'funded_amount_stats':funded_stats,'annual_income_stats':annual_stats,'annual_income_funded_amount_corr':corr,'term_success_rates':term_rates,'hist_counts':hist_counts.astype(int).tolist(),'hist_edges':[float(x) for x in hist_edges]},
 'regression':{'simple':simple,'multivariable':multi},
 'classification_split':{'train_shape':list(X_train.shape),'test_shape':list(X_test.shape),'train_success_rate':float(y_train.mean()),'test_success_rate':float(y_test.mean()),'cv':'RepeatedKFold(n_splits=3, n_repeats=1, random_state=42)'},
 'classification':classification,'shap':{'global':shap_global,'local':shap_local}
}
with open(outdir/'results.json','w',encoding='utf-8') as f: json.dump(result,f,ensure_ascii=False,indent=2)
print('Wrote',outdir/'results.json')
print(json.dumps({'initial_shape':initial_shape,'success_rate':success_rate,'simple':simple,'multi_r2':multi['r2'],'classification':{k:{m:v[m] for m in ['accuracy','precision','recall','f1','negative_recall']} for k,v in classification.items()},'rf_params':m_rf['best_params'],'mlp_params':m_mlp['best_params']},indent=2))
