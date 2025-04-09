from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')
    #return 'Hello, Flask!'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    # TODO: Replace with AI chatbot logic
    response = f"You said: {user_message}. How can I assist further?"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
