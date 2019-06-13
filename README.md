1.프로젝트 목적 및 동기

저희 아버지가 이제 곧 환갑을 바라보십니다. 이제 노후 걱정을 하시는데 저는 아직 부모님의 노후에 대해 깊게 생각한 적이 없습니다. 
그래서 ‘65세 이상 노인들에게 많이 발생하는 질병’에 대해 알아봄으로 부모님의 건강에 대해 조금 더 관심을 가지는 계기가 될 것 같습니다. 
그리고 진료비와 내원일수 같은 항목들을 비교함으로 보험등 미리 대비를 할 수 있을 것입니다. 

2.프로젝트 개요

진료실 인원이 가장 많은 질병  top 5 그래프 ->내원일수가 가장 많은 질병 top5 그래프 -> 
급여일수가 가장 많은 질병 top5 그래프 -> 내원일수와 진료비 그래프 -> 급여일수와 진료비 그래프 

3.프로젝트 구현 내용

3.1 개발환경

python 언어를 사용하여 개발을 했습니다. python script에 코드를 짰고 제 개인 노트북을 주로 이용하였습니다. 
새로 산 노트북이라 잘 돌아갔지만 화면이 작아 침침한 눈으로 코드를 짰습니다.

3.2.CODE

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = "c:/windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
df = pd.read_csv('care.csv',encoding = 'cp949')

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

3.3 기능 설명

표1,2,3: 진료실 인원이 많은 병명, 내원일수가 가장 높은 병명, 급여일수가 가장 높은 병명 top 5를 선정하여 각각의 병명을 비교한다. 
각각의 병명 수가 조금씩 다른데 공통적으로 고혈압 병명이 가장 높은 수치를 나타내고 있다. 

표 4번: 내원 일수를 x축으로 진료비를 y 축으로 둔 그래프를 그려 내원 일수와 진료비의 상관관계를 알 수 있다. 
내원 일수가 높을수록 진료비가 높은 것을 보아 둘은 정비례 관계임을 알 수 있다. 

표5번: 급여 일수를 x축으로 진료비를 y축으로 두어 급여일수와 진료비의 상관관계를 알 수 있다. 
그래프를 보아 급여일수와 진료비 또한 정비례 관계임을 알 수 있다.

4.프로젝트 개발 소감

65세 이상 노인의 질병을 분석함으로 아직은 먼 미래 같았던 부모님의 노후에 대해 다시 생각하는 계기가 된 것 같습니다. 
그리고 당뇨, 고혈압 같은 익숙한 병명부터 협심증 같은 처음 들어보는 병명까지 다양한 병명들을 알게 되었습니다. 
나중에 부모님 보험 드실 때 참고할 예정입니다. 파이썬으로 공공데이터를 분석하는 것은 이번에 처음 배워 PIP와 Pandas, matplotlib이 
굉장히 낯설게 느껴졌는데 직접 주제를 정하고 코드를 짜니 프로젝트를 마무리 지었을 땐 제법 익숙해진 것 같습니다. 
제일 첫단계 아니, 0단계라 할 수 있는 PIP 설치하는 과정에서부터 난관을 봉착했고 그 뒤로 순조롭게 되는듯 싶더니 ‘급여일수’를 부르는 과정에서 
keyword가 계속 잘못 되었다고 뜨는 등 많은 고난을 겪었지만 그래도 계획보고서에 적은 것들을 대부분 실현 시켜 굉장히 만족스럽습니다. 
한가지 아쉬운 점은, 계획 보고서에서는 내원일수와 급여일수를 더하여 그 중 top 5를 그래프로 만드는 것이 있었는데, 구글을 뒤져보고 고민했는데도 결국 성공하지 못했습니다. 
지금 기한이 없어 그 부분을 실현하지 못했지만 나중에 다시 시도해볼 예정입니다. 
사실 요 근래 프로그래밍에 많은 자신감이 떨어져있었는데 이번 프로젝트로 다시 프로그래밍에 흥미를 갖게 되었고 저에게 좋은 기폭제가 될 거라 생각됩니다. 
