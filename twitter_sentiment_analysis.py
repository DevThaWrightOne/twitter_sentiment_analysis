#Following code to authenticate with twitters API is from @llSourcell on github.
import tweepy
from textblob import TextBlob

#Use tweepy to authenticate with twitters API. Following keys have been removed
#because they are unique to my twitter profile. You can get yours at twitter.com
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#CHALLENGE - Retrive tweets based off of users keyword and save to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

#Constants used to determine if a tweet on the subject and if it
#is positive or negative.
positive = 0
subjectivity = 0.4

#Ask user for a keyword and retrive tweets.
keyword = input("Enter a keyword you want to search on twitter: ")
public_tweets = api.search(q = keyword, count = 10)

#Dictonary used to store tweets and sentiment rating
dic = {'Tweet': [], 'Sentiment Rating': []}

#Loop used to gather tweets and sentiment rating
for tweet in public_tweets:
    #If the tweet is related to the keyword add it to the dictionary.
    if TextBlob(tweet.text).sentiment[1] >= subjectivity:
        dic['Tweet'].append(tweet.text)
        
        #Determine if the tweet is positive or negative.
        if TextBlob(tweet.text).sentiment[0] >= positive:
            dic['Sentiment Rating'].append('Positive')
        else:
            dic['Sentiment Rating'].append('Negative')
    
#Write results to a CSV file.
filename = 'tweets.csv'
csv = open(filename, 'w')
columnTitles = ('Tweet, Sentiment Rating\n')
csv.write(columnTitles)

counter = 0
for tweet in dic['Tweet']:
    row = tweet + ',' + dic['Sentiment Rating'][counter] + '\n'
    csv.write(row)

csv.close()
    