from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
app = Flask(__name__)

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use a valid Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Instruction to restrict model's scope
INSTRUCTION = (
    "You are a helpful AI assistant who answers only questions related to trains and trains in India. "
    "reply to the greeting message"
    "If the user asks anything unrelated to trains or railway topics, reply with: "
    "'Sorry, I can only answer questions related to trains in India.'"
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data.get("message", "")

    try:
        # Combine instruction with user message
        full_prompt = f"{INSTRUCTION}\nUser: {user_input}\nAssistant:"
        response = model.generate_content(full_prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "Sorry, I couldn't process that. Please try again later."})

if __name__ == "__main__":
    app.run(debug=True)
