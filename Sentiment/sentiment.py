import json
import textblob

# returns average polarity of 
def calculateSentiment(feed):	
	out = [0.0, 0.0]
	
	for text in feed:
		blob = textblob.TextBlob(text['text'])
		currentSentiment = blob.sentiment

		out[0] += currentSentiment[0]
		out[1] += currentSentiment[1]

	out[0] /= len(feed)
	out[1] /= len(feed)

	return {
		'sentiment' : out[0],
		'signifigance' : out[1]
	}
