
secA = int(input())
setA = list(input().split())

secB = int(input())
setB = list(input().split())

student = {}
for i in range(len(setA)):
    if(student[setA[i]]):
        student[setA[i]] = student[setA[i]] + 1
    else:
        student[setA[i]] = 1

for i in range(len(setB)):
    if(student[setB[i]]):
        student[setB[i]] = student[setB[i]] + 1
    else:
        student[setA[i]] = 1

count = 0

print(student)

for i in range(len(student)):
    if(student[i] == 1):
        count += 1

print(count)
