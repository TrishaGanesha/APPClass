import math

partners = [
    {"id": "D101", "name": "Rahul", "location": (12, 11),
     "status": 1, "deliveries": 8, "rating": 5, "idle": 10},

    {"id": "D102", "name": "Anu", "location": (9, 8),
     "status": 1, "deliveries": 4, "rating": 4, "idle": 8},

    {"id": "D103", "name": "Kiran", "location": (9, 8),
     "status": 0, "deliveries": 4, "rating": 3, "idle": 12},

    {"id": "D104", "name": "John", "location": (11, 9),
     "status": 1, "deliveries": 2, "rating": 5, "idle": 6}
]

restaurant = (6, 7)


def distance(partner):
    x1, y1 = partner["location"]
    x2, y2 = restaurant

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# 1. Only available partners
available = [p for p in partners if p["status"] == 1]

if not available:
    print("All partners are busy. Order placed in waiting queue.")

else:
    # 2. Fewest deliveries
    min_deliveries = min(p["deliveries"] for p in available)
    candidates = [
        p for p in available
        if p["deliveries"] == min_deliveries
    ]

    # 3. Highest rating
    max_rating = max(p["rating"] for p in candidates)
    candidates = [
        p for p in candidates
        if p["rating"] == max_rating
    ]

    # 4. Nearest partner
    min_distance = min(distance(p) for p in candidates)
    candidates = [
        p for p in candidates
        if distance(p) == min_distance
    ]

    # 5. Idle longest
    selected = max(candidates, key=lambda p: p["idle"])

    # Update partner
    selected["status"] = 0
    selected["deliveries"] += 1

    print("Delivery Assigned to", selected["id"])