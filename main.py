import requests

#Exit stops the page from executing. kinda like a break


try:
    count = int(input("Put in a number to loop?"))
except:
    print("This shit wont work")
    exit()

if count > 10:
    print("Nope!!!!")
    exit()


print(count)

for i in range(count):
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




