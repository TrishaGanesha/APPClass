#Exception Handling
#Student file marks record
#Marks can be a list numeric data for 100 marks marks=[25,35,90,"AB",87,"NAme"]
#updated marks=[25,35,90,87]
# with open("students.txt", "r") as file:
#     for line in file:
#        try:
#            marks=int(line.strip().split(","))
#            if marks<0 or marks>100:
#                raise ValueError("Marks must be between 0 and 100" \)
               

"""try:
    #marks=[25,35,90,"87","NAme"]
    marks=list(input("Enter marks separated by space: ").split())
    updated_marks=[]
    for mark in marks:
        updated_marks.append(int(mark))
    print("Updated Marks:",updated_marks)
except ValueError as e:
    print("Error occurred while converting marks to integer:", e)
    print("updated marks",updated_marks)

marks = input("Enter marks separated by space: ").split()

updated_marks = []

for mark in marks:
    try:
        updated_marks.append(int(mark))
    except ValueError as e:
        print(f"Error occurred while converting '{mark}' to integer: {e}")
        continue

print("Numeric marks:", updated_marks)

n=int(input("Enter number of students: "))
updated_marks=[]
for i in range(n):
    mark=input("Enter marks: ")
    try:
        updated_marks.append(int(mark))
    except ValueError as e:
        print(f"Error occurred while converting '{mark}' to integer: {e}")
        continue

print("updated marks list", updated_marks)"""

#Banking application widthdrawal is negative,deposit is 0 raise exception
balance=1000
deposit=int(input("Enter amount to deposit: "))
try:
    if deposit<=0:
        raise ValueError("Deposit amount must be greater than zero")
except ValueError as e:
    print("Error:", e)
else:
    balance += deposit
    print("Deposit successful. New balance:", balance)
try:
    amount=int(input("Enter amount to withdraw: "))
    if amount<0:
        raise ValueError("Withdrawal amount cannot be negative")
    elif amount>balance:
        raise ValueError("Insufficient balance")
    else:
        balance-=amount
        print("Withdrawal successful. New balance:", balance)
except ValueError as e:
    print("Error:", e)
# student name cannot be empty
# marks must be numeric
# marks must be between 0 and 100
# invalid marks using user defined exception
# valid student record store in file
# user should be allowed to enter multiple student using a loop

#temp info if user enter the non numeric raise a error 
#info using array only one type of data type


