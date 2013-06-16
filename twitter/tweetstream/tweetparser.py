import json, os, nltk


path = ''
fileList = os.listdir(path)
keyword = ''
def keyword_search(path):
    
    keyword_tweets = []

    for fileN in fileList:
        f = open(path + '/' + fileN)
        dct = json.load(f)
        text = dct['text']
    
        if keyword in text:
            keyword_tweets.append(fileN)
        f.close()

    return keyword_tweets


def tweet_data(tweetidx):
        f = open(path + '/' + tweetidx)
        dct = json.load(f)
        text = dct['text']
        location = dct['full_name']
        f.close()
    
    return text, location




def tweet_ranker(tweet_text, keyword):
    tokens = nltk.word_tokenize(tweet_text)
    tagged = nltk.pos_tag(tokens)
    tree = nltk.chunk.ne_chunk(tagged)
    tree_string = tree.pprint(tree, margin=70, indent=0, nodesep='', parens='()', quotes=False)
    
    return rank




tweets = keyword_search(path)  

for tweet_id in tweets:
    tweet_text, tweet_location = tweet_data(tweet_id)
    tweet_rank = tweet_ranker(tweet_text)

    
    
  
