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
    'website' : 'sk.com'
]}
'''

data = {}
data['people'] = []
data['people'].append({
    'name' : 'Do',
    'from' : 'Seoul',
    'website' : 'sk.com'
})
data['people'].append({
    'name' : 'Kim',
    'from' : 'Busan',
    'website' : 'google.com'
})
data['people'].append({
    'name' : 'Park',
    'from' : 'Incheon',
    'website' : 'daum.net'
})

#print(data)

#{'people': [{'name': 'Do', 'website': 'sk.com', 'from': 'Seoul'}, {'name': 'Kim', 'website': 'google.com', 'from': 'Busan'}, {'name': 'Park', 'website': 'daum.net', 'from': 'Incheon'}]}

#Dict(json) -> Str
e = json.dumps(data, indent=4)
print(type(e))
print(e)

#Str -> Dict(json)
d = json.loads(e)
print(type(d))
print(d)

#파일로 쓰기
with open('C:/Python/section4/member.json','w') as outfile:
    outfile.write(e)

#파일 읽어오기
with open('C:/Python/section4/member.json','r') as infile:
    r = json.loads(infile.read())
    #print(type(r))
    #print(r)
    for p in r['people']:
        print("-----------------")
        print('Name :', p['name'])
        print('From :', p['from'])
        print('Website :', p['website'])
