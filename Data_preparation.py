import pandas as pd
import numpy as np

df=pd.read_csv("postings.csv")
salries=pd.read_csv(r'C:\Users\rajko\OneDrive\Desktop\LinkedIn\jobs\salaries.csv')
postings_salaries=pd.merge(df, salries,on='job_id',how='inner')
companies=pd.read_csv(r'C:\Users\rajko\OneDrive\Desktop\LinkedIn\companies\companies.csv')
companies=companies.drop('description',axis=1)
companies.rename(columns={'name': 'company_name'}, inplace=True)
industries=pd.read_csv(r'C:\Users\rajko\OneDrive\Desktop\LinkedIn\companies\company_industries.csv')
final_companies=pd.merge(companies,industries,on='company_id',how='inner')
#creating final merging 
LdIn_data=pd.merge(postings_salaries,final_companies,on='company_name',how='inner')
LdIn_data_f=LdIn_data[['job_id','company_name','state','country','city','industry','work_type','currency_x','compensation_type_x','normalized_salary','max_salary_x','min_salary_x','sponsored','views','job_posting_url','application_url']]
LdIn_data_f.isnull()
LdIn_data_f.fillna('Nan')
print(LdIn_data_f.info())
print(LdIn_data_f.shape)
LdIn_data_f.to_csv("LdIn_data_f.csv",index=False)



