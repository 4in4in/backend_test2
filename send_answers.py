import requests


answers = {
    "questionnary_name": "test_questionnary",
    "answers": {
        "1": "10",
        "2": "3",
        "3": "5",
        "4": "1",
        "5": "2",
        "6": "8"
    }
}


url = "http://localhost:5000/api/qustionnaries/dump_qustionnary_answers"
response = requests.post(url, json=answers)
print(response.json())
