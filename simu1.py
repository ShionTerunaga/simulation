#jog onlyのシミュレーション
import math
import random
from turtle import color
import matplotlib.pyplot as plt
road=1.1
wether=1
day_length=31
au=[]
x=[]
distance=[]
trimp=[]
fig=[]
fit=[]
par=[]

for i in range(day_length):
  x.append(i+1)
  distance.append(random.randrange(6,20))
  sub=random.randrange(1,3)
  if sub==1:
    au.append(1)
  else:
    au.append(1.5)

for i in range(day_length):
  trimp.append(round(au[i]*distance[i]*road*wether,3))

fig.append(trimp[0]*2)
fit.append(trimp[0])
par.append(fit[0]-fig[0])
fig[0]*=-1
for i in range(1,day_length):
  fig.append(2*trimp[i]+fig[i-1]*math.exp(-1/15))
  fit.append(trimp[i]+fit[i-1]*math.exp(-1/45))
  par.append(fit[i]-fig[i])
for i in range(1,day_length):  
  fig[i]*=-1  

print(fit)
print(fig)
print(par)

plt.plot(x,fit,color='red')
plt.plot(x,fig,color='blue')
plt.plot(x,par,color='yellow')
plt.xlim(1,day_length)
plt.ylim(-500,500)
plt.show()



