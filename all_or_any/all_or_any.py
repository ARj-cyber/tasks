#!/usr/bin/env python3


#task 4

'''You are given a space separated list of integers. 
If all the integers are positive, 
then you need to check if any integer is a palindromic integer.'''

# take input
x = input("Enter how much numbers do you have \n [+] ")
nums = input("Enter the  numbers , seperated by spaces \n [+]  ").split()

#checking
a = all(map(lambda x:int(x)>-1,nums))
b = any(map(lambda x:x==x[::-1],nums))
#output
print (" [+] ",a and b)
