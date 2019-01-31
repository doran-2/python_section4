import matplotlib.pyplot as plt

#fig객체
fig = plt.figure()

#서브 슬롯 생성(2행1열)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

#리스트 범위(x축)
x = range(0,100)

#리스트 범위(y축)
y = [v*v for v in x]

#리스트 범위(y축)
z = [v*v*2 for v in x]

#멀티라인 1행1열
ax1.plot(x,y,'b',z,'r')

#바차트 2행 1열
ax2.bar(x,z)

plt.show()
