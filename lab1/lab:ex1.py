# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

input('Please enter customer name: ')
labor_hours = float(input('Please enter labor hours: '))
parts = float(input('Please enter cost of parts and supplies: '))

Labor_cost=labor_hours*35
Parts_cost=parts*(1+0.07)
Total_cost=Labor_cost+Parts_cost

print('Labor Cost: {0:.2f}'.format(Labor_cost))
print('Parts Cost: {0:.2f}'.format(Parts_cost))
print('Total Cost: {0:.2f}'.format(Total_cost))