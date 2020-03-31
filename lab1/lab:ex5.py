#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

num1 = int(input('Enter beginning odometer: '))
num2 = int(input('Enter ending odometer: '))
gallons = int(input('Enter gallons: '))

final = (num2 - num1) / gallons

print('Fuel Efficiency: {0:.1f} miles per gallon'.format(final))
