#inheritence
class Parent:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show_info(self):
        super().show_info()
        print(f"Age: {self.age}")

# Creating an instance of the Child class
child = Child("Alice", 10)
child.show_info()

#polymorphism
#run time polymorphism = method overloading and method overriding
#complie time polymorphism = operator overloading and function overloading but python does not support function overloading and operator overloading because python is dynamically typed language and it does not support method overloading and operator overloading but we can achieve polymorphism in python using duck typing and method overriding
#example of method overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")   
#duplication of same method name in different classes so we must avoid duplication

# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the sound method (polymorphism)
animal.sound()  # Output: Animal makes a sound
dog.sound()     # Output: Dog barks
cat.sound()     # Output: Cat meows 
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(self.make, self.model)
    def move(self):
        print("Car is moving")
class Boat:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(self.make, self.model)
    def move(self):
        print("Boat is moving")
class Plane:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(self.make, self.model)
    def move(self):
        print("Plane is moving")

car1=Car("Toyota","Camry")
boat1=Boat("Yamaha","242X")
plane1=Plane("Boeing","747")
for vehicle in (car1, boat1, plane1):
    vehicle.move()  # Output: Car is moving, Boat is moving, Plane is moving
#here still duplication of same method name in different classes so we must avoid duplication
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(self.make, self.model)
    def move(self):
        pass  # Abstract method
class Car(Vehicle):
    def move(self):
        print("Car is moving")
class Boat(Vehicle):
    def move(self):
        print("Boat is moving")
class Plane(Vehicle):
    def move(self):
        print("Plane is moving")
car1=Car("Toyota","Camry")
boat1=Boat("Yamaha","242X")
plane1=Plane("Boeing","747")
for vehicle in (car1, boat1, plane1):
    vehicle.move()  # Output: Car is moving, Boat is moving, Plane is moving    

#using inheritance we can avoid duplication of same method name in different classes 
#how to completely inherit a complete class in python using inheritance using derived class and base class using super() method
# example of complete inheritance of a complete class in python using inheritance using derived class and base class
class Base:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")
class Derived(Base):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show_info(self):
        super().show_info()
        print(f"Age: {self.age}")
#example of accessing the base class methods and attributes in the derived class without super() method which throws an error because the base class methods and attributes are not accessible in the derived class without super() method
class Base:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")
class Derived(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)  # Accessing the base class constructor without super(),error because the base class constructor is not accessible in the derived class without super() method
        self.age = age

    def show_info(self):
        Base.show_info(self)  # Accessing the base class method without super()
        print(f"Age: {self.age}")
x=Derived("Alice", 10)
x.show_info()  # Output: Name: Alice, Age: 10
#----overriding the base class methods in the derived class using super() method-----------





#operator overloading in python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
#magic methods init and str are used to overload the + operator and print the point object respectively
#diff magic methods and normal methods in python
# Magic methods are special methods in Python that have double underscores at the beginning and end of their names (e.g., __init__, __str__). They are automatically called by the Python interpreter in response to specific operations on objects of a class. Normal methods are regular methods defined in a class that are called explicitly by the programmer.
#magic methods are also called dunder methods (double underscore methods) and they are used to implement operator overloading, object representation, and other special behaviors in Python classes. Normal methods are used to define the behavior of objects and can be called directly by the programmer.
#operator overloading allows a user-defined class to give special meaning to operators such as +,-,*,==,<,>,etc
#arthematic operators
# '+'  __add__()
# '-' __sub__()
# '*' __mul__()
# /  __truediv()__
# //
# %
# **
# @
# -obj
# +obj
# abs(obj)

#suppose a financial system has two investment accounts
#adding two account objects should produce combine object
#single class operator overloading
class investment:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
    def __add__(self,other): #self will assign to left ,other to assign right
        return self.balance+other.balance
a1=investment('oi',75000)
a2=investment('oii',80000)
total=a1+a2
print("Combined Investment:",total)


#multiple class
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print()
class bonusmarks:




#magic method __lt__(less than) one example of vectors,__str__ to print the object

##questions class overriding ,method overriding,operator overloading


#inheritance 5type
#single inheritance ,object must be created for child class ,and access parent using child class
#multilevel inheritance=one parent class,derived class is derived class from parent class which will be a derived class of other class
#multiple =one child has multiple parent class
#hybrid combinations
#hierarchical one parent multiple children class