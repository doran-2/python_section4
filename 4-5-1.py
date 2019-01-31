import sys
import io
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 기본읽기
#df = pd.read_csv("C:/Python/section4/csv_s1.csv")
#print(df)

# 행스킵
#df = pd.read_csv("C:/Python/section4/csv_s1.csv", skiprows=[0])
#print(df)

# 행스킵, 헤더 생략
#df = pd.read_csv("C:/Python/section4/csv_s1.csv", skiprows=[0], header=None)
#print(df)

# 헤더 정의
#df = pd.read_csv("C:/Python/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2016,2017,2018])
#print(df)

# 인덱스 컬럼 정의
#df = pd.read_csv("C:/Python/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2016,2017,2018], index_col=[0])
#print(df)

#특정값 치환
#df = pd.read_csv("C:/Python/section4/csv_s1.csv", skiprow s=[0], header=None, names=["Month",2016,2017,2018], index_col=[0],na_values=['JAN'])
#print(df)
#print(pd.isnull(df))

# 실습정리 및 인덱스 재정의
#df = pd.read_csv("C:/Python/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2016,2017,2018])
#print(df.index)
#print(list(df.index))
#print(df.index.values)
#print(df.index.values.tolist())

#기본 명령으로 인덱스를 재정희 하는 부분 값이 많아질 경우 굉장히 많은 코드 및 작업이 요구됨
#print(df.rename(index={0:"aa",1:"bb",2:"cc"}))

#같은 명령을 람다식을 사용할 경우 수월하게 작업이 가능
#print(df.rename(index=lambda x:x*10))

#읽기
df2 = pd.read_csv("C:/Python/section4/csv_s2.csv", sep=";", skiprows=[0], header=None, names=["Name","Test1","Test2","Test3","Final","Grade"])
#print(df2)

#컬럼내용 변경
#df2['Grade'] = df2['Grade'].str.replace('C','A++')
#print(df2)

#평균 컬럼 추가
df2['Avg'] = df2[["Test1","Test2","Test3","Final"]].mean(axis=1)
#print(df2)

#합계 컬럼 추가
df2['Sum'] = df2[["Test1","Test2","Test3","Final"]].sum(axis=1)
print(df2)
