import matplotlib.pyplot as plt

#리스트 범위(x축)
x = list(range(-1000,1000))

#리스트 범위(y축)
y = [v*v for v in x]
#for v in x:
#    y.append(v*v)

#차트설정
plt.plot(x,y)
#차트실행
plt.show()
