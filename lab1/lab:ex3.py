#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

annual_deposit = int(input('Enter annual deposit: '))
rate = int(input('Enter rate: ')) 

balance = annual_deposit * (1+(rate/100))**3 + annual_deposit * (1+(rate/100))**2 + annual_deposit * (1+(rate/100))

print('After 3 years, balance is: ${0:.2f}'.format(balance))
