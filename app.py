from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import requests

app = Flask(__name__)

@app.get('/summary')
def summary_api():
    url = request.args.get('url', '')
    summary = requests.get(url)
    return summary.text, 200



if __name__ == '__main__':
    app.run()