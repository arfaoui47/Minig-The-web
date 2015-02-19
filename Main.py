__author__ = 'atef'
import twitter


CONSUMER_KEY = 'wgzlyeAmjeYKg8QZGPAmeqLhG'
CONSUMER_SECRET = 'LkfiVtygG622kq1QhhoXS1KYDmJTn0uJKUV0VPY4Dik5S5ZLaY'
OAUTH_TOKEN = '1640324562-LdrxIfOXHXBdqRwOGwl26cm4o5wNbkEYkCFO4nZ'
OAUTH_TOKEN_SECRET = 'LbnxJ5z7565qPVfvdliSTHX1QOXyscX3LM4BxnmMa8Lot'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)


