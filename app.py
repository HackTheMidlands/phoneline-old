import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

NEXMO_NUMBER = "447520647999"

intro_message = """Thank you for calling Hack The Midlands. For our Emergency line press 0. 
For event information press 1. For tickets 2. For sponsorship enquiries press 3. For anything else press 4."""

options = """For our Emergency line press 0. 
For event information press 1. For tickets 2. For sponsorship enquiries press 3. For anything else press 4."""

event_url = "http://056f9b36.ngrok.io/ivr/"

@app.route('/')
def start_call():
    return jsonify([
        {
            'action': 'talk',
            'text': intro_message,
            'voice_name': 'Amy',
            'bargeIn': 'true'
        },
        {
            'action': 'input',
            'maxDigits': 1,
            "eventUrl": [event_url]
        }
    ])

@app.route('/emergency/', methods=['POST'])
def emergency():
    ncco = [
    {
        "action": "talk",
        "text": "One moment, We are finding someone to answer your call",
        "voice_name": "Amy"
    },
    {
        "action": "connect",
        "from": NEXMO_NUMBER,
        "endpoint": [{
            "type": "phone",
            "number": '447751312580'
        }]
    },
    {
        "action": "connect",
        "from": NEXMO_NUMBER,
        "endpoint": [{
            "type": "phone",
            "number": '44751312580'
        }]
    }]
    

@app.route('/sponsorship/')

@app.route('/other/')


@app.route('/ivr/', methods=['POST'])
def ivr():
    inbound = json.loads(request.data)
    print(inbound['dtmf'])
    if inbound['dtmf'] == '0':
        emergency()
    elif inbound['dtmf'] == '1':
        ncco = [
            {
            'action': 'talk',
            'text': 'Event information',
            'voice_name': 'Amy'
            },
        ]
        return jsonify(ncco)
    elif inbound['dtmf'] == '2':
        tickets()
    elif inbound['dtmf'] == '3':
        sponsorship()
    elif inbound['dtmf'] == '4':
        other()

    else:
        ncco = [
            {
                'action': 'talk',
                'text': 'Sorry I did not understand that. Please try again',
                'voice_name': 'Amy'
            },
            {
                'action': 'talk',
                'text': options,
                'voice_name': 'Amy',
                'bargeIn': 'true'
            },
            {
                'action': 'input',
                'maxDigits': 1,
                "eventUrl": [event_url]
            }
        ]

        return jsonify(ncco)
