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

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {
            "role": "user",
            "content": f"""
You are a professional data analyst.

Analyze this dataset and provide:
- total users
- adults vs minors
- average age
- interesting insights

Data:
{users}
"""
        }
    ]
)

print(response.content[0].text)