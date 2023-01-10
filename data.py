import requests

params = {
    "amount": 10,
    "category": 9,
    "difficulty": "medium",
    "type": "boolean"
}

url = "https://opentdb.com/api.php"

r = requests.get(url, params=params).json()
question_data = r["results"]
