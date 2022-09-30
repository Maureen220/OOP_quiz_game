import requests

url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean"

r = requests.get(url).json()
question_data = r["results"]
