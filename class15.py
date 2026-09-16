class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B,C):
    print("D")
obj=D()
obj.show()
print(D.mro())
#MRO Method Resolution Order-when multiple inheritence is used


#Magic methods=100 built in magic method among them 20 most commonly used
#__init__(),__str__(),__repr__(),__eq__(),__add__(),___len__(),__lt__(),__contains__(),__call__() wrt object value of multiple classes

#object creation new,init
# str,repr
# eq,ne,lt,gt,le,ge
# add sub,mul,truediv,floordiv
# radd,rsub,rmul
# neg,pos,abs,invert
# len,getitem,setitem,delitem,concatinate
# iter,next
# getattrenter exitcall
# int float bool IndexError
# hash
# format

#oject representation=__str__(),__repr__()
# class research:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def __str__(self):
#         return f"{self.title}-{self.author}"
#     def __repr__(self):
#         return f"RPf("{self,title}")
# paper=research("a","b")
# print(paper)#__str__ is called,first init
# print(repr(paper))

class lib:
    def __init__(self,book):
        self.book=book
    def __len__(self):
        return len(self.book)
    def __contains__(self, item):
        return item in self.book
lib1=lib(["a","b"]) #passed to constructor
#indexing and item assignment
#create a marks class that allows students marks to be accessed and modified
#getitem gets the value,loads value in specific index=setitem if it is proper value update it or throw error
#print the value of object before and after modification using __str__,print(*lib1)==error

#arthematic =diff def __add__(),sub,mul determine the discount ifprice<1000:discount=Discount(0),price<5000:discount=Discount(100)...Discount is class,class product has add,sub,mul is methods
#total=product*quantity ==object*variable,* this will go to __mul__() beacuse it is operator overloading
#price_after_discount=product-discount#object of class product-object of class discount,- is calling __sub__() magic method
#finalprice=price_after_discount*quantity,normal variable no call of magic method



    