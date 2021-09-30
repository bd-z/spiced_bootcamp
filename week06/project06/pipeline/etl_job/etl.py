#print('hello world')
import pymongo
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
s  = SentimentIntensityAnalyzer()
time.sleep(10)  # seconds should I use 3600 instead 10 here?
#question :Rewrite the Python script to post a message once an hour (for testing, use a #shorter interval).how?


# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb")
# Select the database you want to use withing the MongoDB server
db = client.tweets
# Select the collection of documents you want to use within the MongoDB database
collection = db.tweet_data



from sqlalchemy import create_engine
pg = create_engine('postgresql://pipelinetwitter_ps:12345@postgresdb:5432/pipelinetwitter_ps', echo=True)
pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')


    
    
def extract(colle):
  entries = colle.find()
  return entries

def transform(entries):
  for e in entries:
    text = e['text']
#  score = 1.0  # placeholder value
    sentiment = s.polarity_scores(e['text'])  # assuming your JSON docs have a text field
    print('-------------------')
    print(sentiment)
    print('-------------------')
# replace placeholder from the ETL chapter
    score = sentiment['compound']
  return text , score  

# question: will above line just return one pair of 'text , score'? should we use [].append()?



def load(text, score):
  query1 = "INSERT INTO tweets VALUES (%s, %s);"   # this is the command to insert vales to #the psql table(tweets)
  pg.execute(query1, (text, score))



#load(transform(extract(collection)))

entries = extract(collection)
entries = transform(entries)
load(entries)





query2 = """

SELECT * FROM tweets LIMIT 1;

"""
results = engine.execute(query2)

# question: should use random? otherwise everytime just return the first one?

#pip install pyjokes
#import pyjokes
import requests

webhook_url = "https://hooks.slack.com/services/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"

#joke = pyjokes.get_joke()

data = { "text" : results}
requests.post(url=webhook_url, json = data)


#Question: how to use this block?Go to the block-kit-builder and improve the look and feel of your bot. For example you #can try to add the tweet’s author, profile image or date. Use blocks instead of text in the data dictionary:
        
#data = {'blocks': [{
#            "type": "section",
#            "text": {
#                "type": "mrkdwn",
#                "text": "*Farmhouse Thai Cuisine*"
#            },
#            "accessory": {
#                "type": "image",
#                "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/c7ed05m9lC2EmA3Aruue7A/#o.jpg",
#                "alt_text": "alt text for image"
#            }
#        }]
#}













#Following is from teacher note
#import pymongo

# Establish a connection to the MongoDB server
#client = pymongo.MongoClient("mongodb")

# Select the database you want to use withing the MongoDB server
#db = client.tweet_collector

# Select the collection of documents you want to use withing the MongoDB database
#collection = db.tweets


# followings is from get_tweets.py
#client = pymongo.MongoClient("mongodb")
#db = client.tweets
#collection = db.tweet_data 




#Following is from course materials


#pg = create_engine('postgresql://user:password@host:5432/dbname', echo=True)

#Make sure to insert the same host/username/password/dbname that you specified
 #in docker-compose.yml. The host is the name of the container.



#fllowng is from course materials ETL part. after pgdb created, enter from new terminal
#psql -U myusername -h 0.0.0.0 -p 5555 mydbname
#psql -U pipelinetwitter_ps -h 0.0.0.0 -p 5555 pipelinetwitter_ps


#following is from docker-compose.yml file
#postgresdb:
#    image: postgres
 #   ports:
 #   - "5555:5432"
 #   environment:
  #  - POSTGRES_USER=pipelinetwitter_ps
 #   - POSTGRES_PASSWORD=12345
  #  - POSTGRES_DB=pipelinetwitter_ps
  
  
  
  
  










