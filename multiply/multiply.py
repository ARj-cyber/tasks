#!/usr/bin/env python3


#task3

'''Write a small python program to take a few <space> seperated
 numbers as input and make the product of those numbers '''

# inputting the numbers
lst_no = input("Enter numbers seperated by a space  ")
lst =  lst_no .split()
# taking the product as 1
product = 1
for num in lst :
    product *= int(num)
#printing the answer
print(product)
