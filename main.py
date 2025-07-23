import google.generativeai as genai
from config import get_api, build_prompt
import subprocess
import argparse
import json
import re

def start():

    parser = argparse.ArgumentParser(description="Generate Python project structure using Gemini AI")
    parser.add_argument("--desc", type=str, required=True, help="Project description (e.g., 'I want to create a todo app')")
    args = parser.parse_args()

    project_description = args.desc
    prompt = build_prompt(project_description)

    genai.configure(api_key=get_api)

    prompt = prompt

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    raw_output = response.text.strip()

    cleaned_json = re.sub(r"^```json|^```|```$", "", raw_output.strip(), flags=re.MULTILINE).strip()

    try:
        json.loads(cleaned_json)  
        subprocess.run(["python", "utilities//get_args.py", "--json", cleaned_json])
    except json.JSONDecodeError as e:
        print("Gemini-dən gələn JSON düzgün deyil:")
        print(raw_output)

if __name__ == "__main__":
    start()
