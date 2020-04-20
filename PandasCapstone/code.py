# --------------
import pandas as pd

bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# --------------
# code starts here
banks = bank.drop('Loan_ID',axis=1)
print(banks.isnull())
bank_mode = pd.Series(banks.mode().iloc[0])
banks = banks.fillna(bank_mode)
print(banks.head(12))
#code ends here


# --------------
# Code starts here
import numpy as np
avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc=np.mean)
print(avg_loan_amount)



# code ends here



# --------------
# code starts here
mask = (banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')
loan_approved_se = banks[mask]
mask = (banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')
loan_approved_nse = banks[mask]
print(loan_approved_se.head(3))
percentage_se = (loan_approved_se['Loan_Status'].count()/614)*100
percentage_nse = (loan_approved_nse['Loan_Status'].count()/614)*100
print(percentage_se,percentage_nse)

# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
print(loan_term.head())
big_loan_term = loan_term[loan_term>=25].count()
print(big_loan_term)



# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.agg(np.mean)
print(mean_values)



# code ends here


