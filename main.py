from twitter import *
import os
import readline
import io

MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
# Make it secure for each user
CONSUMER_CREDS = [line.strip() for line in open(os.path.expanduser('~/.consumer_creds'))]
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("jernPi", CONSUMER_CREDS[0], CONSUMER_CREDS[1],
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

t = Twitter(auth=OAuth(
    oauth_token, oauth_secret, CONSUMER_CREDS[0], CONSUMER_CREDS[1]))

# Updates your status
while True:
	tweet = str(raw_input("Enter tweet:"))
	log = io.open("/var/log/auth.log")
	lines = log.read()
	lines = [l for l in lines if "ssh" in l]
	if tweet.strip().upper() != 'EXIT':
		t.statuses.update(status=tweet)
		print "Tweet successful"
	else:
		break
