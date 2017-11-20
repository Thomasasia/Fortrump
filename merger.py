import json
from jsonmerge import merge
tweets_json = []
tweets_json.append(json.loads(open('condensed_2009.json','r').read()))

tweets_json.append(json.loads(open('condensed_2010.json','r').read()))
tweets_json.append(json.loads(open('condensed_2011.json','r').read()))
tweets_json.append(json.loads(open('condensed_2012.json','r').read()))
tweets_json.append(json.loads(open('condensed_2013.json','r').read()))
tweets_json.append(json.loads(open('condensed_2014.json','r').read()))
tweets_json.append(json.loads(open('condensed_2015.json','r').read()))
tweets_json.append(json.loads(open('condensed_2016.json','r').read()))
tweets_json.append(json.loads(open('condensed_2017.json','r').read()))

i = 0

tweets = []

for j in tweets_json:
    for jj in j:
        if "http" not in jj['text'] and len(jj['text']) >= 20:
            tweets.append(jj['text'])
            i += 1

csv_file = open('tweets.csv','w')

for t in tweets:
    csv_file.write(t+'\n')

csv_file.close()





print('number of tweets: ',str(i))


