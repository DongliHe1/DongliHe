#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

cloud = int(input('Enter percentage cloud cover: '))

if cloud>0 and cloud<30:
    print('clear')
elif cloud>31 and cloud<70:
    print('pratly cloudy')
elif cloud>71 and cloud<99:
    print('mostly cloudy')
else: 
    print('overcast')
    
        
