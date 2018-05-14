# -*- coding: utf-8 -*- 
# 函数的参数顺序:  必选(位置)参数  默认值参数  *可变参数--tuple    *,命名关键字参数   **关键字参数---dict
def my_abs(x):
  if not isinstance(x,(int,float)):         # isinstance(data,type)   检验数据类型
      raise TypeError('bad data type')
  if x > 0:
    return x
  else:
    return -x

# print(my_abs('qqq'))
print(my_abs(11))


def power(x,n=2):    # 参数默认值 n=2  函数参数：  必选参数在前，默认参数在后
  s = 1 
  while n>0:
    n= n-1 
    s= s*x
  return s
print(power(10))

def enroll(name, gender, age=6, city='Beijing'):
  print('name:', name)
  print('gender:', gender)
  print('age:', age)
  print('city:', city)

enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')       # 修改默认值 参数=value


def calc(*numbers):       # 可变参数  numbers 接收到是一个 tuple(元组)
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum

print(calc(1))
print(calc(1,2))
num = [12,3,4]
print(calc(*num))   #  list/tuple 加 * 即可

def person(name, age, **kw):          # **参数----关键字参数，自动组成一个dict
  print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')      # 类似可变参数接收 list/tuple  **dict   关键字参数

def person2(name, age, *, city, job):        # * 作为特殊的分隔符，后面的参数作为 命名关键字参数  city job 是 命名关键字参数   
  print(name, age, city, job)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
person2('Jack', 24, city='Beijing', job='Engineer')