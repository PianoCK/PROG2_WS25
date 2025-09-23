# decorator
def f1(func):
    def wrapper():
        print("--Start--")
        func()
        print("--Stop--")
    return wrapper

@f1 # Gleichbedeutend wie f = f1(f)
def f():
    print("Hallo")

f()