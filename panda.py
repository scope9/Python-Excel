# py -m venv venv
# venv creates a virtual environment which allows users to work in a new environment so installation of modules and libraries wont update the main python environment on this computers

import pandas as pd

# can import books from excel or csv file
excel_file = 'books.xlsx'

# read_excel is a function from panda which reads these files
# 1. read the file as excel
# df = pd.read_excel(excel_file)
# # reads the second page of excel
# df = pd.read_excel(excel_file, sheet_name=1)
# 2. specify the column using a parameter
df = pd.read_excel(excel_file, usecols=['title', 'authors'])


#df = pd.read_excel(excel_file, sheet_name=None)
# shows the second sheet on excel named books2 which displays the top 3 title and authors
# print(df["books2"].loc[0:3, 'title':'authors'])


print(df)
print("Below is JSON format")

# read the excel file in json format
new_json = df.to_json()
print(new_json)

# shows the first 2 rows
print("Below shows only the first 2 rows: ", df.head(2))
# shows the first 2 rows
print("Below shows only the last 2 rows: ", df.tail(2))
# shows the columns
print("This shows the filtered columns: ",df.columns)
# shows the types
print("This shows the types: ",df.dtypes)
# shows the top 5 "title" and authors
print(df[['title', 'authors']].head(5))


