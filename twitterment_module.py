import tweepy
from textblob import TextBlob
import pandas as pd

tweets = []

def perform_analysis(text):
    global tweets
    tweets = []
    sentiments = []
    polarities = []
    subjectivities = []
    try:
        get_tweets(text)
        print("Tweets retrieval successful")
    except:
        print("Tweets retrieval unsuccessful")
        if not tweets:
            return ["Tweets retrieval unsuccessful", False,0]
    for tweet in tweets:
        tb = TextBlob(str(tweet))
        print(tb.sentiment)
        polarities.append(tb.sentiment.polarity)    
        subjectivities.append(tb.sentiment.subjectivity)
        # set sentiment
        if tb.sentiment.polarity >= 0.05:
            sentiments.append('positive')
        elif tb.sentiment.polarity <= -0.05:
            sentiments.append('negative')
        else:
            sentiments.append('neutral')
    #Defining Pandas DataFrame with all the above lists
    tdf = pd.DataFrame({'Tweet' : tweets, 'Sentiment' : sentiments, 'Polarity' : polarities, 'Subjectivity' : subjectivities}, columns = ['Tweet','Sentiment','Polarity','Subjectivity'])
    analysis = "Sentiment Analysis on #" + text + " tweets : \n"
    analysis += "Total Tweets : " + str(len(tweets)) + "\n"
    analysis += "Average Polarity : " + str(sum(polarities)/len(polarities)) + "\n"
    analysis += "Average Subjectivity: " + str(sum(subjectivities)/len(subjectivities)) + "\n"
    if (sum(polarities)/len(polarities) > 0.05):
        analysis += "Overall Sentiment : Positive"
    elif (sum(polarities)/len(polarities) < -0.05):
        analysis += "Overall Sentiment : Negative"
    else:
        analysis += "Overall Sentiment : Neutral"
        
    return [analysis, True,tdf]

def generateCSV(rdf,file):
    rdf.to_csv(file, index=False)
    print ("Successfully Generated")

def get_tweets(text):
    
    value = ""
    # Authenticate NipunRamagiri Credentials to use API
    consumer_key= 'nfy8PO4EUBlOyZoxWvBlZRrgU'
    consumer_secret= 'mI14XXCYzfyY3123jnSUlsuMAMD2eFAMbNBJV4TbAM1HFSebut'

    access_token='884661639915593728-GTr6tsa1qFqQM6hv3zZUN9BqMjfYEUx'
    access_token_secret='Xik1JSoKAtHjRwVKRRbORQ7lZUKpOeQg4s3HmETFbwIkd'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Retrieve Tweets
    public_tweets = api.search(text,count=15)
    
    global tweets

    for tweet in public_tweets:
        print(tweet.text)
        tweets.append(str(tweet.text))

