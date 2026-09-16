# #comparision magic method
# #compare 2 product based on the review
# #class Product has
# class Product:
#     def __init__(self,name,price,rating,reviews,discount,warranty)
#     def score(self):
#         review_score=min(self.reviews/100,10)
#         overall_score=(self.rating*20+self.discount*2...)
#     def __str__():
#         review_score,overallscore=self.score()
#         return f"{review_score}"
#     def __eq__(self,other):
#         return self.other()[0]==other.score()[0]
#     def__ne__
#     def __lt__(self, other):
#         return self.score()<other.score()
#     def __gt__(self, other):
#     def__ge__
#     def __le__

# p1=Product()
# p2=Product()

# print("score",p1.score())#return multiple values in tuple form
# print("",p2.score())
# print("overallscore")
# review1,score1=p1.score()#assigning to respective variable ,multivalue assignment
# review2,score2=p2.score()
# print(score1)
# print(score2)
# print(f"Review score{p1.name}",p1)#__str__is invoked
# print(f"Review score{p2.name}",p2)


# print("comparisions")
# print(f"{p1.score()[0]}=={p2.score()[0]}:",p1==p2)#invokes __eq__()

class Product:
    def __init__(self, name, price, rating, reviews, discount, warranty):
        self.name = name
        self.price = price
        self.rating = rating
        self.reviews = reviews
        self.discount = discount
        self.warranty = warranty

    def score(self):
        review_score = min(self.reviews / 100, 10)
        overall_score = self.rating * 20 + self.discount * 2 + review_score + self.warranty
        return review_score, overall_score

    def __str__(self):
        review_score, overall_score = self.score()
        return f"Review Score: {review_score}, Overall Score: {overall_score}"

    def __eq__(self, other):
        return self.score()[0] == other.score()[0]

    def __ne__(self, other):
        return self.score()[0] != other.score()[0]

    def __lt__(self, other):
        return self.score()[1] < other.score()[1]

    def __gt__(self, other):
        return self.score()[1] > other.score()[1]

    def __le__(self, other):
        return self.score()[1] <= other.score()[1]

    def __ge__(self, other):
        return self.score()[1] >= other.score()[1]


p1 = Product("Laptop", 50000, 4.5, 850, 10, 2)
p2 = Product("Mobile", 30000, 4.2, 650, 20, 1)

print("Score:")
print(p1.score())
print(p2.score())

review1, score1 = p1.score()
review2, score2 = p2.score()

print("\nOverall Scores:")
print(score1)
print(score2)

print("\nProduct Details:")
print(f"Review score {p1.name}:", p1)
print(f"Review score {p2.name}:", p2)

print("\nComparisons:")
print(f"{p1.score()[0]} == {p2.score()[0]}:", p1 == p2)
print(f"{p1.score()[0]} != {p2.score()[0]}:", p1 != p2)
print(f"{score1} < {score2}:", p1 < p2)
print(f"{score1} > {score2}:", p1 > p2)
print(f"{score1} <= {score2}:", p1 <= p2)
print(f"{score1} >= {score2}:", p1 >= p2)

#unary operator neg,pos,abs,invert
class Number:
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return -self.value

    def __pos__(self):
        return +self.value

    def __abs__(self):
        return abs(self.value)

    def __invert__(self):
        return ~self.value


# n = Number(-10)

# print(-n)
# print(+n)
# print(abs(n))
# print(~n)

n = Number(10)

print(-n)
print(+n)
print(abs(n))
print(~n)

#matrix multiplication
#__matmul__ of 2 object
# A=Matrix([[1,2],[3,4]])
# B=Matrix([[5,6],[7,8]])
# c=A@B #invoking using @ symbol
# c.display()

class Matrix:
    def __init__(self, data):
        self.data = data

    def __matmul__(self, other):
        result = []

        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                total = 0
                for k in range(len(other.data)):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)

        return Matrix(result)

    def display(self):
        for row in self.data:
            print(row)


A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

C = A @ B

C.display()

#user defined magic method and calling the magic method
class Number:
    def __init__(self, n):
        self.n = n

    def __factorial__(self):
        fact = 1
        for i in range(1, self.n + 1):
            fact *= i
        return fact


n = Number(5)

print(n.__factorial__())


#iterator is an object that allows to traverse
#list,tuple,set,dictionary iterable object
#iteration is powered by the iterator protocol
#iterator is stack holder,when ever iteratable is called it will invoke the iterator
#the for loop can traverse the list becasue the list is iterable not a iterator
numbers=[1,2,3,4]
_iterator=iter(numbers) #calls numbers.__iter__()
while True:
    try:
        item=next(_iterator)  #first is used for 0 index for next index next is used
    except StopIteration:
        break #cleanly exits the loop when data runs out
# when iteartor is accessing itearable object then invokes _iterator ,then _iterator will invoke next
# for loop->iter(object)->_iterator->next(_iterator)->value->next(_iterator)->till runs out of numbers
print(iter(numbers))
# iterable (book)vs iterator (bookmark)