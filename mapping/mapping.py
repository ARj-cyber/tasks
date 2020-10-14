#!/usr/bin/env python3


#task 2
# Write a small python program to take a few numbers as input and make them print as a list


#taking input
nums = int ( input ("Enter the numbers of elements  \t") )
# adding a empty list
nums_lst = []
#itering till range
for i in range (0, nums):
     nums1 = int(input("Enter the number \t"))
#adding the element
     nums_lst.append(nums1)
#printing the output
print (nums_lst)

