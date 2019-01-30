
# Sets(집합) 자료형 (순서X, 중복X, 추가O, 수정O, 삭제O)

# 선언
a =set()
b =set([1,2,3,4])

print(type(b))
print(b)

t = tuple(b)
print(type(t))
print(t[0:2])

l = list(b)
print(type(l))
print(l[0:2])

#Set을 사용하는 이유 (집합연산이 가능함)
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print ('s1 & s2', s1 & s2)
print ('s1 intersection s2', s1.intersection(s2))

print ('s1 | s2', s1 | s2)
print ('s1 union s2', s1.union(s2))

print ('s1 - s2', s1 - s2)
print ('s1 difference s2', s1.difference(s2))

#추가 제거
s3 = set([0,1,2,3])
s3.add(4)
print('s3 -',s3)

s3.remove(2)
print('s3 -',s3)
