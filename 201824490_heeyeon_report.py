import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = "c:/windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
df = pd.read_csv('국민건강보험공단_65세이상노인질병소분류별다빈도상병급여현황_20171231.csv',encoding = 'cp949')

df3= df.sort_values(by = '진료실인원', ascending=True).tail(5)
df4 = df3[['상      병      명', '진료실인원']]
df4 = df4.set_index('상      병      명')
df4.plot(kind = 'bar')


df5 =df.sort_values(by = '내원일수', ascending=True).tail(5)
df6 = df5[['상      병      명', '내원일수']]
df6 = df6.set_index('상      병      명')
df6.plot(kind = 'bar')

df9 =df.sort_values(by = ' 급여일수', ascending=True).tail(5)
df10 = df9[['상      병      명', ' 급여일수']]
df10 = df10.set_index('상      병      명')
df10.plot(kind = 'bar')

plt.show()

x = df5['내원일수']
x2 = df5['상      병      명']
df7 =df5.sort_values(by = '진료비', ascending=True)
y =  df7['진료비']
plt.scatter(x,y)
plt.xticks(x,x2)
plt.xlabel('내원일수')
plt.ylabel('진료비')

plt.show()

w = df9[' 급여일수']
w2 = df9['상      병      명']
df11 =df9.sort_values(by = '진료비', ascending=True)
z =  df11['진료비']
plt.scatter(w,z)
plt.xticks(w,w2)
plt.xlabel('급여일수')
plt.ylabel('진료비')


plt.show()






