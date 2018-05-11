from flask import Flask, request

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import requests
import json

app = Flask(__name__)

client = language.LanguageServiceClient()

@app.route('/', methods=['POST'])
def sentiment_analysis():
    # Expect POST JSON: {'data': '<Text to be analyzed>'}
    body = request.data
    dic = json.loads(body.decode('utf-8'))
    text = dic['data']

    # Analyze sentiment of text
    sentiment = analyze_sentiment(text)
    
    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

    # Make Google Home speak
    response_text = '{0}の分析結果は、スコア{1}です。'.format(text, sentiment.score)
    response = make_google_home_speak(response_text)

    return 'Hello world'

def analyze_sentiment(text):
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return sentiment

def make_google_home_speak(text):
    data = {'text': text}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post('http://localhost:8080/google-home-notifier', data=data, headers=headers)
    return r.text
    
if __name__ == '__main__':
    app.run(debug=True)

