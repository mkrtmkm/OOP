class ProtectedDictError(KeyError):
    NOT_INTEGER_KEY = 0
    MISSED_KEY = 1
    CHANGE_VALUE = 2

    def __init__(self, err_code, message):
        super().__init__()
        self.err_code = err_code
        self.message = message

    def __str__(self):
        return f'{self.err_code}: {self.message}'

class ProtectedDictInt:

    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise ProtectedDictError(ProtectedDictError.NOT_INTEGER_KEY, "Not an integer")
        if key in self.data:
            raise ProtectedDictError(ProtectedDictError.CHANGE_VALUE, "Change value")
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __contains__(self, key):
        return key in self.data

    def __add__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            key, value = other
            if not isinstance(key, int):
                raise ProtectedDictError(ProtectedDictError.NOT_INTEGER_KEY, "Not an integer")
            if key in self.data:
                raise ProtectedDictError(ProtectedDictError.CHANGE_VALUE, "Change value")
            new_dict = ProtectedDictInt()
            new_dict.data = self.data.copy()
            new_dict.data[key] = value
            return new_dict
        elif isinstance(other, ProtectedDictInt):
            for key in other.data:
                if key in self.data:
                    ProtectedDictError(ProtectedDictError.CHANGE_VALUE, "Change value")
            new_dict = ProtectedDictInt()
            new_dict.data = {**self.data, **other.data}
            return new_dict
        else:
            raise TypeError('Cannot add {} to {}'.format(type(other), type(self)))

    def __sub__(self, key):
        if key not in self.data:
            if not isinstance(key, int):
                raise ProtectedDictError(ProtectedDictError.NOT_INTEGER_KEY, "Not an integer")
            raise ProtectedDictError(ProtectedDictError.MISSED_KEY, "Missed key")
        new_dict = ProtectedDictInt()
        new_dict.data = {k: v for k, v in self.data.items() if k != key}
        return new_dict

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __call__(self):
        return sum(self.data.keys())


pd = ProtectedDictInt()
pd[2] = "two"
pd[1] = "one"

pd = pd + (3, "three")
print(pd)

pd = pd - 2
print(pd)

print(1 in pd)
print(4 in pd)

print(len(pd))

print(pd())