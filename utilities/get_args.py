import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', type=str, required=True)
    args = parser.parse_args()

    subprocess.run(["python", "utilities//create_folder.py", "--json", args.json])

if __name__ == "__main__":
    main()
