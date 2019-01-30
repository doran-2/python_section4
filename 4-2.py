import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#다운로드 url
url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1159065100"
savaname = "C:/Python/section4/forecast.xml"

if not os.path.exists(savaname):
    req.urlretrieve(url, savaname)
    print('다운로드 확인')

#BeautifulSoup 파싱
xml = open(savaname, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'lxml')

#
for data in soup.find_all("data"):
    print('hour:',data.find("hour").string,end='')
    print(' temp:',data.find("temp").string,end='')
    print(' wfkor:',data.find("wfkor").text)
