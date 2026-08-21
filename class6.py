#students details using keyword arguments
"""def student_details(name,age,course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
student_details(name="John", age=20, course="Computer Science")  # Valid
print("\n")
student_details(course="Mathematics", name="Alice", age=22)  

#variable length Keyword argument
def student_details(**details):
    for key,value in details.items():
        print(key,":",value)
student_details(name='Rahul',age=21,course="MCA",semester=2)

#students details using both *args and **kwargs
def student(*subjects,**details):
    print("Subject:")
    for subject in subjects:
        print("-",subject)
    print("\nStudent Details:")
    for key,value in details.items():
        print(key,":",value)
student("Python","Sql","CV",name="Rahul",semester=2)

#Return Values
#when a function reaches a return statement,it stops executing and sends the result
#Return multiple values
#return multiple values
#DIFF between print() and return()
def add_return(a,b):
    return a+b
def add_print(a,b):
    print(a+b)
add_print(100,30)
print((add_return(20,30)))
result=add_print(30,20)
print(result)
#Returning multiple values
#dynamic insertion of marks with given number of input of n"""
def result(*marks):
    total=sum(marks)
    percentage=total/len(marks)
    return total,percentage
total,percentage=result(85,43,78,99)
print("Total",total)
print("Percentage",percentage)

#Scope of variable 
#local and global variable example
#global keyword in fornt of a variable name ,when used inside in function ,then also it will be global but not local

balance=1000
def deposit(amount):
    global balance
    balance+=amount
deposit(500)
print("Balance=",balance)

#RECURSION
#factorail of a number using recursive
def factorial(n):
    if n==0 or n== 1:
        return 1
    else:
        return n*factorial(n-1)
value=factorial(8)
print(value)

