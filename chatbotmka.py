from flask import Flask, request
from pymongo import MongoClient
from twilio.twiml.messaging_response import MessagingResponse
import re

app = Flask(_name_)

client = MongoClient("mongodb://localhost:27017")
db = client["Chatbot"]
collection = db["Rule"]

def get_response(user_input):
    for rule in collection.find():
        for pattern in rule['patterns']:
            # Use regex with word boundaries and case-insensitive matching
            if re.search(r'\b' + re.escape(pattern) + r'\b', user_input, re.IGNORECASE):
                # Handle both string and list responses
                response = rule['response']
                if isinstance(response, list):
                    return "\n".join(response)  # Join list elements with newlines
                return response
    return "Maaf, saya belum mengerti pertanyaan Anda."

@app.route("/chatbotmka", methods=["POST"])
def chatbot():
    # Parse Twilio's form data
    data = request.form
    print("Data diterima:", dict(data))  # Debugging: print the incoming form data
    user_input = data.get("Body", "").strip()  # Get the message text from Twilio's 'Body' field
    response_text = get_response(user_input)
    
    # Create a TwiML response for Twilio
    twiml_response = MessagingResponse()
    twiml_response.message(response_text)
    
    return str(twiml_response)

if _name_ == "_main_":
    print("Chatbot Flask server is running on http://localhost:5000")
    app.run(port=5000, debug=True)
