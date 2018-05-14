# -*- coding: utf-8 -*- 
# 切片操作   list[起始位置:结束位置:间隔个数] 
l = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(l[0:3])       # [n:m] 取 第 N 到 第 M 个元素   output:['Michael', 'Sarah', 'Tracy']
print(l[:3])        # 等同上面              output:['Michael', 'Sarah', 'Tracy']
print(l[1:3])       # output:['Sarah', 'Tracy']

l2 = list(range(100))
print(l2)
print(l2[:10:2])      #output: [0, 2, 4, 6, 8]  第三个参数间隔个数(每几个数取一次)