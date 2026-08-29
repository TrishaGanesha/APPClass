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
print("File closed:",file.closed)"""
