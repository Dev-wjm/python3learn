# -*- coding: utf-8 -*- 
# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key,d[key])  

for val in d.values():
  print(val)

for key,value in d.items():
  print(key,value)

# 判断一个对象是否可迭代
from collections import Iterable
print(isinstance("ascsd",Iterable))

for i, value in enumerate(['A', 'B', 'C']):
  print(i,value)