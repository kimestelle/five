from flask import Flask, jsonify, request
from flask_cors import CORS
import random
from get_next_word import get_next_word

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/next_word', methods=['POST'])
def next_word():
    letters = request.json.get('letters')
    word = get_next_word(letters)
    return jsonify({'word': word})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run(port=5001, debug=True)