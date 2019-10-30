import json
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def calculateSentiment(data):	# data is a JSON file
	text = json.load(data)		# Calculates the average of all the positive sentiments
	out = [0,0]					# and returns them in a list with this format
								# [avg positive, avg negative]
	for i in range(0, len(text)):
		blob = TextBlob(text[i]['text'], analyzer=NaiveBayesAnalyzer())
		currentSentiment = blob.sentiment

		out[0] += float(currentSentiment[1])
		out[1] += float(currentSentiment[2])

	out[0] /= len(text)
	out[1] /= len(text)

	return out

# Anything below this can be deleted, just used example.json for testing
with open("example.json") as json_file:
	print(calculateSentiment(json_file))
