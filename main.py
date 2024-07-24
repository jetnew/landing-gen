import os
from dotenv import load_dotenv
load_dotenv(override=True)
from openai import OpenAI


with open("prompts/document.txt", "r") as file:
    text = file.read()
    if not text:
        raise Exception("The document.txt file is empty")

with open("prompts/system.txt", "r") as file:
    system = file.read()
    
with open("prompts/format.txt", "r") as file:
    format = file.read()

messages = [
    {"role": "system", "content": system}, 
    {"role": "user", "content": text}, 
    {"role": "system", "content": format}]
    
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
).choices[0].message.content

latest_index = max((int(f.split('_')[1].split('.')[0]) for f in os.listdir("landings/") if f.startswith("landing_") and f.endswith(".md")), default=0)
new_filename = f"landings/landing_{latest_index + 1}.md"

with open(new_filename, "w") as f:
    f.write(response)