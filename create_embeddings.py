import json 
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def user_to_text(user):
    return f"{user['first_name']} from {user['country']} is {user['age']} years old and is an {user['status']}"

#load users
with open("project/users.json", "r") as file:
    users = json.load(file)

# convert to text
user_texts = [user_to_text(user) for user in users]

# create embeddings
embeddings = model.encode(user_texts)

# convert numpy to list (IMPORTANT)
embeddings_list = embeddings.tolist()

# save
with open("project/embeddings.json", "w") as file:
    json.dump(embeddings_list, file)

print("Embeddings saved!")