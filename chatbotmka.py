from flask import Flask, request
from pymongo import MongoClient
import re

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client["Chatbot"]
collection = db["Rule"]

def pattern_to_regex(pattern):
    # Ubah pattern menjadi regex fleksibel
    words = pattern.lower().split()
    return ".*" + ".*".join(words) + ".*"

def get_response(user_input):
    user_input = user_input.lower()
    for rule in collection.find():
        for pattern in rule['patterns']:
            try:
                regex_pattern = pattern_to_regex(pattern)
                if re.search(regex_pattern, user_input):
                    return rule['response']
            except re.error:
                if pattern.lower() in user_input:
                    return rule['response']
    return "Maaf, saya belum mengerti pertanyaan Anda."

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    print("Data diterima:", data)
    user_input = data.get("message", "")
    response = get_response(user_input)  # Panggil fungsi pencocokan
    return {"response": response}


if __name__ == "__main__":
    print("Chatbot Flask server is running on http://localhost:5000")
    app.run(port=5000, debug=True)
