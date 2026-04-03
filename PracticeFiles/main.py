import requests
import json

#Exit stops the page from executing. kinda like a break



def get_user():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
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
    count = int(input("Put in a number to loop?"))
except:
    print("Error!!! dont put that in!!!")
    exit()

if count > 10:
    print("Nope!!!!")
    exit()

users_list = []

for i in range(count):

    user = get_user()
    formatted_user = format_user(user)
    users_list.append(formatted_user)

    #response = requests.get("https://randomuser.me/api/")
    #data = response.json()
    #print(data)
    #user = data["results"][0]

    #first_name = user["name"]["first"]
    #last_name = user["name"]["last"]
    #country = user["location"]["country"]
    #age = user["dob"]["age"] 

    #if age < 18:
    #    status ="Minor"
    #else:
    #    status = "Adult"
 





    print(f"Name: {formatted_user['first_name']} {formatted_user['last_name']}")
    print(f"Country: {formatted_user['country']} ")
    print(f"Age: {formatted_user['age']} ") 
    print(f"Status: {formatted_user['status']} ") 
    print("\n-----\n")

with open("user.txt", "w") as file:
    for user in users_list:
        file.write(f"{user['first_name']} {user['last_name']}, ") 
        file.write(f"{user['country']}, ") 
        file.write(f"{user['age']}, ") 
        file.write(f"{user['status']}") 


