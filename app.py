from flask import Flask, request

app = Flask(__name__)
current_message = "Hello from Flask!"

@app.route('/')
def index():
    return "API is live"

@app.route('/get')
def get_message():
    return current_message

@app.route('/set')
def set_message():
    global current_message
    message = request.args.get('message')
    if message:
        current_message = message
        return "Message set!"
    return "No message", 400
