
'''
JSON 과제
https://jsonplaceholder.typicode.com/Comments에 대한 요청을
JSON 파일로 저장하고 Console에 Parsing하고 싶은 값을 출력
'''
import sys
import io
import urllib.request as req
import os.path
import simplejson as json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#url
url = 'https://jsonplaceholder.typicode.com/Comments'

#경로 & 파일명
savename = "C:/Python/section4/comment.json"

if not os.path.exists(savename):
    req.urlretrieve(url,savename)

items = json.loads(open(savename,'r',encoding='utf-8').read())

#출력
for item in items:
    print(str(item["id"]) + " : " + item["email"])
