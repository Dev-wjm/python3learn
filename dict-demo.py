# -*- coding: utf-8 -*- 
# dict: key-value(map)数据类型,支持快速的查找
dict01 = {'xiaoming':90,'xiaohong':100}   # 初始化
print( dict01['xiaoming'] )         # 获取 
dict01['xiaoqiang'] = 89   # 添加
print( dict01['xiaoqiang'] )
print( 'xiaoqiang' in dict01)         # 判断 key 是否存在 dict 中   key in dict  True/ False
# dict[key] 如果 key 不存在会报错; dict.get(key[,errValue]): 如果 dict 中 key 不存在 则返回 None 或者 errValue
# print( dict01['xxxxxx'] )
print(dict01.get('xxxxx'))
print(dict01.get('xxxxx','errValue'))
print(dict01.pop('xiaoqiang'))      # pop(key) 删除
