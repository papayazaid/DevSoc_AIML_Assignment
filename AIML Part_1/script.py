import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

MODEL_NAME = "llama-3.3-70b-versatile"

with open("text.txt", "r", encoding="utf-8") as f:
    questions = [line.strip() for line in f if line.strip()]

responses = []
for q in questions:
    print(f"Asking Groq ({MODEL_NAME}): {q}")
    try:
        chat = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": q}],
            timeout=60
        )
        answer = chat.choices[0].message.content
        print(f"Answer: {answer[:200].replace(chr(10), ' ')}...\n")
        responses.append({"question": q, "answer": answer})
    except Exception as e:
        print(f"Error with question '{q}': {e}")
        responses.append({"question": q, "answer": f"Error: {e}"})

with open("responses.json", "w", encoding="utf-8") as out:
    json.dump(responses, out, indent=4, ensure_ascii=False)

print("All Groq responses saved to responses.json")
