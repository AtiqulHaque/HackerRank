
def bubleSort(l):
    for j in range(len(l)):
        for i in range(len(l)):
            if i+1 < len(l):
                if l[i] > l[i+1]:
                    temp = l[i+1]
                    l[i+1] = l[i]
                    l[i] = temp
    return l;

n = int(input())
arr = list(map(int, input().split()))
out = {}
for i in range(len(arr)):
    out[arr[i]] = arr[i]

result = bubleSort(list(out.keys()))
print(result[len(result) - 2])
