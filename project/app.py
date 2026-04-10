from flask import Flask, render_template, request
from anthropic import Anthropic
import json
import os
from dotenv import load_dotenv

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

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are a strict data analyst.

Only answer using the provided data.
If not found, say "Not found".

Question:
{question}

Data:
{users}
"""

                }
            ]
        )

        response_text = response.content[0].text

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
        