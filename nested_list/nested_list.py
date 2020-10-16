#!/usr/bin/env python3


#task 5 

''' Given the names and grades for each student in a class of
  students, store them in a nested list and print the name(s)
 of any student(s) having the second lowest grade.'''

#code :

if name == ' main ' :

#empty lists a and b
      a = []
      b = []

      print (' Enter the number of students ')
      for z in range(int(input())):
             print ('Enter the name and mark of student ')
             name = input()
             a.append(name)
             mark = float(input())
             b.append(score)
      p = max(b)
      q = min(b)
      for i in range(len(a)):
          if b[i]<p and b[i]>q:
              p=b[i]
      for j in range(len(a)):
          if b[j]==p:
            print (p[j])
# example code :
'''
if __name__ == '__main__':

    n = []
    s = []
    for _ in range(int(input())):
        name = input()
        n.append(name)
        score = float(input())
        s.append(score)
    a=max(s)
    b=min(s)
    for i in range(len(n)):
        if s[i]<a and s[i]>b:
            a=s[i]

    for j in range(len(n)):
        if s[j]==a:
            print(n[j])
'''
