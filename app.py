import traceback
import telethon
from flask import Flask, jsonify, request
from telethon.sync import TelegramClient
import random
import string
import asyncio

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
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = TelegramClient(generate_random_string(8), api_id, api_hash)
        loop.run_until_complete(client.start(bot_token=bot_token))
        client.disconnect()
        loop.close()
        return jsonify({"status": "The api_id/api_hash combination is correct"})
    except telethon.errors.rpcerrorlist.ApiIdInvalidError:
        return jsonify({"status": "The api_id/api_hash combination is invalid"})
    except Exception as e:
        return jsonify({"status": "The api_id/api_hash combination is correct"})
