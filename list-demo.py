# -*- coding: utf-8 -*-
# list: 一种有序的集合，可随时添加/删除其中元素
classmates = ['xiaoming','xiaohong','xiaoqiang']
print(classmates)
# len(list): 获取list的长度
print( len(classmates))
# 访问方式,下标索引,从0(-1)开始
print( classmates[0] )  
print( classmates[-3] )
# 添加:list.insert(index,element) / list.append(element)
classmates.append('xiaoli')
classmates.insert(1,'meimei')
print( classmates )
# 删除: list.pop([index]),默认删除尾部
classmates.pop()
classmates.pop(1)
print( classmates )
# tuple: 元组，一种不可变的list
nochange = (1,3)
print( nochange )