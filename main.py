import requests

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

    return first_name, last_name, country, age, status


try:
    count = int(input("Put in a number to loop?"))
except:
    print("Error!!! dont put that in!!!")
    exit()

if count > 10:
    print("Nope!!!!")
    exit()

 

for i in range(count):

    user = get_user()
    first_name, last_name, country, age, status = format_user(user)

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


    print(f"Name: {first_name} {last_name}")
    print(f"Country: {country} ")
    print(f"Age: {age} ") 
    print(f"Status: {status} ") 
    print("\n-----\n")

