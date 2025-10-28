#data Cleaning

#drop unnneccessary columns

cols_to_drop=['max_salary','pay_period','company_id','views','med_salary','min_salary','applies','original_listed_time',
              'remote_allowed','application_url','job_posting_url','application_type','closed_time','currency',
              'compensation_type','normalized_salary','zip_code' , 'fips','posting_domain','expiry'
              ]
df.drop(columns=cols_to_drop,inplace=True,errors='ignore')

//fill missing values for those columns which are neccessary to Keep 

df['complany_name'].fillna('Unknown',inplace=True)
df['description'].fillna('Description not provided',inplace=True)
df['skills_desc'].fillna('skills not listed',inplace=True)
df['formatted_work_type'].fillna('Not Specified', inplace=True) #prtective step if future version have some mssing value for this attribute 

print(df)