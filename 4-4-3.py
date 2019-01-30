import sys
import io
import urllib.request as req
import os.path
import simplejson as json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#url
url = "https://api.github.com/repositories"

#경로 & 파일명
savename = "C:/Python/section4/repo.json"

if not os.path.exists(savename):
    req.urlretrieve(url,savename)

#items = json.load(open(savename,'r',encoding='utf-8'))
items = json.loads(open(savename,'r',encoding='utf-8').read())

#출력
for item in items:
    print(item["full_name"] + "---------->" + item["owner"]["url"])
