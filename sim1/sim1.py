#jog onlyのシミュレーション
import math
import random
from turtle import color
import pandas as pd
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
for i in range(1,day_length):
  fig.append(2*trimp[i]+fig[i-1]*math.exp(-1/15))
  fit.append(trimp[i]+fit[i-1]*math.exp(-1/45))
  par.append(fit[i]-fig[i])
for i in range(day_length):  
  fig[i]*=-1  




print(f'最終日:フィットネス={fit[-1]},疲労={fig[-1]},パフォーマンス={par[-1]}')

file_df=pd.DataFrame(zip(au,distance,fit,fig,par),columns=['au','distance','fitness','fatigue','performance'])
figure=plt.figure()
print(file_df)
file_df.to_excel('./sim1.xlsx')
plt.plot(x,fit,color='red',label="fitness")
plt.plot(x,fig,color='blue',label="fatigue")
plt.plot(x,par,color='yellow',label="performance")
plt.legend()
plt.xlim(1,day_length)
plt.ylim(-500,500)
plt.show()

figure.savefig("./sim1.png")



