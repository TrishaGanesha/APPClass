# Electricity Bill Calculator

category = input("Enter consumer category (Domestic/Commercial/Heavy load): ")
units = float(input("Enter units consumed: "))

# Rate based on consumer category
if category.lower() == "domestic":
    rate = 5
elif category.lower() == "commercial":
    rate = 8
elif category.lower() == "heavy load":
    rate = 12
else:
    print("Invalid consumer category")
    exit()

# First 120 units are free
if units <= 120:
    bill = 0
else:
    bill = (units - 120) * rate

print("Consumer Category:", category)
print("Units Consumed:", units)
print("Rate per Unit:", rate)
print("Electricity Bill: ₹", bill)