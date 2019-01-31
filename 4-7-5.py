import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2019,1,1)
end = datetime.datetime(2019,1,15)

#Google 정보 호출
#gs = web.DataReader('KRX: 035720', 'google', start, end) #구글 서비스 종료로 사용불가
df1 = web.DataReader("BAC", "iex", start, end)
#print(df1)

df2 = web.DataReader("AMZN", "iex", start, end)
#print(df2)

#윈도창 제목
fig = plt.figure('Chart Test')
fig.set_size_inches(10,6,forward=True)

#차트설정1
plt.plot(df1.index, df1['close'],'b',label='BAC')
plt.plot(df2.index, df2['close'],'r',label='AMZN')

#범례위치
plt.legend(loc='upper right')
#차트제목
plt.title("BAC & AMZN")

plt.xlabel('date')
plt.ylabel('close')

plt.show()
