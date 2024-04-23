import json


with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'a') as csv_file:
    for entry in data[:5]: 
        name = entry['name']
        html_url = entry['html_url']
        updated_at = entry['updated_at']
        visibility = entry['visibility']

        line = f"{name},{html_url},{updated_at},{visibility}\n"

        csv_file.write(line)