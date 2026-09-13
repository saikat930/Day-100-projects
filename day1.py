import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Riya", "Rahul", "Sneha", "Arjun", "Priya", None, "Neha"],
    "Age": [20, 22, np.nan, 21, 21, 23, 20, 25],
    "City": ["Delhi", "Mumbai", "Delhi", "Kolkata", "Mumbai", None, "Delhi", "Delhi"],
    "Salary": [30000, 45000, 35000, np.nan, 50000, 45000, 30000, 60000],
    "Email": [
        "aman@gmail.com",
        "riya@gmail.com",
        "rahulgmail.com",
        "sneha@gmail.com",
        None,
        "priya@gmail.com",
        "aman@gmail.com",
        "neha@gmail.com"
    ],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"]
}

report = {
    "Missing Values" : {"Name" :0,"Age": 0, "City": 0, 'Salary': 0,"Email": 0,"Gender" :0},
    "Duplicate Values" : {"Name" : 0,"Age" : 0, "City": 0, 'Salary': 0,"Email": 0,"Gender" :0},
    "Data Type" : {"Name" : 0,"Age":0, "City": 0, 'Salary': 0,"Email": 0,"Gender" :0}
}

df = pd.DataFrame(data)
report_df = pd.DataFrame(report)

def report_of_df(df,report_df):
    """IT FINDS THE MISSING VALUES, DUPLICATE VALUES AND DATA TYPE FOR EACH COLUMN"""
    report_df['Missing Values']['Name'] = df['Name'].isna().sum()
    report_df['Missing Values']['Age'] = df['Age'].isna().sum()
    report_df['Missing Values']['City'] = df['City'].isna().sum()
    report_df['Missing Values']['Salary'] = df['Salary'].isna().sum()
    report_df['Missing Values']['Email'] = df['Email'].isna().sum()
    report_df['Missing Values']['Gender'] = df['Gender'].isna().sum()

    report_df['Duplicate Values']['Name'] = df['Name'].duplicated().sum()
    report_df['Duplicate Values']['Age'] = df['Age'].duplicated().sum()
    report_df['Duplicate Values']['City'] = df['City'].duplicated().sum()
    report_df['Duplicate Values']['Salary'] = df['Salary'].duplicated().sum()
    report_df['Duplicate Values']['Email'] = df['Email'].duplicated().sum()
    report_df['Duplicate Values']['Gender'] = df['Gender'].duplicated().sum()


    report_df['Data Type']['Name'] = df['Name'].dtype
    report_df['Data Type']['Age'] = df['Age'].dtype
    report_df['Data Type']['City'] = df['City'].dtype
    report_df['Data Type']['Salary'] = df['Salary'].dtype
    report_df['Data Type']['Email'] = df['Email'].dtype
    report_df['Data Type']['Gender'] = df['Gender'].dtype
    return report_df

report_df = report_of_df(df,report_df)
print(report_df)

print("Total rows           : ",df.shape[0])
print("Total columns        : ",df.shape[1])
print("Total missing values : ",report_df['Missing Values'].sum())
print("Total Duplicate rows : ",df.duplicated().sum())

print("__PERCENTAGE OF MISSING VALUES FOR EACH COLUMN__")
print(df.isna().sum()/df.shape[0] * 100)

