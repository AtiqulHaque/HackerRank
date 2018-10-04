class MyClass:
    i = 123

    def __init__(self,real="ss",virtual="dfghj") :
        self.real = real
        self.virtual = virtual

    def f(self):
        return "Hello world" + self.virtual


obj = MyClass("HI","AGAIN")
print(obj.f());
