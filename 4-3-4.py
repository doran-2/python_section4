
# 딕션너리 자료형 (Key, Value) (순서X, 중복X, 수정O, 삭제O)

# 선언
a = {'name' : 'Do', 'phone' : '010-XXXX-XXXX', 'birth' : 20190101}
b = {0:'hello world!'}
c = {'arr':[0,1,2,3]}

print(type(a),a)

#출력
print('a -',a['name'])
print('a -',a.get('name'))
#키 값을 가져오는 점에서 같으나  없는 키값을 가져올 경우
#처음 방법은 Exception이 발생, 두번째 방법은 None 값을 가져옴
print('c -',c.get('arr'))

#딕셔너리 추가
a['address'] ='Seoul'
print('a -',a)
a['rank'] = [1,2,3]
print('a -',a)

print('a keys', list(a.keys()))
print('a keys', a.keys())

print('a values', list(a.values()))
print('a values', a.values())

#item을 사용할 경우 튜플로 값을 반환함
print('a items', a.items())

#키값의 유무 확인
print('a -', 'name' in a)
print('a -', 'city' in a)
