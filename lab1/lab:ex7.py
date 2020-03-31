#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

v = int(input('Enter initial velocity(fps): '))
h = int(input('Enter initial height(feet): '))

height= v*3 + h - 16*3*3

print('The height after 3 seconds is: {0:.1f} ft'.format(height))
