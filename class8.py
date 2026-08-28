#Files 
#Text file=txt,XML,JSON....
#Mode=r,w,a,r+,w+,a+,...
#operations=open,read,close
#file creating using open operation,mode =write to create a file
#to read and write into a file r+,w+
#default parameters in file =2,path and mode
#what happens if file is not closed
#to close file,file.close,with pointer to null,with statement


#create/Open a File
"""file=open("students.txt","w")
print("File opened successfully")
file.close()

#Writing to a text file
file=open("students.txt","w")
file.write("Anita\n")
file.write("Rahul\n")
file.write("Priya\n")
file.close()
print("student details saved successfully")

# #writing multiples Lines using writelines()
# students=["Anita\n","Anu\n","Bhanu\n"]
# file=open("students.txt","w")
# file.writelines(students)
# file.close()

#append the data
#writing multiples Lines using writelines()
students=["Jake\n","Ammy\n","Rosa\n"]
file=open("students.txt","a")
file.writelines(students) #can use write  also but for single string
file.close()

#Reading a complete file
file=open("students.txt","r")
content=file.read()
print(content)
file.close()

#Reading a specific number of characters
file=open("students.txt","r")
content=file.read(10)
print(content)
file.close()


#Reading one lines at a time
file=open("students.txt","r")
line=file.readline()
print(line)
file.close()

#Reading all lines into a list
file=open("students.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()"""

#Reading all lines using readlines()
file=open("students.txt","r")
lines=file.readlines()#list of strings is returned
print(lines)
file.close()

#read specific number of lines,or statisfy a certain condition(read only verbs in statement) with loop 





