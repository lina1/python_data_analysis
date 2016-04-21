#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lina'
__date__ = '16/4/20'

import numpy as np

# 创建
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 7, 8, 9]])

print a
print b

print a.shape
print b.shape

b.shape = 4, 3
print b

b.shape = 2, -1
print b

c = a.reshape((2, 2))
print c
print a

a[1] = 200
print c
print a


d = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 7, 8, 9]], dtype=np.float16)
e = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 7, 8, 9]], dtype=np.complex)
print d
print e

# start end(not include) step
f = np.arange(0, 1, 0.1)
print f

# start end(which is determined by endpoint, default include), count
g = np.linspace(0, 1, 12)
print g

# 创建从10^0到10^2的20个等比数列
h = np.logspace(0, 2, 20)
print h

s = "abcdefgh"

# ASCII
print np.fromstring(s, dtype=np.int8)

print np.fromstring(s, dtype=np.int16)

print np.fromstring(s, dtype=np.float)


def func(i):
    return i % 4 + 1

print np.fromfunction(func, (10,))


def func2(i, j):
    return (i + 1) * (j + 1)

print np.fromfunction(func2, (9, 9))

# 存取元素

# First: 下标
a = np.arange(10)

print a[5]
print a[2:4]
print a[:5]
print a[:-1]
a[2:4] = 100, 101
print a
print a[::-1]

# b和a共享一块数据空间
b = a[3:7]
b[2] = -10
print b
print a


# Second: 整数序列
x = np.arange(10, 1, -1)
print x

b = x[np.array([3, 3, -3, 8])]
print b

# b和x不共享数据空间
b[2] = 100
print b
print x

x[[1, 2, 3]] = -1, -2, -3
print x


# Third: 布尔数组
x = np.arange(5, 0, -1)
print x

print x[np.array([True, False, True, False, False])]

# x[np.array([True, False, True])] = -1, -2, -3
# print x

x = np.random.rand(10)
print x
print x[x > 0.5]


# 多维数组
a = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
print a
print a[0, 3:5]
print a[4:, 4:]
print a[:, 2]
print a[2::2, ::2]


print a[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
print a[3:, (0, 2, 5)]

mask = np.array([1, 0, 0, 1, 0, 0], dtype=np.bool)
print a[mask, 2]

persontype = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S32', 'i', 'f']
})

a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)], dtype=persontype)
print a
print a.dtype

c = a[1]
c["name"] = "Li"
print a[1]["name"]




