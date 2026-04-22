from flask import Flask, render_template, request
from anthropic import Anthropic
import json
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
    
chat_history = []

load_dotenv()

app = Flask(__name__)
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Load user once

with open("project/users.json", "r") as file:
    users = json.load(file)
 
with open("project/embeddings.json", "r") as file:
    user_embeddings = np.array(json.load(file))

def user_to_text(user):
    return f"{user['first_name']} from {user['country']} is {user['age']} years old and is an {user['status']}"

user_texts = [user_to_text(user) for user in users] 

def find_relevant_users_semantic(question, top_k=3):
    question_embedding = model.encode([question])[0]

    similarities = []

    for i, user_embedding in enumerate(user_embeddings):
        score = np.dot(question_embedding, user_embedding)
        similarities.append((score, users[i]))

    similarities.sort(reverse=True, key=lambda x: x[0])

    return [user for _, user in similarities[:top_k]]



@app.route("/", methods=["GET", "POST"])
def index(): 

    if request.method == "POST":

        if "clear" in request.form:
            chat_history.clear()
            return render_template("index.html", chat=chat_history)

        question = request.form["question"]
        filtered_users = find_relevant_users_semantic(question)

        chat_history.append({"role": "user", "content": question})
        system_prompt = f"""
            You are a data analyst.

            Use ONLY this filtered dataset:

            {filtered_users}

            Answer the question clearly and concisely.
            """

        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=500,
            messages  = [
                {
                    "role": "user", 
                    "content": system_prompt
                    }
            ] + chat_history
        )

    

        answer = response.content[0].text

        chat_history.append({"role": "assistant", "content": answer})

    return render_template("index.html", chat=chat_history)

#This is only for the website
#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    app.run(debug=True)
        