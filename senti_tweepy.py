#!/usr/bin/python3

#to consume Twitter's API
import tweepy
#to handle data
import pandas as pd
#for number computing
import numpy as np
import request

#for plotting and visualization
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

import speech_recognition as sr 
import pyaudio

# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = 'zumHggorhcsaUjFtZo4cfjf3y'
CONSUMER_SECRET = 'fwtNObwo2SYGgEubW5uV5IWA2nbPhYzTAA4lnNehfP0uKIbE7c'

app_only_auth: True

# Access:
ACCESS_TOKEN  = '897488518074605568-OShUHypCKadYJaP1AHaw3JGojUI7AvU'
ACCESS_SECRET = 'SCPDyAmNbArGYyUU4LJYtAv7kfC5cOsfDnv2vIv84UeOb'

#API's setup:
def twitter_setup():
    '''
    Utility function to setup the Twitter's API
    with our access keys provided.
    '''
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api



r = sr.Recognizer()                                                                                   
with sr.Microphone() as source: 
	r.adjust_for_ambient_noise(source)                                                                       
	print("speak the username of the tweet you want ot extract ...")	
	audio = r.listen(source)  # get audio from the microphone
	print("Done")  

#try:
	text=r.recognize_google(audio,language='En-IN') #google api for hindi
	print("You said .." )
	print(text) #printing your sweet voice  to  text form
	
#except sr.UnknownValueError:
#	print("Could not understand audio")
#except sr.RequestError as e:
#	print("Could not request results; {0}".format(e))



# We create an extractor object:
extractor = twitter_setup()


#tweet_name=input("Enter the username of the tweet you want ot extract:")
# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name=text, count=1000)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

# We print the most recent  tweets:
tweet_num=input("Enter no of tweets you want:")
tweet_num=int(tweet_num)
print(tweet_num ," recent tweets:\n")
for tweet in tweets[:tweet_num]:
    print(tweet.text)
    print()

#we create a pandas dataframe as follows(systematic manner)
data=pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

#we display the first 10 elements of the data frame
display(data.head(20))

'''
# We print info from the first tweet:
print("-----------------------------------------------------------")
print(tweets[0].id)
print(tweets[0].id)
print(tweets[0].created_at)
print(tweets[0].source)
print(tweets[0].favorite_count)
print(tweets[0].retweet_count)
print(tweets[0].geo)
print(tweets[0].coordinates)
print(tweets[0].entities)
#print(dir(tweets[0]))




# We add relevant data:
data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])


# Display of first 20 elements from dataframe:
display(data.head(20))



# We extract the tweet with more FAVs and more RTs:

fav_max = np.max(data['Likes'])
rt_max  = np.max(data['RTs'])

fav = data[data.Likes == fav_max].index[0]
rt  = data[data.RTs == rt_max].index[0]

# Max FAVs:
print("---------------The tweet with more likes is---------------: \n{}".format(data['Tweets'][fav]))
print("Number of likes: {}".format(fav_max))
print("{} characters.\n".format(data['len'][fav]))

# Max RTs:
print("---------------The tweet with more retweets is---------------: \n{}".format(data['Tweets'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))

'''
