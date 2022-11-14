import pandas as pd
import math
import matplotlib.pyplot as plt
#excelデータ取得
df=pd.read_excel("./11_19.xlsx")

#データをリスト変換
au1=df['au1'].tolist()
au2=df['au2'].tolist()
au3=df['au3'].tolist()
distance1=df['distance1'].tolist()
distance2=df['distance2'].tolist()
distance3=df['distance3'].tolist()
road1=df['road1'].tolist()
road2=df['road2'].tolist()
road3=df['road3'].tolist()
wether=df['wether'].tolist()

length=len(au1)


trimp=[]
fig=[]
fit=[]
par=[]
x=[]
for i in range(length):
  x.append(i+1)
  menu1=au1[i]*distance1[i]*road1[i]*wether[i]
  menu2=au2[i]*distance2[i]*road2[i]*wether[i]
  menu3=au3[i]*distance3[i]*road3[i]*wether[i]
  sub=menu1+menu2+menu3
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
  

file_df=pd.DataFrame(zip(trimp,fit,fig,par),columns=['trimp','fitness','fatigue','performance'])
figure=plt.figure()
print(file_df)
file_df.to_excel('./sim12_2.xlsx')
plt.plot(x,fit,color='red')
plt.plot(x,fig,color='blue')
plt.plot(x,par,color='yellow')
plt.xlim(1,length)
plt.ylim(-800,800)
#plt.show()

figure.savefig("./sim12_2.png")