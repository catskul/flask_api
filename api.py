from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route('/')
def root_api():
    return jsonify( { 'key' : 'value' } )

if __name__ == '__main__':
    app.run()
