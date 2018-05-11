# Sentiment analysis

1. Please set up google-home-notifier-interface

* https://github.com/lethe2211/google-home-notifier-interface

2. Set up

```
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/<google cloud platform service account key>

pip install --upgrade flask
pip install --upgrade google-cloud-language
```

3. Execute this program

```
python3 sentiment_analysis.py
```

3. Send an HTTP POST request

```
curl -v -XPOST -H "Content-Type: application/json" -d '{"data": "<Text to be analyzed>"}' http://localhost:5000/
```
