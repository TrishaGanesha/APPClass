#function
#Positional arguments
#when you call a function, the values you pass to the function are called arguments. The order in which you pass the arguments matters. These are called positional arguments.
#Positional only arguments=you can specify that some parameters must be specified positionally. This is done by placing a / in the function definition. All parameters before the / must be specified positionally.
#example 
"""function arguments types default arguments, keyword arguments, variable-length arguments, positional-only arguments, and keyword-only arguments."""
def greet(name, /):
    print(f"Hello, {name}!")
c=greet("Alice")  # Valid
#Function with positional arguments
def func(a,b):
    if b!=0:
        return a/b
    else:
        return "Error: Division by zero"
c=func(10,2)
print(c) 
d=func(10,0)
print(d)  
#variable-length arguments=when no fixed number of arguments are specified, the function can accept any number of arguments. These are called variable-length arguments. In Python, you can use *args for variable-length positional arguments and **kwargs for variable-length keyword arguments.
#example
def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
l=[2,3,4,5,6]
print(calculate_sum(*l))  
print(calculate_sum(1, 2, 3, 4, 5))

#to add the incoming strings
def concatenate_strings(*args):
    result = ""
    for string in args:
        result += string
    return result
str1=["Hello", " ", "World", "!"]
v=concatenate_strings(*str1)
print(v)  # Output: Hello World!

#keyword arguments=when you call a function, you can specify the values of the parameters by using their names. These are called keyword arguments. The order in which you specify the keyword arguments does not matter.
#example
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")   

greet(name="Alice", age=30)  # Valid
greet(age=25, name="Bob")     # Valid (order doesn't matter)
#variable-length keyword arguments=when no fixed number of keyword arguments are specified, the function can accept any number of keyword arguments. These are called variable-length keyword arguments. In Python, you can use **kwargs for variable-length keyword arguments.
#example
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")  # Valid