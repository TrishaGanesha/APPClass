#When to use shorthand coniditon
#to code readable ,simple,qucik assignment based on condition
#short hand if
"""n=int(input("enter the age"))
if n>=18:print("eligible to vote")
#short hand if else
marks=int(input("enter the marks"))
print(f"pass with score {marks}") if marks>=35 else print(f"you are fail with marks {marks}")
#assign value based on if else
result = "pass" if marks>=35 else "fail"
print(f"result: {result}")
#multiple condition
amount=int(input("enter the amount"))
discount=0.1 if amount>=10000 else 0.05 if amount>=5000 else 0.02
print(f"discount: {discount*100}%")
#combining multiple conditions
age=int(input("enter the age"))
is_stud=False
dscnt_code=True
if(age<18 and age>65) and not is_stud or dscnt_code:
    print("eligible for discount")
else:
    print("not eligible for discount")
#leap year
year=int(input("enter the year"))
leapyear=print("leap")if year%4==0 and year%100!=0 or year%400==0 else print("not leap")
#using paranthesis for clarity
temp=25
is_rain=False
is_weekend=True
if(temp>20 and not is_rain) or is_weekend:
    print("great day for outdoor activity")
#multiple condition
marks=int(input("enter the marks"))
print("O") if marks>=90 else\
print("A") if marks>=80 else\
print("B") if marks>=70 else\
print("C") if marks>=60 else\
print("F")
#fibnocii using while
n=int(input("enter the fibonacii number range"))
a,b=0,1
i=0
while(i<n):
    print(a,end=" ")
    a,b=b,a+b
    i+=1
n="hello"
for i in reversed(range(len(n))):
    print(n[i])"""
#sort is used for list type of data type ,sorted is used for other data type


