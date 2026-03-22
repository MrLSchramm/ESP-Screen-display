from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
# Initialises with a default ID and command
current_payload = f"{datetime.now().strftime('%H%M%S')}_STP"

@app.route('/')
def index():
    return "API is live"

@app.route('/get')
def get_message():
    # Now just returns the stored payload without changing the time
    return current_payload

@app.route('/set')
def set_message():
    global current_payload
    command = request.args.get('message')
    if command:
        # Generate the new ID ONLY when the button is pressed
        timestamp_id = datetime.now().strftime("%H%M%S")
        current_payload = f"{timestamp_id}_{command}"
        return "Command set!"
    return "No command", 400
