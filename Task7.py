def save_xml(data, file_path):
    with open(file_path, 'w') as file:
        xml_str = xmltodict.unparse(data, pretty=True)
        file.write(xml_str)

save_xml(data, output_file)
