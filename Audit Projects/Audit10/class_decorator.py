def mydecorator(cls):
    old_method = cls.__init__

    def wrapper(*args, **kwargs):
        print(f"@mydecorator before {old_method.__name__}")
        if kwargs != {}:
            try:
                for val in kwargs.values():
                    if type(val) != int:
                        raise TypeError("Not int type")
            except ValueError as e:
                print(e)

        print(f"@mydecorator after {old_method.__name__}")
        return wrapper
    cls.__init__ = wrapper(cls.__init__)
    return cls



@mydecorator
class MyClass:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return str(self.args) + "and" + str(self.kwargs)

d = {"a": 1, "b": 2, "c": 3}
a = MyClass(d)
print(a)