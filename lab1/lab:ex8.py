#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""
year = int(input('Enter year: '))

if year // 4 == 0:
    print('{0} is a leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))
