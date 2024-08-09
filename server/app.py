from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from get_next_word import get_next_word

# instantiate the app
app = Flask(__name__, static_folder='../client/dist')
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Serve the frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

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
