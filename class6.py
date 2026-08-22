#when recursive will fail=stack overflow
#to handle stack overflow,tradition appraoch=iteratively,tail recursion,dp(tabular)
#(accumelator=track of variable)no need of stack but use variable =tail recursion
#recursive tree (ada=masters ,substituion,recursive tree,brute froce)


#tail recurisve call is the last thing the function does
#factorial using tail recursive
"""def factorial(n):
    if n==0 or n== 1:
        return 1
    else:
        return n*factorial(n-1)
value=factorial(5)
print(value)
def factorial(n,result=1):
    if n==0:
        return result
    return factorial(n-1,result*n)
print(factorial(5))

def factorial(n,result=1):
    print(n,result)
    if n==0:
        return result
    return factorial(n-1,result*n)
print(factorial(5))
#sum of n numbers using tail recursion
def sum_num(n,result=0):
    print(n,result)
    if n==0:
        return result
    return sum_num(n-1,result+n)
print(sum_num(5))"""

#fibonacci using tail recursion
def fibonacci(n,a=0,b=1):
    print(n,a,b)#to print tree
    if n==0 :
        return a
    return fibonacci(n-1,b,a+b)
print(fibonacci(5))
for i in range(3):
    print(fibonacci(i),end=" ")
#python does not perform tail call optimization so iterative solution is used for large computation
#Tail Recursion vs Normal Recursion
#Feature                            Normal Recursion                           Tail Recursion
#Recursion call                     not necessarily last                         last operation
#Pending Operation                  Yes                                          no
#use accumulator                    Usually no                                   often yes
#Tail call optimization in python    no                                           no
#stack limitation                    yes                                          still yes in python