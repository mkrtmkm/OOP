def instance_creation(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print(f"Створюється екземпляр класу: {cls.__name__}")
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

@instance_creation
class MyClass:
    def __init__(self):
        print("Конструктор MyClass")

obj = MyClass()
