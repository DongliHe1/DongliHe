#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

miles = int(input('Enter miles: '))
yards = int(input('Enter yards: '))
feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

total_inches = miles * 63360 + yards * 36 + feet * 12 +inches
total_centimeters = total_inches / 0.3937


kilometers = total_centimeters // 100000
total_centimeters = total_centimeters % 100000

meters = total_centimeters // 100
total_centimeters = total_centimeters % 100

centimeters = total_centimeters / 1
print('The metric length is: ')
print('kilometers: {0}'.format(kilometers))
print('meters: {0}'.format(meters))
print('centimeters: {0:.1f}'.format(centimeters))