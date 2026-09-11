#OOPs ,class methods, static methods, instance methods
#not static method should have self as first argument
#an online food delivey application
#creates an order using customer name,food item and quantity
"""class FoodOrder:
    def __init__(self,customer_name,food_item,quantity):  #Parameterized constructor
        self.customer_name=customer_name
        self.food_item=food_item
        self.quantity=quantity

order1=FoodOrder("John","Pizza",2)   #FoodOrder() is the constructor of the class FoodOrder
order2=FoodOrder("Alice","Burger",1)#order1 and order2 are the objects of the class FoodOrder
print("Customer Name:"+order1.customer_name)
print("Food Item:"+order1.food_item)
print("Quantity:",order1.quantity)

print("Customer Name:"+order2.customer_name)
print("Food Item:"+order2.food_item)
print("Quantity:"+str(order2.quantity))"""


#instance variable = variables that are defined inside the constructor and are unique to each object of the class
#class variable = variables that are defined inside the class but outside the constructor and are shared among all objects of the class
#diff between instance variable and class variable is that instance variable is unique to each object of the class and class variable is shared among all objects of the class
#methods = functions that are defined inside the class and are used to perform operations on the objects of the class
#built in methods = methods that are defined inside the class and are used to perform operations on the objects of the class
#init method = constructor of the class that is used to initialize the instance variables of the class ,built in method that is called when an object of the class is created
#__str__ method = built in method that is used to return a string representation of the object of the class
#Encapsulation = concept of wrapping data and methods that operate on that data within a single unit (class) and restricting access to some of the object's components
#self.__balance = private variable that can only be accessed within the class and not outside the class
