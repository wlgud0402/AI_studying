# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


path = '/Library/Fonts/NanumBarunGothic.otf'
font_name = font_manager.FontProperties(fname=path).get_name()

rc('font', family=font_name)

data = [242, 256, 237, 223, 263, 81, 46]  # 실제값
x_data = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']  # x축값

# 그래프제목
plt.title('일주일간 유동 인구수 데이터', fontsize=16)  # 큰제목
plt.xlabel('요일', fontsize=12)  # x축제목
plt.ylabel('유동 인구수', fontsize=12)  # y축제목

# 꺽은선 그래프 그리기
plt.scatter(x_data, data)
plt.plot(x_data, data)
plt.show()
