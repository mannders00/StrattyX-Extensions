import json
from flask import Flask, render_template, request, url_for, jsonify
import sentiment

app = Flask(__name__)

@app.route('/invoke/live', methods = ['POST'])
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
            ts : { 'value' : sentiment.calculateSentiment(feed) }
        }
    })

if __name__ == '__main__':
    app.run(port=5052)


# in future should also make a gui or sth so people can test things out
