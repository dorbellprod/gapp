# Goofy App
Goofy App is a goofy command line substitute for Twitter that I made for myself. It is __not__ a proper Twitter client.
## Features
Users may Tweet text, optionally with media. Additionally, users may use Goofy App to announce YouTube videos, as well as YouTube and Twitch livestreams.

## Setup
### Dependencies
This app requires [Python](https://python.org) to be installed with [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)).

Once you have both installed, run the following commands to install libraries [python-dotenv]() and [tweepy](https://www.tweepy.org/):
```
pip install python-dotenv
pip install tweepy
```
### Twitter App
1. Login to the [Twitter developer portal](https://apps.twitter.com) with the account you wish to use. If applicable, link and confirm your phone number.
2. Under *Projects & Apps > Standalone Apps*, click "Create App". There is a limit of 10 per account. Save your API Keys.
3. Click your app on the left panel, and set up user authentication settings. Enable OAuth 1.0a along with permissions to read and write. Finally, enter any URL in the required fields and save.
4. Enter your app settings once again. Under *Keys and tokens*, (re)generate your Access Tokens to finalize the permission changes.
5. You are officially pogging!
### Environment Variables
Create a `.env` file in the master directory. With your Twitter app keys ready, enter them next to their respective variable name:
```
API_KEY                 = your_api_key
API_KEY_SECRET          = your_api_key_secret
ACCESS_TOKEN            = your_access_token
ACCESS_TOKEN_SECRET     = your_access_token_secret

YT_CHANNEL_ID           = your_youtube_id
TWITCH_USERNAME         = your_twitch_username
```
If you do not wish to specify a YouTube ID or Twitch username, simply set it to `none`.
## Usage
On Windows, run `./goofy` in the master directory. For a list of flags, run `./goofy --help`.
## Special Thanks
- Thanks to [A Crazy Town](https://github.com/acrazytown) for assisting during the livestreamed development of this silly program.