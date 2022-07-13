# Goofy App
Goofy App is a goofy command line substitute for Twitter that I made for myself. It is __not__ a proper Twitter client, in that it requires API setup and does not support many standard features. It's just a goofy app.
## FBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOORINGOAuth 1.0a along with permissions to read and write. Finally, enter any URL in the required fields and save.
4. Enter your app settings once again. Under *Keys and tokens*, (re)generate your Access Tokens to finalize the permission changes.
5. You are officially pogging!
### Environment Variables
Create a `.env` file in the master directory. With your Twitter app keys ready, enter each next to its respective variable name:
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
## Planned Features
- [ ] Ability to set up environment variables with commands.
- [ ] `--help` listing program commands as well as flags.
## Special Thanks
- Thanks to [A Crazy Town](https://github.com/acrazytown) for assisting during the livestreamed development of this silly program.
