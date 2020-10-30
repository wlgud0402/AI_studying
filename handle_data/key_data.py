# -*- coding: utf-8 -*- 
# 전체 선수들의 이름과 선호하는 발 정보 출력하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')

# ----------------------------------------------------

sub3 = fifa2019.loc[:,['Name', 'Preferred Foot']]# (:) 범위지정이 없으므로 모든행 , Name, Foot 만 출력
print(sub3)
