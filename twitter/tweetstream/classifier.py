import nltk
import csv



# read all tweets and labels
fp = open( 'sentiment.csv', 'rb' )
reader = csv.reader( fp, delimiter=',', quotechar='"', escapechar='\\' )
tweets = []
for row in reader:
    tweets.append( [row[4], row[1]] );


# treat neutral and irrelevant the same
for t in tweets:
    if t[1] == 'irrelevant':
        t[1] = 'neutral'


def get_words(tweet_text):
    words = []
    
    for (text, sentiment) in tweet_text:
        words.extend(text)
    return words

def get_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

filtered_tweets = []
for (words, sentiment) in tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    filtered_tweets.append((words_filtered, sentiment))


word_features = get_features(get_words(filtered_tweets))
training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

#tweet = tweet from database
#print classifier.classify(extract_features(tweet.split()))
