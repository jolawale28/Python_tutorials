# The scope of a variable is the region of its availability.
# Where in the code the variable can be accessed from

y = 100 # Global scope

def func():
    global x
    x = 300 # Global scope
    z = 500 # Function / Local Scope
    def myfunc():
        print(z)
    myfunc()
    print(x, y)

func()
print(x)

def func1():
    x = "Jane"
    def func2():
        nonlocal x
        x = "hello"
    func2()
    return x

print(func1())