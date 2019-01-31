import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#xlrd, openpyxl

df = pd.read_excel('C:/Python/section4/excel_s1.xlsx', header=0)

#컬럼값 수정
#df['State'] = df['State'].str.replace(' ','|')
#print(df)

#평균컬럼 추가
df['Avg'] = df[['2003','2004','2005']].mean(axis=1).round(2)
#print(df)

#합계컬럼 추가
df['Sum'] = df[['2003','2004','2005']].sum(axis=1).round(2)
print(df)

#최대값 출력
print(df[['2003','2004','2005']].max(axis=0))

#최소값 출력
print(df[['2003','2004','2005']].min(axis=0))

#상세 정보 출력
print(df.describe())
