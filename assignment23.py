try:
    marks = 150

    if marks > 100:
        raise ValueError("Marks cannot be greater than 100")

except ValueError as e:
    print("Error:", e)

print("Program continues...")