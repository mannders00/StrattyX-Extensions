import json
from flask import Flask, render_template, request, url_for, jsonify
import sentiment

app = Flask(__name__)

@app.route('/invoke/realtime', methods = ['POST'])
def rt():
    feed = request.json()['arguments']['Feed']
    return json.dumps({
        'return' : sentiment.calculateSentiment(feed) 
    })
    
@app.route('/invoke/historic', methods = ['POST'])
def tl():
    body = request.json()
    ts = body['ts']
    feed = body['arguments']['Feed']
    
    return json.dumps({
        'timeline': {
            ts : sentiment.calculateSentiment(feed)
        }
    })

# in future could also make a gui or sth so people can test things out
