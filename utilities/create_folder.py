import os
import json
import argparse

def create_structure(base_path, structure):
    if isinstance(structure, dict):
        for key, value in structure.items():
            current_path = os.path.join(base_path, key)
            if isinstance(value, list):
                os.makedirs(current_path, exist_ok=True)
                create_structure(current_path, value)
            elif isinstance(value, dict):
                os.makedirs(current_path, exist_ok=True)
                create_structure(current_path, value)
            elif isinstance(value, str):
                with open(os.path.join(base_path, value), 'w') as f:
                    pass
    elif isinstance(structure, list):
        for item in structure:
            if isinstance(item, dict):
                create_structure(base_path, item)
            elif isinstance(item, str):
                file_path = os.path.join(base_path, item)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'w') as f:
                    pass

def main():
    parser = argparse.ArgumentParser(description="Folder structure creator")
    parser.add_argument('--json', type=str, required=True)
    args = parser.parse_args()

    base_path = "C:\\Users\\User\\Desktop\\test_app"

    try:
        structure = json.loads(args.json)
    except json.JSONDecodeError as e:
        print(f"JSON format xətası: {e}")
        return

    for root_folder, content in structure.items():
        root_path = os.path.join(base_path, root_folder)
        os.makedirs(root_path, exist_ok=True)
        create_structure(root_path, content)

    print("Struktur uğurla yaradıldı.")

if __name__ == "__main__":
    main()
