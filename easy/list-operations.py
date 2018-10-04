if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        command, *params = input().split()


        def insert(params):
            l.insert(int(params[0]), int(params[1]))

        def printList(params):
            print(l)

        def removeItem(params):
            l.remove(int(params[0]))

        def appendItem(params):
            l.append(int(params[0]))

        def sortItem(params):
            l.sort()

        def popItem(params):
            l.pop()

        def reverseItem(params):
            l.reverse()


        def getCommand(command,params):
            switcher = {
                'insert'    : insert,
                'print'     : printList,
                'append'    : appendItem,
                'sort'      : sortItem,
                'pop'       : popItem,
                'reverse'   : reverseItem,
                'remove'    : removeItem
            }
            fun = switcher.get(command)
            fun(params)

        getCommand(command, params)
