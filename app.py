from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
# Initialises with a default format the ESP understands
current_command = "STP"

@app.route('/')
def index():
    return "API is live"

@app.route('/get')
def get_message():
    # Generates a numeric ID based on the current time (e.g., 185201)
    # Then attaches the command: "185201_CW"
    timestamp_id = datetime.now().strftime("%H%M%S")
    return f"{timestamp_id}_{current_command}"

@app.route('/set')
def set_message():
    global current_command
    command = request.args.get('message') # You send "CW" or "CCW"
    if command:
        current_command = command
        return "Command set!"
    return "No command", 400
