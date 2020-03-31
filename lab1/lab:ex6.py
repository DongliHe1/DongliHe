#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

time1 = int(input('Enter time 1 hours: '))
time2 = int(input('Enter time 1 minutes: '))
time3 = int(input('Enter time 2 hours: '))
time4 = int(input('Enter time 2 minutes: '))

time5= time1 + time3
time6= time2 + time4

if time6>60:
    time7= time6 // 60
    time8= time6 % 60
    time9= time5 + time7

print('Total time is {0}:{1}'.format(time9, time8))