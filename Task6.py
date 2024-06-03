import xmltodict

def load_xml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = xmltodict.parse(file.read())
        return data
    except Exception:
        print("Invalid XML format.")
        sys.exit(1)

data = load_xml(input_file)
