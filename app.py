from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
current_message = "Hello from Flask!"

@app.route('/')
def index():
    return "API is live"

@app.route('/get')
def get_message():
    # Formats the current time (e.g., 18:38:26)
    timestamp = datetime.now().strftime("%H:%M:%S")
    return f"[{timestamp}] {current_message}"

@app.route('/set')
def set_message():
    global current_message
    message = request.args.get('message')
    if message:
        current_message = message
        return "Message set!"
    return "No message", 400
