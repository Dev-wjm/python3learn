# -*- coding: utf-8 -*- 
# set: 存 key 的集合，不重复
s = set([1,3,9])    # 初始化   set(list)
print(s)
s.add(4)      # 添加
print(s)
s.remove(1)     # 删除
print(s)


# set 数学操作
s1 = set([1, 2, 3])
s2 = set([4, 2, 3])

print(s1 & s2)      # set & set 求交集
print(s1 | s2)      # set | set 求并集