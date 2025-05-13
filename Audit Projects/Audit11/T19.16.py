_max_instances = 1

class PoolMeta(type):
    _instances = {}
    _count = {}

    def __call__(cls, *args, **kwargs):
        if len(PoolMeta._instances) < _max_instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls].append(instance)
            cls._count[cls] += 1
            return instance
        else:
            idx = cls._count[cls] % cls._max_instances
            cls._count[cls] += 1
            instance = cls._instances[cls][idx]
            instance.__init__(*args, **kwargs)
            return instance


class Example(metaclass=PoolMeta, _max_instances=3):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Example(value={self.value})"

if __name__ == '__main__':
    t1 = Example("1")
    t2 = Example("2")
    t3 = Example("3")
    t4 = Example("4")
    t5 = Example("5")
    t6 = Example("6")
    t7 = Example("7")

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)
    print(t6)
    print(t7)