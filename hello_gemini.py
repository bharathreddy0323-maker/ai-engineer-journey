"""
Hello Gemini — my first AI Engineer project.
Day 1 of the AI Engineer journey.
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-flash-latest")

question = "Explain what an AI Engineer does in 3 sentences."

response = model.generate_content(question)

print("Question:", question)
print()
print("Gemini's answer:")
print(response.text)