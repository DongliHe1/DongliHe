#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
c = int(input('Enter value for c: '))

judge = b*b - 4*a*c
solu1 = (judge**(1/2)-b) / (2*a)
solu2 = (-judge**(1/2)-b) / (2*a)

if judge>0:
    print('Solution:{0},{1}'.format(solu1,solu2))
elif judge==0:
    print('Solution:{0}'.format(solu1))
else:
    print('No solutions.')
    