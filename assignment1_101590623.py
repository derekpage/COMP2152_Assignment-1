"""
Author: Derek Page
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5 # Float
highest_reps = 25 # Int
membership_active = True # Boolean

# Step c: Create a dictionary named workout_stats
# Dictionary data type: A mutable collection of key value pairs
# In this instance the key is a string and the value is a tuple of ints
workout_stats = {
    "John": (20, 30, 45),
    "Bob": (60, 20, 40),
    "Alice": (40, 20, 70),
    "Jason": (30, 60, 120),
    "Jennifer": (10, 30, 15)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
totals = {}
for member, stats in workout_stats.items():
    total = stats[0] + stats[1] + stats[2]
    totals[member + "_Total"] = stats[0] + stats[1] + stats[2]
workout_stats = workout_stats | totals

# Step e: Create a 2D nested list called workout_list
# List datatype: An ordered collection of items
# In this case the list contains lists which themselves contain ints
workout_list = []
for stats in workout_stats.values():
    if isinstance(stats, tuple):
        workout_list.append([stats[0], stats[1], stats[2]])

# Step f: Slice the workout_list
for stats in workout_list:
    print(stats[slice(2)])
for stats in workout_list[slice(len(workout_list) - 2, len(workout_list))]:
    print(stats[slice(2,3)])
print()

# Step g: Check if any friend's total >= 120
for member, stats in workout_stats.items():
    if isinstance(stats, int) and stats >= 120:
        print(f"Great job staying active, {member[:-6]}!")
print()

# Step h: User input to look up a friend
search_name = input("Please enter a friend name\n")
found = False
for member, stats in workout_stats.items():
    if isinstance(stats, tuple) and member == search_name:
        print(f"Yoga: {stats[0]}, Running: {stats[1]}, Weightlifting: {stats[2]}")
        print("Total:", workout_stats[member + "_Total"])
        found = True
        break
if not found:
    print(f"Friend {search_name} not found in the records.")
print()

# Step i: Friend with highest and lowest total workout minutes
highest = ("", 0)
lowest = ("", 0)
for member, stats in workout_stats.items():
    if isinstance(stats, int):
        if stats > highest[1]:
            highest = (member[:-6], stats)
        if lowest[1] == 0 or stats < lowest[1]:
            lowest = (member[:-6], stats)
print("Highest is", highest[0], "with", highest[1], "minutes")
print("Lowest is", lowest[0], "with", lowest[1], "minutes")