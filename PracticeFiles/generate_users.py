#This page gets teh users from the api 
import json
from urllib.request import urlopen

def get_user():
    with urlopen("https://randomuser.me/api/") as response:
        data = json.loads(response.read().decode())
    return data["results"][0]

def format_user(user):
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    country = user["location"]["country"]
    age = user["dob"]["age"] 

    if age < 18:
        status = "Minor"
    else:
        status = "Adult"

    return {
        "first_name": first_name, 
        "last_name": last_name, 
        "country": country, 
        "age": age, 
        "status": status
    }

try:
    count = int(input("How many users? "))
except:
    print("Invalid input")
    exit()

if count > 10:
    print("Max is 10")
    exit()


users_list = [] 

for i in range(count):
    user = get_user()
    formatted_user = format_user(user)
    users_list.append(formatted_user)

    print(f"Name: {formatted_user['first_name']} {formatted_user['last_name']}")
    print(f"Country: {formatted_user['country']}")
    print(f"Age: {formatted_user['age']}")
    print(f"Status: {formatted_user['status']}")
    print("\n-----\n")

with open("users.json", "w") as file:
    json.dump(users_list, file, indent=4)