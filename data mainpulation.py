import pandas as pd

df = pd.read_csv("C:\\Users\\Vishwajeet\\Downloads\\sql\\SQL - Retail Sales Analysis_utf .csv", encoding="latin1")

print(df.info())

#print(df.head())  #showing data's staring 5 lines

#print(df.tail())  #showing data's ending 5 lines