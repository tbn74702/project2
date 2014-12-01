#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import twitter

import regex_generator
import joke_generator

from datetime import datetime,timedelta
from email.utils import parsedate_tz

from twitter.api import Twitter, TwitterError
from twitter.oauth import OAuth, write_token_file , read_token_file
from twitter.oauth_dance import oauth_dance
from urllib2 import URLError
from httplib import BadStatusLine

def oauth_login():
#enter the corresponding information from your Twitter application:
    CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
    OAUTH_TOKEN = ''#keep the quotes, replace this with your access token
    OAUTH_TOKEN_SECRET = ''#keep the quotes, replace this with your access token secret
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = Twitter(auth=auth)
    return twitter_api
	
#Creates bot login for later use in functions
bot=oauth_login()
	
def to_datetime(datestring):
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])	
	
#Checks if retweet
def is_retweet(tweetid):
    try:
        bot.statuses.show(id=tweetid)['retweeted_status']
    except KeyError:
        retweet=0   #Tweet is not a retweet
    except twitter.TwitterError:
        retweet=1   #Twitter error (counts as a retweet for us)
    else:
        retweet=1   #Tweet is a retweet
    return retweet

#Checks if tweet time is within 3 days
def timediff3(tweetid):
    try:
        tweet_time=bot.statuses.show(id=tweetid)['created_at']
    except twitter.api.TwitterHTTPError:
        a=0   #Considered too old
        print "twitter error"
        pass
    else:
        t=datetime.now() - to_datetime(tweet_time)
        if t < timedelta(3.0,0.0,0.0):
            a=1
        else:
            a=0
    return a
   
#Creates a reply tweet given an id and message to tweet
def reply_id(tweetid,message):
    try:
        speaker=bot.statuses.show(id=tweetid)['user']['screen_name']
        reply = '@%s %s' % (speaker, message)
        bot.statuses.update(status=reply,in_reply_to_status_id=tweetid)
        return 1
    except twitter.api.TwitterHTTPError, e:
        return e.e.code
    else:
        return 0
	
	
if __name__ == "__main__":

	bot_name = 'KidHealthBot' #put your actual bot's name here
	
	patterns=regex_generator.regex_generate('symptoms.txt','synonyms.txt')
	
	#main loop. Just keep searching anyone talking to us
	while True:
		try:
			
			#Searches MongoDB for patterns
			print 'Searching for patterns \n'
			last_id=regex_generator.lastid_read('latest_mongo_id.txt')  #Reads a last_id for last location searched for in mongodb
			t_id=regex_generator.getall_tweet(patterns,last_id)	#Gets all tweets of interest from MongoDB and returns tweet ids as well as the last id marker
			tweetids=t_id[0]		#Grabs only tweet ids from t_id
			
			print 'Done searching for patterns \n'
			
			#Reply to all tweets of interest
			print 'Replying to tweets \n'
			for i in range(len(patterns)):
				for j in range(len(tweetids[i])):
					time.sleep(2)
					#print "finished pause"
					print tweetids[i][j] +' ' + str(is_retweet(tweetids[i][j])) + str(timediff3(tweetids[i][j]))
					
					retweet=is_retweet(tweetids[i][j])
					tim=timediff3(tweetids[i][j])
					try:
						sc_name=str(bot.statuses.show(id=tweetids[i][j])['user']['screen_name'])
					except twitter.api.TwitterHTTPError:
						sc_name='anything' #Passes error along to rest of code
					if retweet==0 and tim==1 and sc_name!=bot_name:
						#print "test"
						joke=joke_generator.tweets_respond(i)
						e_indicator=reply_id(tweetids[i][j],joke)
						if e_indicator in (1,401,404):
							if e_indicator==1:
								print 'Replied to tweet to ' + str(i) + str(j)
								pass
							else:
								print "Failed to reply to " +str(i) + str(j)
								pass
						elif e_indicator in (500, 502, 503, 504):
							for k in range(5):
								time.sleep(3)
								e_indicator=reply_id(tweetids[i][j],joke)
								if e_indicator == 1:
									print 'Replied to tweet to ' + str(i) + str(j)
									k=5
						elif e_indicator == 429:
							print "Rate Limit Exceeded, sleeping 15 minutes"
							time.sleep(905)
							print "Finished Sleeping"
							e_indicator =reply_id(tweetids[i][j],joke)
							if e_indicator !=1:
								print "Failed to reply to " + str(i) + str(j)
								pass
						else:
							pass
					else:
						print "conditions not met"
			print 'Done replying to all tweets. \n'
			
			regex_generator.lastid_write('latest_mongo_id.txt',t_id[1])		#After successfully replying to all tweets, sets the last_id marker for next search
			
			sleep_int = 60*5 #downtime interval in seconds
			print "Sleeping for "+str(sleep_int/60)+" minutes...\n"
			time.sleep(sleep_int)
			
		except KeyboardInterrupt:
			print"[!] Cleaning up. Operation interrupted by user."
			sys.exit()