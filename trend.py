#!/usr/bin/python2.7
# -*- coding: utf-8 -*
from Main import *
import json


WORLD_WOE_ID = 1
US_WOE_ID = 23424977
# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.
def Trends(WOE_ID):
	trends = twitter_api.trends.place(_id=WOE_ID)
	return trends 

def searchForTweet(query_string):
	count = 100
	search_result = twitter_api.search.tweets(q=query_string,count=count)
	return search_result

#trend=Trends(WORLD_WOE_ID)
#trend_json=json.dumps(trend,indent=1)
#print trend_json
#print "---------------\n"
hash="Tunisie"

tweets = json.dumps(searchForTweet(hash),indent=1)	
_file = open('tweets.json','w')
_file.write(tweets)