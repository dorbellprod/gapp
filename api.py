import sys
import tweepy
import os
from dotenv import load_dotenv
from ansi_print import *
'''
Goofy App
2 modes
   - Send tweets
   - Announce YouTube Videos | YouTube Streams | Twitch Streams
'''
load_dotenv()
try:
   API_KEY = os.getenv("API_KEY")
   API_KEY_SECRET = os.getenv("API_KEY_SECRET")
   ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
   ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
   YT_CHANNEL_ID = os.getenv("YT_CHANNEL_ID")
   TWITCH_USERNAME = os.getenv("TWITCH_USERNAME")
except:
   print_error("Error loading environment variables.")
   sys.exit(1)

# TODO: Rename 'Goof' to something proper
class Goof:
   def __init__(self) -> None:
      try:
         self.authenticate()
      except tweepy.TweepyException as e:
         print_error("Twitter API error:", e)
         sys.exit(1)
   def authenticate(self):
      self.auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
      self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
      self.api = tweepy.API(self.auth)
      self.id = self.api.verify_credentials().id

      # TODO: Make channel ID and Twitch username optional via value 'none'.
      self.youtube = YT_CHANNEL_ID; self.twitch = TWITCH_USERNAME
   def tweet(self, contents):
      try:
         self.api.update_status(contents)
         print_success("Successfully tweeted!")
      except tweepy.TweepyException as e:
         print_error(f"Error tweeting: {e}")
   
   def get_latest_tweet(self):
      try:
         tweet = self.api.user_timeline(user_id = self.id, count = 1)[0]
         return tweet
      except tweepy.TweepyException as e:
         print_error(f"Error fetching latest tweet: {e}")
   def upload_file(self, path, contents):
      try:
         assert os.path.exists(path), f"'{path}' is not a valid path."
         m = self.api.media_upload(path)
         self.api.update_status(status=contents, media_ids=[m.media_id])
         print_success(f"Successfully uploaded")
      except Exception as e:
         print_error(f"Error uploading media: {e}")