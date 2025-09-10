import pandas as pd

df = pd.read_csv("C:\\Users\\Vishwajeet\\Downloads\\sql\\SQL - Retail Sales Analysis_utf .csv", encoding="latin1")

print(df)

#How to select the specifies the columns
#How to filter rows
#how to combine the multiple conditon


#print(df["sale_date"])  #selecting the specifies column

print(df[["customer_id", "gender"]])   # for selecting multiple columns


#for Filterd rows

#filterd_rows= df[df["gender"] == "male"]
#print(filterd_rows)

rows=df[(df["gender"] == "male") & (df["age"]>40)]
print(rows)