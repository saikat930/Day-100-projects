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
    "Data Type" : {"Name" : "","Age":"", "City": "", 'Salary': "","Email": "","Gender" :""}
}

df = pd.DataFrame(data)
report_df = pd.DataFrame(report)

def report_of_df(df,report_df):
    """IT FINDS THE MISSING VALUES, DUPLICATE VALUES AND DATA TYPE FOR EACH COLUMN"""
    report_df.loc['Name', 'Missing Values'] = df['Name'].isna().sum()
    report_df.loc['Age', 'Missing Values'] = df['Age'].isna().sum()
    report_df.loc['City', 'Missing Values'] = df['City'].isna().sum()
    report_df.loc['Salary', 'Missing Values'] = df['Salary'].isna().sum()
    report_df.loc['Email', 'Missing Values'] = df['Email'].isna().sum()
    report_df.loc['Gender', 'Missing Values'] = df['Gender'].isna().sum()

    report_df.loc['Name', 'Duplicate Values'] = df['Name'].duplicated().sum()
    report_df.loc['Age', 'Duplicate Values'] = df['Age'].duplicated().sum()
    report_df.loc['City', 'Duplicate Values'] = df['City'].duplicated().sum()
    report_df.loc['Salary', 'Duplicate Values'] = df['Salary'].duplicated().sum()
    report_df.loc['Email', 'Duplicate Values'] = df['Email'].duplicated().sum()
    report_df.loc['Gender', 'Duplicate Values'] = df['Gender'].duplicated().sum()

    report_df.loc['Name', 'Data Type'] = str(df['Name'].dtype)
    report_df.loc['Age', 'Data Type'] = str(df['Age'].dtype)
    report_df.loc['City', 'Data Type'] = str(df['City'].dtype)
    report_df.loc['Salary', 'Data Type'] = str(df['Salary'].dtype)
    report_df.loc['Email', 'Data Type'] = str(df['Email'].dtype)
    report_df.loc['Gender', 'Data Type'] = str(df['Gender'].dtype)

    return report_df

report_df = report_of_df(df,report_df)
print(report_df)

print("Total rows           : ",df.shape[0])
print("Total columns        : ",df.shape[1])
print("Total missing values : ",report_df['Missing Values'].sum())
print("Total Duplicate rows : ",df.duplicated().sum())

print("__PERCENTAGE OF MISSING VALUES FOR EACH COLUMN__")
print(df.isna().sum()/df.shape[0] * 100)

