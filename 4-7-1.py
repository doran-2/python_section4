from pandas import Series

#series1 선언
series1 = Series([921600, 943000, 940123, 123940, 129010])
print(series1)

#총 개수
print('count : ', series1.count())

#요약
print('describe :', series1.describe())

#인덱스접근
print(series1[2])


#series2 선언
series2 = Series([921600, 943000, 940123, 123940, 129010], index=['2016','2017','2018','2019','2020'])
print(series2)

#인덱스 순회
for date in series2.index:
    print('year :',date)

#값 순회
for price in series2.values:
    print('price :',price)


#series3 선언
series_g1 = Series([10,20,30],index=['n1','n2','n3'])
series_g2 = Series([50,40,25],index=['n3','n2','n1'])

#Series 병합
sum = series_g1 + series_g2
mul = series_g1 * series_g2
cul = (series_g1 * series_g2) * (0.5 + 1)

print('sum :\n', sum)
print('mul :\n', mul)
print('cul :\n', cul)
