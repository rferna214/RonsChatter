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

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""

    if request.method == "POST":
        question = request.form["question"]



        chat_history.append({"role": "user", "content": question})
        system_prompt = f"""
            You are an AI data assistant.

            Rules:
            - Use ONLY the dataset
            - Be concise
            - No long explanations
            - No mentioning being an AI

            Dataset:
            {users}
            """
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            messages  = [
                {"role": "user", "content": system_prompt}
            ] + chat_history
        )

       

        answer = response.content[0].text

        chat_history.append({"role": "assistant", "content": answer})
        if "clear" in request.form:
            chat_history.clear()
            return render_template("index.html", chat=chat_history)

    return render_template("index.html", chat=chat_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
        