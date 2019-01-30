
# List (순서O, 중복O, 수정O, 삭제O)

#선언
a =[]
b = list()
c = [0,0,1,2]
d = [0,1,'car','apple','apart']
e = [0,1,['car','apple','apart']]

#인덱싱
print("#=====================================================================#")
print('d -', type(d), d)
print('d -', d[1])
print('c -', c[0] + c[1] +c[2])
print('e -', e[-1][1])
print('e -', e[2][1])

#슬라이싱
print("#=====================================================================#")
print('d -', d[0:3])
print('d -', d[2:])

#연산
print("#=====================================================================#")
print('c + d', c+d)
print('c * 3', c*3)
print('hi + c[0]','hi' + str(c[0]))

#리스트의 수정 삭제
print("#=====================================================================#")
c[0] =4
print('c -', c)
c[1:2]=['a','b','c']
print('c -', c)
c[1]=['a','b','c']
print('c -', c)
c[1:3]=[]
print('c -', c)
del c[3]
print('c -', c)

#리스트 함수
print("#=====================================================================#")
f =[5,2,3,1,4]
print('f -',f)

f.append(6)
print('f -',f)

f.sort()
print('f -',f)

f.reverse()
print('f -',f)

print('f -',f.index(4))
print('f -',f[4])
print('f count-',f.count(1)) #해당원소를 찾기

f.remove(2) #해당 원소를 지우기
print('f -',f)

print('f -',f.pop())
print('f -',f)

ex = [8,9]
f.extend(ex)
print('f -',f)

#리스트 삭제 : del, remove, pop

while f:
    g = f.pop()
    print(g)
