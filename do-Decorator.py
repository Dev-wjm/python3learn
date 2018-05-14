# -*- coding: utf-8 -*- 
# 函数修饰器
def log(func):
  def wappers(*args,**kw):
    print("call %s():" % func.__name__)
    return func(*args,**kw)
  return wappers

@log
def now(x):
  print("2018-05-14")

now(10);