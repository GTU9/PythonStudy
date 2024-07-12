import pandas as pd
df=pd.read_csv("salaries_by_college_major.csv")

#상위 5개 출력
df.head()
#속성값 출력
df.columns
#해당 결측값 확인 (없으면 True)
df.isna()
#하위 5개 출력
df.tail()
#결측값 제거
clean_df = df.dropna(thresh=3)
# print(clean_df.tail())

print(
    # clean_df['Starting Median Salary']
    # clean_df['Starting Median Salary'].max()
    # clean_df['Starting Median Salary'].idxmax()
    # clean_df['Undergraduate Major'].loc[43]
)

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
# print(clean_df.head())

#오름차순 정렬
low_risk = clean_df.sort_values('Spread')
# print(low_risk[['Undergraduate Major', 'Spread']].head())

#내림차순 정렬
low_risk = clean_df.sort_values('Spread',ascending=False)
# print(low_risk[['Undergraduate Major', 'Spread']].head())

#그룹별로 분류 후 행의 수, 숫자값의 평균값
group_counts = clean_df.groupby('Group').count()
group_means = clean_df.groupby('Group').mean(numeric_only=True)