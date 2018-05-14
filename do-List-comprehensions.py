# -*- coding: utf-8 -*- 
# 列表生成式
l = list(range(1, 11))    # 简单list生成
print(l)

#  生成[1x1, 2x2, 3x3, ..., 10x10]
l = [];
for x in range(1,11):
  l.append(x*x) 
print(l)

# 另外一种写法
l = [x * x for x in range(1,11)]
print(l)
# for 之后还能加 if 返回满足条件的元素
l = [x * x for x in range(1,11) if x%2 == 0]
print(l)
# 使用 多层 for 循环
l = [m+n for m in 'abc' for n in 'ABC']
print(l)

import os 
l = [d for d in os.listdir('.')]
print(l)


L = ['Hello', 'World', 18, 'Apple', None]
l = [x.lower() for x in L if isinstance(x,str)]
print(l)