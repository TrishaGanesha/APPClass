{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df52951c-0874-46cf-bfe1-65b591e8cc97",
   "metadata": {},
   "outputs": [],
   "source": [
    "Object-Oriented Programming (OOP) is a programming approach where a program is designed using objects that contain:\n",
    "\n",
    "Data → attributes/variables\n",
    "Behavior → methods/functions\n",
    "\n",
    "For instance, in a college management system:\n",
    "Student\n",
    " ├── Data\n",
    " │    ├── name\n",
    " │    ├── roll_no\n",
    " │    └── marks\n",
    " │\n",
    " └── Behavior\n",
    "      ├── display_details()\n",
    "      └── calculate_grade()\n",
    "\n",
    "The Core Building Blocks\n",
    "- Classes\n",
    "- Objects\n",
    "- Constructors\n",
    "- Instance Variables\n",
    "- Methods\n",
    "\n",
    "The Pillars of OOP\n",
    "- Encapsulation\n",
    "- Inheritance\n",
    "- Polymorphism\n",
    "\n",
    "Dynamic & Static Behaviors\n",
    "- Method Overriding\n",
    "- Class Methods\n",
    "- Static Methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "610f14d0-5dfd-4250-8b89-2fca7b6aeafa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lamp brand: Philips\n",
      "Lamp pawer rating:  12\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "- 1. CLASS: A class is a blueprint, template, or prototype used to define the structure of an object.\n",
    "- 2. OBJECT: An object is an instance of a class.\n",
    "'''    \n",
    "\n",
    "# A smart-home application controls different lamps. Every lamp has a brand and power rating.\n",
    "class SmartLamp:\n",
    "    brand = \"Philips\"  # variable/ attribute\n",
    "    power = 12\n",
    "\n",
    "lamp1 = SmartLamp()    # lamp1 - object\n",
    "\n",
    "print(\"Lamp brand: \" + lamp1.brand)\n",
    "print(\"Lamp pawer rating: \", lamp1.power)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8fb2d394-662c-4a5a-81a2-77dc474acd68",
   "metadata": {},
   "outputs": [],
   "source": [
    "1. Create a Printer class and create three printer objects holding the details of printers \n",
    "such as print capacity, color/mono tone, type of printer:\n",
    "\n",
    "printer1\n",
    "printer2\n",
    "printer3\n",
    "\n",
    "Display their object identities."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0217117c-3615-451d-b3e0-cb4aa1f2cc19",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arun\n",
      "MCA\n",
      "20\n",
      "Roopa is pursuing BCA, and his age is 18\n",
      "Arun is pursuing MCA, and his age is 20\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "CONSTRUCTOR: A special method automatically invoked when a new object is created. \n",
    "Its primary purpose is to initialize the object's variables and set up its initial state.\n",
    "\n",
    "TYPES: \n",
    "- Default constructor\n",
    "- Non-parameterized Constructor\n",
    "- Parameterized Constructor\n",
    "'''\n",
    "\n",
    "# default constructor\n",
    "\n",
    "class EmptyClass:\n",
    "    name = \"Arun\"\n",
    "    course = \"MCA\"\n",
    "    age = 20\n",
    "    \n",
    "    @staticmethod   # A static method performs an operation that does not require object or class data.\n",
    "    def funMethod(): # method without any parameter\n",
    "        print(\"Roopa is pursuing BCA, and his age is 18\")\n",
    "\n",
    "    def funMethods(self):  # Non-parameterized method\n",
    "        print(f\"{self.name} is pursuing {self.course}, and his age is {self.age}\")\n",
    "\n",
    "# Python uses a default constructor to create the object\n",
    "obj = EmptyClass() \n",
    "print(obj.name)\n",
    "print(obj.course)\n",
    "print(obj.age)\n",
    "obj.funMethod()\n",
    "obj.funMethods()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "862501be-ee7b-418b-b332-eef4fa9c201a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dogs are loyal animals.\n",
      "There are many dogs of class <class '__main__.Dog'>\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Static Methods\n",
    "Methods that are completely independent of both the class and individual objects. \n",
    "They behave like regular utility functions but are visually nested inside \n",
    "the class namespace for logical grouping. \n",
    "They cannot access instance or class variables directly.\n",
    "'''\n",
    "\n",
    "class Dog:\n",
    "    @staticmethod\n",
    "    def info():\n",
    "        print(\"Dogs are loyal animals.\")\n",
    "\n",
    "    @classmethod\n",
    "    def count(cls):\n",
    "        print(\"There are many dogs of class\", cls)\n",
    "\n",
    "Dog.info()  # Static method call\n",
    "Dog.count()  # Class method call"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c6f0ca3f-1240-4f0d-b724-325cd3113f01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n",
      "60\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Class Methods\n",
    "A class method is useful when the information belongs to the class as a whole.\n",
    "\n",
    "Methods that are bound to the class itself rather than an individual object. \n",
    "They can access and modify class-level variables (variables shared by all instances) \n",
    "and accept the class type as their first parameter.\n",
    "'''\n",
    "\n",
    "class Ride:\n",
    "    base_fare = 50\n",
    "\n",
    "    @classmethod\n",
    "    def change_base_fare(cls, new_fare):\n",
    "        cls.base_fare = new_fare\n",
    "\n",
    "print(Ride.base_fare)\n",
    "Ride.change_base_fare(60)\n",
    "print(Ride.base_fare)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ddc18284-e872-4509-a759-a232019cb483",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Robot name: Generic Bot\n",
      "Robot battery life:  100\n"
     ]
    }
   ],
   "source": [
    "# Non-parameterized Constructor\n",
    "\n",
    "# self — self represents the current object.\n",
    "\n",
    "class Robot:\n",
    "    def __init__(self):    # Default constructor: takes no extra arguments\n",
    "        self.name = \"Generic Bot\"\n",
    "        self.battery = 100\n",
    "\n",
    "# Creating an object without passing any data\n",
    "my_robot = Robot()\n",
    "print(\"Robot name: \" + my_robot.name)  \n",
    "print(\"Robot battery life: \", my_robot.battery)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f3c73ae6-92d0-4eab-9723-f2cc519621b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Samsung S24\n",
      "Apple iPhone 16\n"
     ]
    }
   ],
   "source": [
    "# Parameterized Constructor\n",
    "\n",
    "class Mobile:\n",
    "\n",
    "    def __init__(self, brand, model):\n",
    "        self.brand = brand\n",
    "        self.model = model\n",
    "\n",
    "phone1 = Mobile(\"Samsung\", \"S24\")\n",
    "phone2 = Mobile(\"Apple\", \"iPhone 16\")\n",
    "\n",
    "print(phone1.brand, phone1.model)\n",
    "print(phone2.brand, phone2.model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "642536be-277d-438a-a61a-8080e9119560",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Customer Name: Anita\n",
      "Food order: Pizza\n",
      "Quantity:  1\n",
      "Customer Name: Bharath\n",
      "Food order: Dosa\n",
      "Quantity:  2\n"
     ]
    }
   ],
   "source": [
    "# An online food-delivery application \n",
    "# creates an order using customer name, food item, and quantity.\n",
    "\n",
    "class FoodOrder:\n",
    "    def __init__(self, customer, item, quantity):   # Parameterized constructor\n",
    "        self.customer = customer\n",
    "        self.item = item\n",
    "        self.quantity = quantity\n",
    "\n",
    "order1 = FoodOrder(\"Anita\", \"Pizza\", 1)   # FoodOrder() is the constructor\n",
    "order2 = FoodOrder(\"Bharath\", \"Dosa\", 2)  # order1 and order2 - multiple objects\n",
    "\n",
    "print(\"Customer Name: \" + order1.customer)\n",
    "print(\"Food order: \" + order1.item)\n",
    "print(\"Quantity: \", order1.quantity)\n",
    "\n",
    "print(\"Customer Name: \" + order2.customer)\n",
    "print(\"Food order: \" + order2.item)\n",
    "print(\"Quantity: \", order2.quantity)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1673a6a5-7f68-4bcd-aab7-cd5e18c0e529",
   "metadata": {},
   "outputs": [],
   "source": [
    "2. Create a MovieTicket class with a constructor accepting:\n",
    "\n",
    "movie_name\n",
    "theatre\n",
    "seat_number\n",
    "\n",
    "Create three ticket objects."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "feb8e63b-71a2-4b53-8aeb-75edefacc377",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Archer 100 5\n",
      "Warrior 150 8\n"
     ]
    }
   ],
   "source": [
    "# Instance Variables — Instance variables store data that is different for each object.\n",
    "\n",
    "# Scenario: A game contains multiple characters.\n",
    "class GameCharacter:\n",
    "    def __init__(self, name, health, level):\n",
    "        self.name = name\n",
    "        self.health = health\n",
    "        self.level = level\n",
    "\n",
    "player1 = GameCharacter(\"Archer\", 100, 5)\n",
    "player2 = GameCharacter(\"Warrior\", 150, 8)\n",
    "\n",
    "print(player1.name, player1.health, player1.level)\n",
    "print(player2.name, player2.health, player2.level)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "97c83686-0456-4dea-8859-fb74d709f2b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Species of pet: Canine\n",
      "Pets name: Buddy and is 3 years old\n",
      "Pets name: Lucy and is 2 years old\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Class Variables vs Instance Variables\n",
    "Class Variables are shared by all instances of a class. \n",
    "They are defined inside the class but outside any methods.\n",
    "Instance Variables are unique to each instance and are defined in the init() method.\n",
    "'''\n",
    "\n",
    "class Pets:\n",
    "    species = \"Canine\"  # Class variable\n",
    "\n",
    "    def __init__(self, name, age):\n",
    "        self.name = name  # Instance variable\n",
    "        self.age = age  # Instance variable\n",
    "\n",
    "dog1 = Pets(\"Buddy\", 3)\n",
    "dog2 = Pets(\"Lucy\", 2)\n",
    "\n",
    "print(\"Species of pet: \" + dog1.species)  # Accessing class variable\n",
    "print(\"Pets name: \" + dog1.name + f\" and is {dog1.age} years old\")  # Accessing instance variable\n",
    "print(\"Pets name: \" + dog2.name + f\" and is {dog2.age} years old\")  # Accessing instance variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7c1cae07-bd1e-4d0b-bd05-54e0a5ba2968",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Anita\n",
      "Marks: 85\n",
      "Anita is 85 years old\n",
      "Person name: Anita, her age is 85 years.\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Methods \n",
    "Functions defined inside a class that describe the behaviors or actions an object can perform. \n",
    "They typically manipulate the object's instance variables\n",
    "'''\n",
    "\n",
    "class Student:\n",
    "    def __init__(self, name, marks): # parameterized method\n",
    "        self.name = name\n",
    "        self.marks = marks\n",
    "\n",
    "    def get_info(self):             # non-parameterized method\n",
    "        return f\"{self.name} is {self.marks} years old\"\n",
    "\n",
    "    def display(self):              # non-parameterized method\n",
    "        print(\"Name:\", self.name)\n",
    "        print(\"Marks:\", self.marks)\n",
    "\n",
    "    # __str__() method is a special method that controls what is returned when the object is printed\n",
    "    def __str__(self):\n",
    "        return f\"Person name: {self.name}, her age is {self.marks} years.\"  \n",
    "\n",
    "stud = Student(\"Anita\", 85)         # stud object invokes __init__() by default constructor\n",
    "stud.display()                      # stud object invokes non-parameterized method\n",
    "print(stud.get_info())\n",
    "print(stud)                         # stud object is getting printed\n",
    "\n",
    "# del stud.display                   # the del keyword is used to delete methods from a class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fd4e80c4-11a7-4ae2-9fec-d6bf8dbfe831",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Balance: 2200\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Encapsulation - The practice of bundling data (variables) and methods together \n",
    "into a single unit (a class) while restricting direct outside access. \n",
    "This is usually achieved by making variables private and \n",
    "exposing them only through controlled public get and set methods. \n",
    "'''\n",
    "\n",
    "class DigitalWallet:\n",
    "    def __init__(self, balance):\n",
    "        self.__balance = balance\n",
    "\n",
    "    def add_money(self, amount):\n",
    "        if amount > 0:\n",
    "            self.__balance += amount\n",
    "\n",
    "    def spend_money(self, amount):\n",
    "        if amount <= self.__balance:\n",
    "            self.__balance -= amount\n",
    "        else:\n",
    "            print(\"Insufficient wallet balance\")\n",
    "\n",
    "    def get_balance(self):\n",
    "        return self.__balance\n",
    "\n",
    "\n",
    "wallet = DigitalWallet(2000)\n",
    "\n",
    "wallet.add_money(500)\n",
    "wallet.spend_money(300)\n",
    "\n",
    "print(\"Balance:\", wallet.get_balance())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "db181612-4f83-410d-ae0c-937446282e01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sending email notification\n",
      "Sending SMS notification\n",
      "Sending push notification\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Polymorphism\n",
    "Meaning \"many forms,\" it lets a single interface, method, or object behave\n",
    "differently depending on the context or the type of object acting on it.\n",
    "'''\n",
    "\n",
    "class EmailNotification:\n",
    "    def send(self):\n",
    "        print(\"Sending email notification\")\n",
    "\n",
    "class SMSNotification:\n",
    "    def send(self):\n",
    "        print(\"Sending SMS notification\")\n",
    "\n",
    "class PushNotification:\n",
    "    def send(self):\n",
    "        print(\"Sending push notification\")\n",
    "\n",
    "# one object invoking multiple constructors\n",
    "notifications = [EmailNotification(), SMSNotification(), PushNotification()]  \n",
    "\n",
    "for notification in notifications:\n",
    "    notification.send()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "7eff2fce-144e-4a97-9763-830bea491708",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vehicle started\n",
      "Car boot opened\n",
      "Vehicle started\n",
      "Bicycle bell ringing\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Inheritance\n",
    "A mechanism that allows a new class (subclass/child) to acquire \n",
    "the properties and methods of an existing class (superclass/parent). \n",
    "This promotes code reusability and builds hierarchical relationships.\n",
    "'''\n",
    "\n",
    "class Vehicle:\n",
    "    def start(self):\n",
    "        print(\"Vehicle started\")\n",
    "\n",
    "class Car(Vehicle):\n",
    "    def open_boot(self):\n",
    "        print(\"Car boot opened\")\n",
    "\n",
    "class Bicycle(Vehicle):\n",
    "    def ring_bell(self):\n",
    "        print(\"Bicycle bell ringing\")\n",
    "\n",
    "car = Car()\n",
    "bicycle = Bicycle()\n",
    "\n",
    "car.start()\n",
    "car.open_boot()\n",
    "\n",
    "bicycle.start()\n",
    "bicycle.ring_bell()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78bf26a1-c7be-48bc-b17e-5235183e5a04",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Method Overriding\n",
    "A feature of runtime polymorphism where a subclass provides its own specific \n",
    "implementation of a method that is already defined in its parent class. \n",
    "The method name, parameters, and return type must match exactly.\n",
    "'''"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
