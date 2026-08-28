#module define group of task (function,variables)
#library/package(collection of similar module)
#list of built in module or packages
#create a user defined module can be function variable or class,how to save a module
#how to use the user defined module =1.import module name,2.specific=from module_name import method_name1,mn2....  3.Alias import module_name as mn
# package=modules=submodules(studentdetails.py)=methods/function(studetails())
#create a module (.py with specific functionality)
#create a package=create directory/folder=in that create module within module create functions/methods or submodules 
#a module is python(.py) containing functions,variable,class
#why use modules=to avoid 100 of lines,difficult to maintain,code reusability,modularity,easy maintainece
#built in modules math,random,statistics,datetime,os,sys,clander,collections,re,json

#Import statements =there are several ways to import functionality
#import entire module
import math
math.sqrt(36)
#import specific function
from math import sqrt
sqrt(36)
#mulitple methods
from math import sqrt,factorial
#import using alias
import math as m
m.sqrt(36)

#Packages
#__init__.py=default ,user defined must have this module which will allow access all other modules within when python version less than 3.3,now it is automatic
#create package=1.create project folder,then open in vs code(in jupyter other way)





#create a module called calculator
import Calculator

print("sum",Calculator.add(5,6))
print("difference",Calculator.sub(6,5))
print("Multiply",Calculator.multiply(5,6))
print("Division",Calculator.divide(35,5))


import Calculator as cal

print("sum",cal.add(5,6))
print("difference",cal.sub(6,5))
print("Multiply",cal.multiply(5,6))
print("Division",cal.divide(35,5))

from Calculator import add,sub,multiply,divide
print(add(6,7))
print(sub(6,7))
print(multiply(6,7))
print(divide(36,6))




