import pandas_datareader.data as web
import datetime

start = datetime.datetime(2019,1,1)
end = datetime.datetime(2019,1,31)

#Google 정보 호출
#gs = web.DataReader('KRX: 035720', 'google', start, end) #구글 서비스 종료로 사용불가
df = web.DataReader("BAC", "iex", start, end)
print(df)
