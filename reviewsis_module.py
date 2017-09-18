from textblob import TextBlob
import pandas as pd

def perform_analysis(file):
    
    df = pd.read_csv(file)
    if 'Review Content' in df.columns:
        reviews = df['Review Content']
        sentiments = []
        polarities = []
        subjectivities = []
    else:
        return ["Check CSV File format : Review Content Column is missing", False,0]
    for review in reviews:
        tb = TextBlob(str(review))
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
    rdf = pd.DataFrame({'Review Content' : reviews, 'Sentiment' : sentiments, 'Polarity' : polarities, 'Subjectivity' : subjectivities}, columns = ['Review Content','Sentiment','Polarity','Subjectivity'])
    analysis = "Sentiment Analysis on " + file + " : \n"
    analysis += "Total Reviews : " + str(len(reviews)) + "\n"
    analysis += "Average Polarity : " + str(sum(polarities)/len(polarities)) + "\n"
    analysis += "Average Subjectivity: " + str(sum(subjectivities)/len(subjectivities)) + "\n"
    if (sum(polarities)/len(polarities) > 0.05):
        analysis += "Overall Sentiment : Positive"
    elif (sum(polarities)/len(polarities) < -0.05):
        analysis += "Overall Sentiment : Negative"
    else:
        analysis += "Overall Sentiment : Neutral"

    del df
      
    return [analysis, True,rdf]

def generateCSV(rdf,file):
    rdf.to_csv(file, index=False)
    print ("Successfully Generated")
    
        
        
