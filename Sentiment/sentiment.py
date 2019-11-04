import json
import textblob

# returns average polarity (sentiment) and subjectivity (significance)
def calculateSentiment(texts):	
	out = [0.0, 0.0]
	
	for text in texts:
		blob = textblob.TextBlob(text['text'])
		currentSentiment = blob.sentiment

		out[0] += currentSentiment[0]
		out[1] += currentSentiment[1]

	out[0] /= len(texts)
	out[1] /= len(texts)

	return {
		'sentiment' : out[0],
		'signifigance' : out[1]
	}
