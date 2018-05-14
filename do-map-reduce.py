# -*- coding: utf-8 -*- 
# map(f,Iterable)
def func(x):
  return x
l =  list(map(func,"ancmaninsiin"))
print(l)

from functools import reduce
def fn(x,y):
  return x*10+y

result = reduce(fn,[1,3,5,7,9])     # reduce 函数需要两个参数
print(result)

l = ['a', 'n', 'c', 'm', 'a', 'n', 'i', 'n', 's', 'i', 'i', 'n']
def fn2(x,y):
  return x+y

result = reduce(fn2,l,"这是通过reduce:")    # 第三个参数初始值
print(result)

# lambda
func = lambda x: x+1
print(func(1))


# sorted
l1=[('a', 6), ('b', 5), ('c', 4), ('d', 3), ('e', 2)]
l2 = sorted(l1,key=lambda x:x[1])
print(l2)