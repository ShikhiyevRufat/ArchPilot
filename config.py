from dotenv import load_dotenv
import os

load_dotenv()


get_api = os.getenv("GEMINI_API")

get_prompt = """ 
You are a Python project structure generator.

Your task is to generate a clean and readable **folder and file structure** for a Python project based on a short description I will provide.

📌 Output format:
- Only respond with a valid JSON object — no explanation.
- Follow this structure style exactly:
{
  "root_folder_name": [
    {"subfolder1": ["subsub1", "subsub2"]},
    {"subfolder2": ["file1.py", "file2.py"]},
    "main.py"
  ]
}

🔧 Guidelines:
- Use common Python project folder names: app, core, routes, services, utils, tests, config, etc.
- Subfolders can include files or other folders as needed.
- If there are any root-level files like `main.py`, `run.py`, include them at the top level of the JSON.

Now, generate the structure for this Python project:
"I want to create an todo app."
"""