# -*- coding: utf-8 -*- 
# 선수들이 선호하는 발의 종류 데이터를 막대그래프로 나타내기

import pandas as pd                      # 그래프를 출력하기 위한 모듈  

fifa2019 = pd.read_csv('fifa2019.csv')

# --------------------------------------------------------------------

import matplotlib.pyplot as plt          # 그래프를 출력하기 위한 모듈

print(fifa2019['Preferred Foot'].value_counts()) #왼발 오른발 수

fifa2019['Preferred Foot'].value_counts().plot(kind='bar') #막대 그래프
plt.legend()                             # 범례 표시하기
plt.show()                               # 그래프 출력하기

fifa2019['Preferred Foot'].value_counts().plot(kind='pie', autopct ='%1.f%%')
plt.legend()
plt.show()

