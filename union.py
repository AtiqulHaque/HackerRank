
secA = int(input())
setA = list(input().split())

secB = int(input())
setB = list(input().split())

student = {}
for i in range(len(setA)):
    student[setA[i]] = setA[i]

for i in range(len(setB)):
    student[setB[i]] = setB[i]

print(len(student))
