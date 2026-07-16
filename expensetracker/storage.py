import json

def load_expenses():
    try:
        with open("expenses.json",'r') as file:
            data = json.load(file)
            return data

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(data):
    data_str = json.dumps(data,indent=4)
    with open("expenses.json","w") as file:
        file.write(data_str)
  

