from flask import Flask, render_template, request
from anthropic import Anthropic
import json
import os
from dotenv import load_dotenv
    
chat_history = []

load_dotenv()

app = Flask(__name__)
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Load user once

with open("project/users.json", "r") as file:
    users = json.load(file)

def find_relevant_users(users, question):
    question = question.lower()
    results = []

    for user in users:
        # simple keyword matching
        if "adult" in question and user["status"] == "Adult":
            results.append(user)
        elif "minor" in question and user["status"] == "Minor":
            results.append(user)
        elif user["country"].lower() in question:
            results.append(user)

    #fall back (if nothing is matched)
    if not results:
        return users

    return results




@app.route("/", methods=["GET", "POST"])
def index(): 

    if request.method == "POST":

        if "clear" in request.form:
            chat_history.clear()
            return render_template("index.html", chat=chat_history)

        question = request.form["question"]
        filtered_users = find_relevant_users(users, question)

        chat_history.append({"role": "user", "content": question})
        system_prompt = f"""
            You are a data analyst.

            Use ONLY this filtered dataset:

            {filtered_users}

            Answer the question clearly and concisely.
            """

        response = client.messages.create(
            model="claude-3-haiku-20240307",
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
        