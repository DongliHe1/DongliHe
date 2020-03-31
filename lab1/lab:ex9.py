#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

time = int(input('Enter military time: '))
time1 = time // 100
time2 = time % 100

if time1>12:
    time1=time1-12
    print('{0}:{1}pm'.format(time1,time2))
else:
    time1=time1
    print('{0}:{1}am'.format(time1,time2))