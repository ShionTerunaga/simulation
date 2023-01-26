#2022年9月の練習メニューからのシミュレーション
import pandas as pd
import math
import matplotlib.pyplot as plt
#excelデータ取得
df=pd.read_excel("./deta.xlsx")

#AMデータをリスト変換
AM_au1=df['AM_au1'].tolist()
AM_au2=df['AM_au2'].tolist()
AM_distance1=df['AM_distance1'].tolist()
AM_distance2=df['AM_distance2'].tolist()
AM_road1=df['AM_road1'].tolist()
AM_road2=df['AM_road2'].tolist()
AM_wether=df['AM_wether'].tolist()
#PMデータをリスト変換
PM_au1=df['PM_au1'].tolist()
PM_au2=df['PM_au2'].tolist()
PM_distance1=df['PM_distance1'].tolist()
PM_distance2=df['PM_distance2'].tolist()
PM_road1=df['PM_road1'].tolist()
PM_road2=df['PM_road2'].tolist()
PM_wether=df['PM_wether'].tolist()

length=len(AM_au1)


trimp=[]
fig=[]
fit=[]
par=[]
x=[]
for i in range(length):
  x.append(i+1)
  AM1=AM_au1[i]*AM_distance1[i]*AM_road1[i]*AM_wether[i]
  AM2=AM_au2[i]*AM_distance2[i]*AM_road2[i]*AM_wether[i]
  PM1=PM_au1[i]*PM_distance1[i]*PM_road1[i]*PM_wether[i]
  PM2=PM_au2[i]*PM_distance2[i]*PM_road2[i]*PM_wether[i]
  sub=AM1+AM2+PM1+PM2
  trimp.append(sub)



fig.append(trimp[0]*2)
fit.append(trimp[0])
par.append(fit[0]-fig[0])
for i in range(1,length):
  fig.append(2*trimp[i]+fig[i-1]*math.exp(-1/15))
  fit.append(trimp[i]+fit[i-1]*math.exp(-1/45))
  par.append(fit[i]-fig[i])
for i in range(length):  
  fig[i]*=-1  
  

file_df=pd.DataFrame(zip(fit,fig,par),columns=['fitness','fatigue','performance'])
figure=plt.figure()
print(file_df)
file_df.to_excel('./sim7.xlsx')
plt.plot(x,fit,color='red',label="fitness")
plt.plot(x,fig,color='blue',label="fatigue")
plt.plot(x,par,color='yellow',label="performance")
plt.xlim(1,length)
plt.ylim(-800,800)
plt.legend(fontsize=14)
#plt.show()

figure.savefig("./sim7.png")