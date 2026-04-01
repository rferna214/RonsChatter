import requests

for i in range(3):
    response = requests.get("https://randomuser.me/api/")
    data = response.json()

    #print(data)

    user = data["results"][0]

    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    country = user["location"]["country"]
    age = user["dob"]["age"]
    status = user["dob"]["age"]

    if age < 18:
        status ="Minor"
    else:
        status = "Adult"
        print(f"Name: {first_name} {last_name}")
        print(f"Country: {country} ")
        print(f"Age: {age} ") 
        print(f"Status: {status} ") 
        print("\n-----\n")
 


