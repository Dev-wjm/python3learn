# -*- coding: utf-8 -*- 
# 生成器  [] 改成 ()
g = (x for x in range(1,10))
print(g)        # output: <generator object <genexpr> at 0x000001F7A84BB0A0>
print(next(g))      # 获取方式  
for x in g:
  print(x) 

def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n = n + 1
  return 'done'

g = fib(6)
for x in g:
  print(x)