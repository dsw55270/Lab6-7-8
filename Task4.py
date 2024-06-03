import yaml

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError:
        print("Invalid YAML format.")
        sys.exit(1)

data = load_yaml(input_file)
