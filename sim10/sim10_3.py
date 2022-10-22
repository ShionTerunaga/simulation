#ペース走導入！！！
import math
import random
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
road=[
  1.1,
  1.1,
  1.1,
  1.1,
  1.1,
  1,
  1.1,
  0,
  0,
  1.1,
  1.1,
  1.1,
  1.1,
  1
]
wether=1
day_length=14
menu=[
  'jog(4分59秒~4分)',
  'jog(4分59秒~4分)',
  'jog(4分59秒~4分)',
  'jog(4分59秒~4分)',
  'jog(~5分)',
  'ペース走',
  'jog(4分59秒~4分)',
  'OFF',
  'OFF',
  'jog(~5分)',
  'jog(4分59秒~4分)',
  'jog(4分59秒~4分)',
  'jog(~5分)',
  'ペース走'
  ]
au=[
  1.5,
  1.5,
  1.5,
  1.5,
  1,
  3.5,
  1.5,
  0,
  0,
  1,
  1.5,
  1.5,
  1,
  3.5
]
x=list(range(1,day_length+1))
distance=[
  9.09,
  10.06,
  11.07,
  12.11,
  8.15,
  10,
  8.4,
  0,
  0,
  15.94,
  11.32,
  12.04,
  6.3,
  10
]
trimp=[]
fig=[]
fit=[]
par=[]
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


print(f'最終日:フィットネス={fit[-1]},疲労={fig[-1]},パフォーマンス={par[-1]}')

file_df=pd.DataFrame(zip(menu,au,distance,fit,fig,par),columns=['menu','au','distance','fitness','fatigue','performance'])
figure=plt.figure()
print(file_df)
file_df.to_excel('./sim10_2.xlsx')
plt.plot(x,fit,color='red')
plt.plot(x,fig,color='blue')
plt.plot(x,par,color='yellow')
plt.xlim(1,day_length)
plt.ylim(-400,400)
plt.show()

figure.savefig("./sim10_2.png")



