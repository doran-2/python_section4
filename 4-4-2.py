import sys
import io
import simplejson as json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Dic(Json) 선언

'''
data ={people:[
    'name' : 'Do',
    'from' : 'Seoul',
    'website' : 'sk.com',
    'grade' : [95,77,89,91]
]}
'''

data = {}
data['people'] = []
data['people'].append({
    'name' : 'Do',
    'from' : 'Seoul',
    'website' : 'sk.com',
    'grade' : [95,77,89,91]
})
data['people'].append({
    'name' : 'Kim',
    'from' : 'Busan',
    'website' : 'google.com',
    'grade' : [60,80,74,92]
})
data['people'].append({
    'name' : 'Park',
    'from' : 'Incheon',
    'website' : 'daum.net',
    'grade' : [80,73,81,88]
})

#json 파일쓰기 (dump)
with open('C:/Python/section4/member.json','w') as outfile:
    json.dump(data,outfile)

with open('C:/Python/section4/member.json','r') as infile:
    r = json.load(infile)
    print(type(r))
    print(r)
    print('--------------------------------')

    for p in r['people']:
        print("-----------------")
        print('Name :', p['name'])
        print('From :', p['from'])
        print('Website :', p['website'])

        grade =''
        for g in p['grade']:
            grade = grade + ' ' + str(g)
        print('Grade :',grade.lstrip())
