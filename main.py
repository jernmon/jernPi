from twitter import *
import os

MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("jernPi", "N4rUOi6kTQjTmRdB2Tg", "m8T2mTpRVJtsfp8GxnWl5tuf8xTZUg2S0DoWhqubPzI",
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

t = Twitter(auth=OAuth(
    oauth_token, oauth_secret, "N4rUOi6kTQjTmRdB2Tg", "m8T2mTpRVJtsfp8GxnWl5tuf8xTZUg2S0DoWhqubPzI"))

# Updates your status
t.statuses.update(status="Found out about @sixohsix's sweet Python Twitter Tools. I'm I doing this right?")