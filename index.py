from wsgi import app
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "এপিআই সার্ভার সফলভাবে চলছে!"

@app.route('/api/hello')
def hello():
    return jsonify({"status": "success", "message": "গিটহাব থেকে এপিআই কাজ করছে"})

# ভারসেলের জন্য এটি জরুরি
def handler(event, context):
    return app(event, context)
