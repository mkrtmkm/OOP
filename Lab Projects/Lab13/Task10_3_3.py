def function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається функція/метод: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

#Приклад використання
@function_name
def my_func():
    print("Hello World")

my_func()