# file one.py
def func():
    print("func() in one.py")
    print("top-level in one.py")

if __name__ == "__main__":
    def anotherFun():
        print ("Another funtion")
    print("one.py is being run directly")
    anotherFun()
