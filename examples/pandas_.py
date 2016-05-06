#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lina'
__date__ = '16/4/29'

from pandas import Series, DataFrame
import pandas as pd

s = Series([100, "python", "go", "lua"])
print s
print s.values
print s.index

s2 = Series([100, "python", "scu", "lina"], index=["mark", "title", "university", "name"])
print s2
print s2.index
print s2["name"]

sd = {"python": 10000, "go": 8900, "lua": 7200}
s3 = Series(sd)
print s3

s4 = Series(sd, index=["python", "go", "java"])
print s4

print pd.isnull(s4)
print s4.isnull()

s4.index = ["p1", "p2", "p3"]
print s4


data = {"name": ["yahoo", "facebook", "google"], "marks": [200, 400, 800], "price": [9, 3, 7]}
f1 = DataFrame(data)
print f1

f2 = DataFrame(data, columns=["name", "marks", "price"])
print f2

f3 = DataFrame(data, columns=["name", "marks", "price", "debt"], index=["a", "b", "c"])
print f3

new_data = {"lang": {"firstline": "python", "secondline": "go"}, "price": {"firstline": 8000}}
f4 = DataFrame(new_data)
print f4

f3["debt"] = 89.2
print f3

sdebt = Series([2.2, 3.3], index=["a", "c"])
f3["debt"] = sdebt
print f3

# there is a warning
# f3["price"]["a"] = 5
# print f3


