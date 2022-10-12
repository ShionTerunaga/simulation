#jog onlyのシミュレーション
import math
import random
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
road=1.1
wether=1
day_length=10
au=[1.5,1.5,1.5,1,1,0,1,1,1,1]
x=list(range(1,11))
distance=[20,20,17,6,6,6,8,6,6,6]
trimp=[]
fig=[]
fit=[]
par=[]
for i in range(day_length):
  trimp.append(round(au[i]*distance[i]*road*wether,3))

fig.append(trimp[0]*2)
fit.append(trimp[0])
par.append(fit[0]-fig[0])
for i in range(1,day_length):
  fig.append(2*trimp[i]+fig[i-1]*math.exp(-1/15))
  fit.append(trimp[i]+fit[i-1]*math.exp(-1/45))
  par.append(fit[i]-fig[i])
for i in range(day_length):  
  fig[i]*=-1  


'''
print(au)
print(distance)
print(fit)
print(fig)
print(par)
'''
file_df=pd.DataFrame(zip(au,distance,fit,fig,par),columns=['au','distance','fitness','fatigue','performance'])
figure=plt.figure()
print(file_df)
file_df.to_excel('./sim9.xlsx')
plt.plot(x,fit,color='red')
plt.plot(x,fig,color='blue')
plt.plot(x,par,color='yellow')
plt.xlim(1,day_length)
plt.ylim(-400,400)
plt.show()

figure.savefig("./sim9.png")



