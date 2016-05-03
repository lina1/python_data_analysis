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

s4.index = ["p1", "p2", "p3", "p4"]
print s4
