#Exception Handling
#Student file marks record
#Marks can be a list numeric data for 100 marks marks=[25,35,90,"AB",87,"NAme"]
#updated marks=[25,35,90,87]
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
# git init
# git add .
# git commit -m "class9"