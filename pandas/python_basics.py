#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2021/1/9 19:18
# @Author : Newport
# @Site : 
# @File : python_basics.py
# @Software: PyCharm

#1 列表推导式与条件赋值
#1.1 列表推导式与条件赋值¶
#列表表达式还支持多层嵌套，如下面的例子中第一个 for 为外层循环，第二个为内层循环：
print([m+'_'+n for m in ['a','b'] for n in ['c','d']])

#另一个实用的语法糖是带有 if 选择的条件赋值，其形式为 value = a if condition else b ：
value='cat' if 2>1 else 'dog'
print(value)

#1.2匿名函数与map方法
#匿名函数的方法简洁地表示：
my_func = lambda x: 2*x
print(my_func(3))

multi_para_func = lambda a, b: a + b
print(multi_para_func(1, 2))

#但上面的用法其实违背了“匿名”的含义，事实上它往往在无需多处调用的场合进行使用，例如上面列表推导式中的例子，用户不关心函数的名字，只关心这种映射的关系：
res=[(lambda x: 2*x)(i) for i in range(5)]
print(res)

#对于上述的这种列表推导式的匿名函数映射， Python 中提供了 map 函数来完成，它返回的是一个 map 对象，需要通过 list 转为列表：
res_map=list(map(lambda x: 2*x, range(5)))
print(res_map)

#对于多个输入值的函数映射，可以通过追加迭代对象实现：
res_mul=list(map(lambda x, y: str(x)+'_'+y, range(5), list('abcde')))
print(res_mul)

#1.3 zip对象与enumerate方法
#zip函数能够把多个可迭代对象打包成一个元组构成的可迭代对象，它返回了一个 zip 对象，通过 tuple, list 可以得到相应的打包结果：
L1, L2, L3 = list('abc'), list('def'), list('hij')
print(list(zip(L1, L2, L3)))
print(tuple(zip(L1, L2, L3)))

for i,j,k in zip(L1,L2,L3):
    print(i,j,k)

#enumerate 是一种特殊的打包，它可以在迭代时绑定迭代元素的遍历序号
L = list('abcd')
for index,value in enumerate(L):
    print(index,value)
#用 zip 对象也能够简单地实现这个功能：
for index,value in zip(range(len(L)),L):
    print(index,value)

#当需要对两个列表建立字典映射时，可以利用 zip 对象：
print(dict(zip(L1,L2)))

#既然有了压缩函数，那么 Python 也提供了 * 操作符和 zip 联合使用来进行解压操作：
zipped=list(zip(L1,L2,L3))
print(zipped)
print(list(zip(*zipped)))





