import pandas as pd

data = pd.read_csv("CRDC2013_14.csv", encoding="Latin-1")

a=data["JJ"].value_counts()
b=data["SCH_STATUS_MAGNET"].value_counts()

print(a)
print(b)

print(pd.pivot_table(data,values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum"))

print(pd.pivot_table(data,values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum"))



