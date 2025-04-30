class MyClass:

    def __init__(self, value):
        self.value = value

    def print(self):
        print(self.value)

ob = MyClass(10)
print(dir(ob))

print(hasattr(MyClass, "print"))

if hasattr(MyClass, "print"):
    method = getattr(ob, "print")
    method()

if hasattr(MyClass, "print"):
    delattr(MyClass, "print")
    print(dir(ob))

def __str__(self):
    return "Some text"

setattr(MyClass, "__str__", __str__)
print(ob)