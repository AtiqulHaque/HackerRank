if __name__ == "__main__":
    for _ in range(int(input())):
        noC = int(input())
        cLengths = list(map(int,input().split()))
        for i in range(int(len(cLengths)/2)):
            print(cLengths[i] , cLengths[(len(cLengths) - 1)  - i])
