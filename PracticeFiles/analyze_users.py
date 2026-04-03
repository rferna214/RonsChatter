import json 

with open("users.json", "r") as file:
    users = json.load(file)

adults = 0
minors = 0
total_age = 0

for user in users:
    if user["status"] == "Adult":
        adults += 1
    else:
        minors += 1

    total_age += user["age"]

average_age = total_age / len(users)

print(f"Total Users: {len(users)}")
print(f"Adults: {adults}")
print(f"Minors: {minors}")
print(f"Average Age: {average_age}")

us_users = [user for user in users if user["country"] == "United States"]

print(f"US users: {len(us_users)}")

oldest_user = max(users, key=lambda x:x["age"])

print(f"Oldest: {oldest_user['first_name']} ({oldest_user['age']})")