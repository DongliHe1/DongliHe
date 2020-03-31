#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

cycling = int(input('Enter cycling: '))
running = int(input('Enter running: '))
swimming = int(input('Enter swimming: '))


total_col = cycling * 200 + running * 475 + swimming * 275
total_pounds = total_col / 3500


print('Total pounds lost: {0:.1f}'.format(total_pounds))
