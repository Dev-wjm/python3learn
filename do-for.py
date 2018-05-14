# -*- coding: utf-8 -*- 
classmates = ['xiaoming','xiaohong','xiaoqiang']
for item in classmates:
  print( item ) 

# range()：可以生成一个整数序列
print(list(range(10)));   # output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for x in range(101):
  sum += x

print(sum)