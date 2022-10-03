#途中から練習しなくなるシミュレーション
import math
import random
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
road=[]
wether=1
day_length=31
au=[]
x=[]
distance=[]
trimp=[]
fig=[]
fit=[]
par=[]
menu=[]
a=4
b=7
for i in range(day_length):
  x.append(i+1)
  if i<=15 and (i+1)==a:
    a+=7
    sub=random.randrange(1,3)
    road.append(1)
    if sub==1:
      menu.append('12km_pacerunnning')
      au.append(3.5)
      distance.append(12)
    else:
      menu.append('10km_pacerunnning')
      au.append(4)
      distance.append(10)
  elif i<=15 and (i+1)==b:
    b+=7    
    sub=random.randrange(1,3)
    road.append(1)
    if sub==1:
      menu.append('1000m_interval×5')
      au.append(5)
      distance.append(5)
    else:
      menu.append('2000m_interval×5')
      au.append(4.5)
      distance.append(10)
  elif i > 15 or (i==(a-7) or i==(b-7) or i==(b-6))and i!=0:
    menu.append('OFF')
    au.append(0)
    distance.append(0)
    road.append(0)
  else:
    road.append(1.1)
    menu.append('jog')  
    distance.append(random.randrange(6,20))
    sub=random.randrange(1,3)
    if sub==1:
      au.append(1)
    else:
      au.append(1.5)

for i in range(day_length):
  trimp.append(round(au[i]*distance[i]*road[i]*wether,3))

fig.append(trimp[0]*2)
fit.append(trimp[0])
par.append(fit[0]-fig[0])
for i in range(1,day_length):
  fig.append(2*trimp[i]+fig[i-1]*math.exp(-1/15))
  fit.append(trimp[i]+fit[i-1]*math.exp(-1/45))
  par.append(fit[i]-fig[i])
for i in range(day_length):  
  fig[i]*=-1  

file_df=pd.DataFrame(zip(menu,au,distance,fit,fig,par),columns=['menu','au','distance','fitness','fatigue','performance'])
figure=plt.figure()
print(file_df)
file_df.to_excel('./sim6.xlsx')
plt.plot(x,fit,color='red')
plt.plot(x,fig,color='blue')
plt.plot(x,par,color='yellow')
plt.xlim(1,day_length)
plt.ylim(-800,800)
#plt.show()

figure.savefig("./sim6.png")



