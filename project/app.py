from flask import Flask, renter_template, request
from anthropic import Anthropic
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Load user once

with open("user.json", "r") as file:
    user = json.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""

    if request.method == "POST":
        question = request.form["question"]