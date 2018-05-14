#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python str(字符串)在内存是以Unicode表示,如果要在网络上传输或者保存在磁盘需要str转为以字节单位的bytes
#区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
# ord()---获取字符的整数表示
print( ord('A') )
print( ord('a') )
print( ord('中') )

# chr()---将编码转为字符
print( chr(97) )
print( chr(66) )

# .encode():str转为对应编码的bytes
print( '中文'.encode('utf-8') ) 
# .decode():将bytes转为对应编码的str
print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') )
# len():计算字符/字节数