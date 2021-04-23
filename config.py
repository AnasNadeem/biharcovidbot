import tweepy
import logging
import os

logger = logging.getLogger()

# API key
# API_KEY="IJBD4l8evXPzw8T20h10UZx5T"
# API Secret Key
# API_SECRET="zLCrGxwTv9zlxgIo62YsIE5RqOdRz8JhZH7q7pI2d2OlywiJUs"
# Bearer Token
# AAAAAAAAAAAAAAAAAAAAACkBOwEAAAAAKrz2PWaRlhfPlwxpbWuBEqIga1M%3DSKUjIfItBrGpm1DTUX6DJFRYAoiGI2ug9gxg4ES0EO515zwGFP
# Access token
# ACCESS_TOKEN="1384451795557052417-248ceoj0xPOncdR4bGwIpO4djydDgk"
# Access token secret
# ACCESS_TOKEN_SECRET="ly26fLVNBy4UpQBWE6K5IFzBFz0f1eg4bSmEyS6XGrf8O"

def create_api():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        # print("Connection OK")
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

# create_api()