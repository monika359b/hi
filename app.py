import traceback
import pyrogram
from flask import Flask, jsonify, request
from pyrogram import Client
import random
import string

app = Flask(__name__)

def generate_random_string(string_length=8):
    """Generate a random string of fixed length """
    letters = string.ascii_letters + string.digits 
    return ''.join(random.choice(letters) for i in range(string_length))

@app.route('/check_api')
def check_api():
    try:
        api_id = request.args.get('api_id')
        api_hash = request.args.get('api_hash')
        bot_token = '5711346303:AAGxyS-o-Aijdfqdhyz5EnwwBcAWkjO74AA'
        client = pyrogram.Client(generate_random_string(8), api_id, api_hash)
        client.run()
        client.stop()
        return jsonify({"message":"Your api keys are valid"})
    except Exception as e:
        traceback.print_exc()
        return("Your api keys are not valid")