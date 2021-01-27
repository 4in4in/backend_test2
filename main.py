import json

from bson import json_util
from flask import Flask
from flask import request
from flask import jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('0.0.0.0', 27017)

db = client['testDB']

questionnaries_collection = db['questionnaries']
answers_collection = db['answers']

def insert_document(collection, data):

    return collection.insert_one(data).inserted_id

def find_document(collection, elements, multiple=False):
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)

@app.route("/test_page", methods=["GET"])
def test_page():
    return 'It works, nakonets-to'

@app.route("/get_questionnary", methods=["GET"])
def get_questionnary():
    if not "questionnary_name" in request.args:
        return {"Error": "not questionnary_name argument!"}
    else:
        args = request.args
        questionnary_filename = args["questionnary_name"]
        # questionnary_filename = questionnary_filename + ".json"
        # with open(questionnary_filename, "r", encoding="utf-8") as q:
        #     questionnary = json.load(q)
        doc = find_document(questionnaries_collection, {'name':questionnary_filename})
        questionnary = json.loads(json.dumps(doc, sort_keys=True, indent=4, default=json_util.default))
        return {"response": questionnary}


@app.route("/dump_qustionnary_answers", methods=["POST"])
def dump_qustionnary_answers():
    answers = request.json
    if answers is None:
        return {"Error!": "No answers data!"}
    else:
        questionnary_name = answers.get("questionnary_name")
        qanswers = answers.get("answers")
        print("questionnary name: {}".format(questionnary_name))
        if qanswers is not None:
            # for qnum, answer in qanswers.items():
            #     print("  question number: {}".format(qnum))
            #     print("    answer: {}".format(answer))
            insert_document(answers_collection, answers)
        else:
            return {"Error!": "No enough data!"}
    return {"test": "dumped!"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
