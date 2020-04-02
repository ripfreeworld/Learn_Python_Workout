class MyClass:
    """A simple example class"""
    # https://docs.python.org/3/tutorial/classes.html
    i = 12345

    def f(self):
        return 'hello world'

sample = MyClass()
print(sample.f())


class Complex:
    # When a class defines an __init__() method, 
    # class instantiation automatically invokes __init__() 
    # for the newly-created class instance.
    def __init__(self, realpart, imagpart):
    # 在类中定义的函数有一点不同，第一个参数永远是实例变量self
        self.r = realpart
        self.i = imagpart

x = Complex(1, -1)
print(f"the realpart of 'x' is {x.r}")