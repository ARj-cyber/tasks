no = int(input())
marksh=[[input(),float(input())] for _ in range(0,no)]
marksh.sort(key = lambda x: (x[1],x[0]))
names = [i[0] for i in marksh]
marks = [i[1] for i in marksh]

m_score = min(marks)

while marks[0] == m_score:
    marks.remove(marks[0])
    names.remove(names[0])

for x in range(0,len(marks)):
	 if marks[x] == min(marks):
        	print(names[x])
