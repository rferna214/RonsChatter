from anthropic import Anthropic
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key securely
api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)

with open("users.json", "r") as file:
    users = json.load(file)

while True:
    question = input("\nAsk a question (type 'exit' to quit): ")
    if question.lower() == "exit":
        break

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": f"""
    You are a strict data analyst.

    Only answer using the provided data. 
    make sure to sound very casual when answering.
    If the answer is not in the data, say "Not Found".

    Question:
    {question}

    Data:
    {users}
    """
            }
        ]
    )

    print("\nAI Response:\n")
    print(response.content[0].text)