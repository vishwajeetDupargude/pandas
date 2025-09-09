import pandas as pd

data={
    "Name":["vishwajeet","Vijay","sumit"],
    "Age":[21,20,19],
    "city":["solapur","Jalgaon","Dharashiv"]

}
df=pd.DataFrame(data)
print(df)

df.to_csv("output.csv",index=False)