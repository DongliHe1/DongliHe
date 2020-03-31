#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

hours = int(input('Enter the number of hours worked: '))
wage = int(input('Enter the hourly wage: '))

if hours>40:
    total=40*wage + (hours-40)*wage*(1+0.5)
    print("Gross pay is ${0:.2f}".format(total))
else:
    total = hours * wage
    print("Gross pay is ${0:.2f}".format(total))