# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oAm3yaZqqoRqJlwysYLMQNznQxRAkC7I

# New Section
"""

!pip install jsonpickle

import tweepy    
import pandas as pd
import re 
import jsonpickle 
import string

CONSUMER_KEY = "......."
CONSUMER_SECRET = "......"
ACCESS_TOKEN = "......."
ACCESS_SECRET = "......."

def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api
 

api = connect_to_twitter_OAuth()

query = 'zero day attack'

max_tweets = 10000

lang= 'en'

tweet_list = []

tweets_collected = tweepy.Cursor(api.search,q=query,lang=lang).items(max_tweets)


for tweet in tweets_collected:         


    tweettosave = jsonpickle.encode(tweet._json, unpicklable=False).encode('utf-8')
    tweet_list.append(tweettosave)

tweet_list

attack_tweets = tweet_list
len(attack_tweets)

def tweets_to_df(tweets):
    ID = []
    text = []  
    weekday = []
    month = []
    day = [] 
    hour = [] 
    hashtag = [] 
    url = [] 
    favorite = []
    reply = [] 
    retweet = []
    follower = [] 
    following = []
    user = []
    screen_name = [] 
    source = []
    in_reply_to_screen_name = [] 
    tweet_hashtags = []
    user_location = []
    for t in tweets:
        t = jsonpickle.decode(t)
        ID.append(t['id'])
        text.append(t['text']) 
        
       
        date = t['created_at']
        weekday.append(date.split(' ')[0])
        month.append(date.split(' ')[1])
        day.append(date.split(' ')[2])
        
        time = date.split(' ')[3].split(':')
        hour.append(time[0]) 
        
        # Has hashtag    
        if len(t['entities']['hashtags']) == 0:            
            hashtag.append(0)
        else:
            hashtag.append(1)
            
        # Has url
        if len(t['entities']['urls']) == 0: 
            url.append(0)
        else:
            url.append(1)
            
        # Number of favs
        favorite.append(t['favorite_count'])
        
        # Is reply?
        if t['in_reply_to_status_id'] == None: 
            reply.append(0)
        else:
            reply.append(1)       
        
        # Retweets count
        retweet.append(t['retweet_count']) 
        
        # Followers number
        follower.append(t['user']['followers_count']) 
        
        # Following number
        following.append(t['user']['friends_count']) 
        
        # Add user
        user.append(t['user']['name'])

        # Add screen name
        screen_name.append(t['user']['screen_name'])
        # Add sourse
        source.append(t['source'])
        in_reply_to_screen_name.append(t['in_reply_to_screen_name'])
                                                                    
        
        newhastags= [] 
        for tweetHashtag in t["entities"]["hashtags"]:    #iterate over the list
            newhastags.append(tweetHashtag["text"])
        tweet_hashtags.append(newhastags)
        
        user_location.append(t["user"]["location"])
        
        
    d = {'id' : ID,
         'text': text,
         'weekday': weekday,
         'month' : month,
         'day': day,
         'hour' : hour,
         'has_hashtag': hashtag,
         'has_url': url,
         'fav_count': favorite,
         'is_reply': reply,
         'retweet_count': retweet,
         'followers': follower,
         'following' : following,
         'user': user,
         'screen_name' : screen_name,
         'source' : source,
         'in_reply_to_screen_name' :in_reply_to_screen_name,
         'tweet_hashtags' : tweet_hashtags,
         'user_location' : user_location
         
        }
    
    return pd.DataFrame(data = d)

tweets = tweets_to_df(attack_tweets)

tweets.head()

tweets.shape

tweets.to_csv('tweets26_zero_day_attack.csv',encoding='utf-8-sig')# Spyware

"""## Merge data to one dataframe

Please note that we collected the data on various days because of the limitation by Twitter API and to ensure that we collect the data in different timestamps. In the following lines we merage the collected data in one dataframe.
"""

df_1 = pd.read_csv('tweets1_Spyware_attack.csv')
df_2 = pd.read_csv('tweets2_ransomware_attack.csv')
df_3 = pd.read_csv('tweets3_viruses_attack.csv')
df_4 = pd.read_csv('tweets4_worms_attack.csv')
df_5 = pd.read_csv('tweets5_macro_viruses_attack.csv')
df_6 = pd.read_csv('tweets6_trojan_attack')
df_7 = pd.read_csv('tweets7_logic_bombs_attack')
df_8 = pd.read_csv('tweets8_malware_breaches')
df_9 = pd.read_csv('tweets9_phishing_attacks')
df_10 = pd.read_csv('tweets10_spear_attack')


df_11 = pd.read_csv('tweets11_MitM_attacks.csv')
df_12 = pd.read_csv('tweets12_session_hijacking.csv')
df_13 = pd.read_csv('tweets13_replay attack.csv')
df_14 = pd.read_csv('tweets14_insider_Threats.csv')
df_15 = pd.read_csv('tweets15_supply_chain_attack.csv')
df_16 = pd.read_csv('tweets16_XSS_attack.csv')
df_17 = pd.read_csv('tweets17_cryptojacking.csv')
df_18 = pd.read_csv('tweets18_Web_Attacks.csv')
df_19 = pd.read_csv('tweets19_Birthday_attack.csv')
df_20 = pd.read_csv('tweets20_DoS_attack.csv')


df_21 = pd.read_csv('tweets21_teardrop_attack.csv')
df_22 = pd.read_csv('tweets22_flood_attack.csv')
df_23 = pd.read_csv('tweets23_SQL_injection_attack.csv')
df_24 = pd.read_csv('tweets24_password_attack.csv')
df_25 = pd.read_csv('tweets25_IOT_attacks.csv')
df_26 = pd.read_csv('tweets26_zero_day_attack.csv')
#df_27 = pd.read_csv('tweets27_Botnet_attack.csv')
#df_28 = pd.read_csv('tweets28_Malware_attack.csv')
#df_29 = pd.read_csv('tweets29_Buffer_overflow_attack.csv')
#df_30 = pd.read_csv('tweets30_Rootkit_attack.csv')

frames = [df_11,df_12,df_13,df_14,df_15,df_16,df_17,df_18,df_19,df_20,df_21,df_22,df_23,df_24,df_25,df_26]#,df_27,df_28,df_29,df_30]
tweets = pd.concat(frames)
del tweets['Unnamed: 0']
tweets.shape

tweets.head()

tweets.text.duplicated().sum()

tweets.id.duplicated().sum()

tweets2 = tweets.drop_duplicates(subset=['id'])
tweets3 = tweets2.drop_duplicates(subset=['text'])

tweets2.shape ,tweets3.shape

tweets3.to_csv('tweets_final.csv',encoding='utf-8-sig',index=False)

tweets_text = tweets3["text"]

tweets_text.head()

tweets_text.to_csv('tweets_text.csv',encoding='utf-8-sig',index=False)

