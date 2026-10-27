def hello(a, b):
    print("Hello, World!")
    print(a * b)

hello(2, 4)


def hi(a, b):
    pass

hi(2, 4)


# /Functions 
# 1)Builtin Functions: These are functions that are already defined in Python and can be used directly. Examples include print(), len(), type(), etc.
# 2)User-Defined Functions: These are functions that you create yourself to perform specific tasks. You can define a function using the def keyword, followed by the function name and parentheses. Inside the parentheses, you can specify parameters that the function can accept. The function body is indented below the function definition.

def hello(a=90, b=67):
    print(a * b)

hello(29, 4)

def trop(a=90, b=67):
    print(a * b)

trop(29)

# /Arbitrary Arguments
# Sometimes, you may want to create a function that can accept a variable number of arguments.

def average(*Args):
    sum = 0
    for i in Args:
        sum += i
    print(sum / len(Args))
average(2, 4, 6, 8)


# Keyword Arbitrary Arguments:-
# ==============================
# If you want to handle named arguments that you have not defined in advance, you can use **kwargs in the function definition. This allows you to pass a variable number of keyword arguments to the function.
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
person_info(name="Alice", age=30, city="New York")