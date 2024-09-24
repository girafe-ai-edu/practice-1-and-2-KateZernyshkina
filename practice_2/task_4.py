# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
print('Hello! Please, enter an integer 4-digit number.')
a = int(input())
print(a // 1000, '+', a // 100 % 10, '+', a // 10 % 10, '+', a % 10, '=', a // 1000 + a % 10 + a // 10 % 10 + a // 100 % 10)
