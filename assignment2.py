# 1. Increasing Right Triangle
print("Increasing Right Triangle:")
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
print("\n")


print("Decreasing Right Triangle:")
# 2. Decreasing Right Triangle
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print("\n")


print("Right-Aligned Increasing Triangle:")
# 3. Right-Aligned Increasing Triangle
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("* ", end="")
    print()
print("\n")


print("Right-Aligned Decreasing Triangle:")
# 4. Right-Aligned Decreasing Triangle
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("* ", end="")
    print()
print("\n")


print("Full Pyramid:")
# 5. Full Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * (2 * i - 1))
print("\n")


print("Inverted Pyramid:")
# 6. Inverted Pyramid
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * (2 * i - 1))
print("\n")


print("Diamond Pattern:")
# 7. Diamond
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("* " * (2 * i - 1))
print("\n")


print("Hollow Pyramid:")
# 8. Hollow Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    elif i == n:
        print("* " * (2 * i - 1))
    else:
        print("*" + " " * (2 * i - 3) + "*")
print("\n")


print("Solid Square:")
# 9. Solid Square
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
print("\n")


print("Hollow Square:")
# 10. Hollow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")


print("Number Square:")
# 11. Number Square
n = 5
for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()
print("\n")


print("Same Number Square:")
# 12. Same Number Square
n = 5
for i in range(1, n + 1):
    for j in range(n):
        print(i, end=" ")
    print()
print("\n")


print("Increasing Number Triangle:")
# 13. Increasing Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("\n")


print("Decreasing Number Triangle:")
# 14. Decreasing Number Triangle
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("\n")


print("Repeated Number Triangle:")
# 15. Repeated Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
print("\n")


print("Reverse Number Triangle:")
# 16. Reverse Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(n, n - i, -1):
        print(j, end=" ")
    print()
print("\n")


print("Continuous Number Triangle:")
# 17. Continuous Number Triangle
n = 4
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
print("\n")


print("Number Pyramid:")
# 18. Number Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
print("\n")


print("Increasing Alphabet Triangle:")
# 19. Increasing Alphabet Triangle
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
print("\n")


print("Decreasing Alphabet Triangle:")
# 20. Repeated Alphabet Triangle
n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()
print("\n")


print("Continuous Alphabet Triangle:")
# 21. Continuous Alphabet Triangle
n = 5
ch = 65
for i in range(1, n + 1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("\n")


print("Reverse Alphabet Triangle:")
# 22. Reverse Alphabet Triangle
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
print("\n")


print("X Pattern:")
# 23. X Pattern
n = 5
for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("\n")


print("Plus Pattern:")
# 24. Plus Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


print("Hollow Diamond:")
# 25. Hollow Diamond
n = 5

for i in range(n):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*" + " " * (2 * i - 1) + "*")
print("\n")


print("Hourglass Pattern:")
# 26. Hourglass Pattern
n = 5

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * (2 * i - 1))

for i in range(2, n + 1):
    print(" " * (n - i), end="")
    print("* " * (2 * i - 1))
print("\n")


print("Filtering Based on Condition:")
# 27. Filtering Based on Condition
numbers = [12, 45, 7, 23, 56, 18, 90]
large_numbers = []

for num in numbers:
    if num > 21:
        large_numbers.append(num)

print(large_numbers)
print("\n")


print("Reversing a String Using For Loop:")
# 28. Reversing a String Using For Loop
original_str = "Python"
reversed_str = ""

for ch in original_str:
    reversed_str = ch + reversed_str

print(reversed_str)
print("\n")