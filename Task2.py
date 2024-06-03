import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        sys.exit(1)

data = load_json(input_file)
