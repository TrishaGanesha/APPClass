arr=list(map(int,input("enter the numbers").split()))
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("sorted array:",arr)
#jump statements: pass and continue
for i in range(6):
    if i==5:
        pass
    else:
        print(i)
    print("hello")
for i in range(6):
    if i==5:
        continue
    else:
        print(i)
    print("hello")
#print prime numbers in given range

import math

n=int(input("enter the range"))
for i in range(2,n):
    y=int(math.sqrt(i))+1
    for j in range(2,y):
        if i%j==0:
            break
    else:
        print(i,end=" ")
#take input until 0 is entered and print the sum of all numbers
sum=0
while True:
    n=int(input("enter the number"))
    if n==0:
        break
    sum+=n
print(f"sum of all numbers: {sum}")
total=0
num=int(input("enter the number"))
while num!=0:
    total+=num
    num=int(input("enter the number"))
print(f"sum of all numbers: {total}")
#factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number"))
result=factorial(n)
print(f"factorial of {n} is {result}")
#print pattern
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#pyramid pattern
for i in range(1,5):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
def print_pyramid(rows: int) -> None:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)


n = int(input("Enter number of rows: "))
print_pyramid(n)
