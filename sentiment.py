import recent as r
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import preprocessor as p
import os
import json

def make_list(data):
    list_data = []
    dict_data = json.loads(data.text)
    for i in dict_data['data']:
        list_data.append(i['text'])
    return list_data

def clean_tweet(tweet_list):
    new_list = []
    for tweet in tweet_list:
        new_list.append(p.clean(tweet))
    return new_list

def SentimentAnalysis(tweets):
    pol_list = []
    print("Please wait while the tweets are being analyzed. This will take some time...\n")
    for tweet in tweets:
        blob = TextBlob(tweet,analyzer=NaiveBayesAnalyzer())
        sent = blob.sentiment
        if sent[0]=='pos':
            pol_list.append(1)
        else:
            pol_list.append(0)
    return pol_list

if __name__=="__main__":
    BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
    RecentTweet = r.RecentTweetAPI(BEARER_TOKEN)
    keyword=input("Enter the keyword: ")
    data = RecentTweet.get_tweet(keyword)
    tweet_list = make_list(data)
    clean_list = clean_tweet(tweet_list)
    analysis = SentimentAnalysis(clean_list)
    print("10 tweets were analyzed!\n")
    print(f"{(analysis.count(1)/10)*100}% were in favour!\n")
    print(f"{(analysis.count(0)/10)*100}% were not in favour!\n")
