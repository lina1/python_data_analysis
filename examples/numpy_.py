#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lina'
__date__ = '16/4/20'

import numpy as np
import time
import math

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

# ufunc运算, 能对数组的每个元素进行操作

# 计算后x的值没有变
x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)
print x
print y


# 将被覆盖的数组作为第二个参数传给ufunc, 计算后x的值会改变
t = np.sin(x, x)
print x
print t
print id(x) == id(t)

# numpy.math 和 python标准库math.sin计算速度

x = [i * 0.001 for i in xrange(1000000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = math.sin(t)

print "math.sin:", time.clock() - start

x = [i * 0.001 for i in xrange(1000000)]
x = np.array(x)
start = time.clock()
np.sin(x, x)
print "numpy.sin: ", time.clock() - start

# 对单个值进行计算
x = [i * 0.001 for i in xrange(1000000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = np.sin(t)
print "numpy.sin loop: ", time.clock() - start


def triangle_wave(x, c, c0, hc):

    x -= int(x)
    if x >= c:
        r = 0.0

    elif x < c0:
        r = x / c0 * hc

    else:
        r = (c - x) / (c - c0) * hc

    return r

x = np.linspace(0, 2, 1000)
y = np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in x])
print y


triangle_ufunc = np.frompyfunc(lambda x: triangle_wave(x, 0.6, 0.4, 1.0), 1, 1)
y2 = triangle_ufunc(x)
print y2

def triangle_wave_2(c, c0, hc):

    def triangle_func(x):

        x -= int(x)
        if x >= c:
            r = 0.0

        elif x < c0:
            r = x / c0 * hc

        else:
            r = (c - x) / (c - c0) * hc

        return r

    return np.frompyfunc(triangle_func, 1, 1)

y3 = triangle_wave_2(0.6, 0.4, 1.0)(x)
print y3


a = np.arange(0, 60, 10).reshape(-1, 1)
print a
print a.shape

b = np.arange(0, 5)
print b
print b.shape

c = a + b
print c
print c.shape

x, y = np.ogrid[0:5, 0:5]
print x
print y

x, y = np.ogrid[0:1:4j, 0:1:3j]
print x
print y


from mayavi import mlab
# from enthought.mayavi import mlab

x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp(- x ** 2 - y ** 2)

pl = mlab.surf(x, y, z, warp_scale="auto")
mlab.axes(xlabel='x', ylabel='y', zlabel='z')
mlab.outline(pl)

