#mode      Read methods           write methods
# r           read()                   write()
# w           readline()               writelines()
# a           readlines()           
# r+
# w+

#methods
# open()
# read()
# write()
# close()
#seek() 
#tell()   #diff seek and tell(returns to current pointer position,default tell returns to=last position(for w),to first position(for r))

#different methods to inspect file properties:
"""file=open("students.txt","r+")
readcontent=file.read()
file.write("\nThank you")
print("Read Content:\n",readcontent)
print("File Name:",file.name)
print("File Mode:",file.mode)
print("File Closed:",file.closed)


#The with statement automatically closes the file
with open("students.txt","a") as file:
    name=input("enter new student name:")
    file.write(name+"\n")
print("student added successfully")
print("File closed:",file.closed)


#Counting Lines,Words, and Characters in a file  
with open("students.txt","r") as file:
    content=file.read()
lines=content.splitlines()
words=content.split()
characters=len(content)
print("number of lines:",len(lines))
print("number of words:",len(words))
print("number of characters",characters)

#without built do
with open("students.txt","r") as file:
    content=file.read()


#The file pointer tell() indicate the current position in the file
with open("students.txt","r") as file:
    print("Initial position:",file.tell())
    print(file.read(5))
    print("Position after reading",file.tell())

#for other operation
with open("students.txt","a") as file:
    print("Initial position:",file.tell())
    print(file.read(0))
    print("Position after reading",file.tell())
#seek() moves the file pointer to a specific position
with open("students.txt","r") as file:
    print(file.read(10))
    print("Position before seeking:",file.tell())
    file.seek(5)
    print("Position after seeking:",file.tell())
    print(file.read(6))#from 5 read 6 character

#an MCA department wants to store students information such as
#roll number,name,course,marks
#write,read,search for paticular information ,change year as pormoted 1st to 2nd year(save as 1st year to 2nd year rename the file,creating as duplicate file),delete first year students detail file using remove
#delete folder rmdir
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")
    year = input("Enter year: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{course},{marks},{year}\n")

    print("Student added successfully")

    def display_students():
        with open("students.txt", "r") as file:
            for line in file:
                print(line.strip())

def search_student():
    roll = input("Enter roll number to search: ")

    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[0] == roll:
                print("Student found:")
                print("Roll:", data[0])
                print("Name:", data[1])
                print("Course:", data[2])
                print("Marks:", data[3])
                print("Year:", data[4])
                return

    print("Student not found")
add_student()
search_student()"""


import os

# 1. WRITE student details
f = open("1st_year.txt", "w")

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Roll No: ")
    name = input("Name: ")
    course = input("Course: ")
    marks = input("Marks: ")

    f.write(f"{roll},{name},{course},{marks}\n")

f.close()
print("Student details saved.")


# 2. READ student details
f = open("1st_year.txt", "r")

print("\nStudent Details:")
print(f.read())

f.close()


# 3. SEARCH particular student
roll = input("Enter roll number to search: ")

f = open("1st_year.txt", "r")
found = False

for line in f:
    data = line.strip().split(",")

    if data[0] == roll:
        print("Student Found:")
        print("Roll No:", data[0])
        print("Name:", data[1])
        print("Course:", data[2])
        print("Marks:", data[3])
        found = True

f.close()

if not found:
    print("Student not found.")


# 4. PROMOTE 1st year → 2nd year
# Creates a duplicate file first
f1 = open("1st_year.txt", "r")
f2 = open("2nd_year.txt", "w")

for line in f1:
    f2.write(line)

f1.close()
f2.close()

print("Students promoted to 2nd year.")


# 5. Delete 1st year file
os.remove("1st_year.txt")
print("1st year file deleted.")


# 6. Create and delete folder
os.mkdir("MCA_Students")

# Folder must be empty before rmdir
os.rmdir("MCA_Students")

print("Folder deleted.")