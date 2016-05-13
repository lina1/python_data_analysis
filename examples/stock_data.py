#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'lina'
__date__ = '16/5/6'

import pandas
from pandas_datareader import data, wb
import matplotlib.pyplot as plt

sym = "BABA"

finace = data.DataReader(sym, "yahoo", start="2014/11/11")
# print finace.tail(3)
plt.plot(finace.index, finace["Open"])

plt.show()

