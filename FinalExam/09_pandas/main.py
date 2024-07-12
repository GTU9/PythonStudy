import pandas as pd
df=pd.read_csv("salaries_by_college_major.csv")
print(df.sort_values("Starting Median Salary"))
print(df.groupby("Group").mean(numeric_only=True))