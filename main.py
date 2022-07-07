import os
import sys
from sys import platform
from ansi_print import *
from api import *

# TODO: Wrap this in a class to avoid explicitly passing 'bot' into every method.
def announce_twitch(bot: Goof, description: str):
    bot.tweet(f"Live on Twitch, {description}\nhttps://twitch.tv/{bot.twitch}")
def announce_youtube_video(bot: Goof, description: str, url: str):
    bot.tweet(f"New video, {description}\n{url}")
def announce_youtube_stream(bot: Goof, description: str):
    bot.tweet(f"Live on YouTube, {description}\nhttps://youtube.com/{bot.youtube}/live")
def tweet(bot: Goof, contents: str):
    bot.tweet(contents)
def tweet_media(bot: Goof, path: str, contents: str):
    bot.upload_file(path, contents)
CLR_CMD = "cls" if platform == "win32" else "clear"

def hard_break(condition: bool, message: str):
    os.system(CLR_CMD)
    if not condition:
        print_error("HARD BREAK\n-----------------------------------\n'" + message + "'\n-----------------------------------\nStop.")
        sys.exit(1)

BATCH_VALID_ARGV = {
    "--default":"Default execution.",
    "--hb":"Hard-coded breaks enabled for debugging purposes.",
    "--help":"Display help then stop."
}

COMMAND_ARGC = {
    "fetch":0,      # fetch     [no args]   N/A
    "tweet":0,      # tweet     [no args]   'Lorem ipsum'
    "tstream":0,    # tstream   [no args]   'Lorem ipsum'
    "ystream":0,    # ystream   [no args]   'Lorem ipsum'
    "video":1,      # video     [URL]       'Lorem ipsum'
    "media":1,      # media     [path]      'Lorem ipsum'
    "quit":0        # quit      [no args]    N/A
}
AUTO_CONFIRM = "-g"

def main():
    ###
    #   Check for arguments.
    ###
    argv = sys.argv
    if len(argv) == 1: argv.append("--default")
    flag = argv[1:][0]
    print_success(argv)
    if not flag.startswith("--"):
        print_error(f"Unsupported argument '{flag}'; flags must start with '--'.")
    elif flag not in BATCH_VALID_ARGV.keys():
        print_error(f"Unrecognized flag '{flag}'")

    if flag == "--help":
        print("** GOOFY APP FLAGS **")
        for i in BATCH_VALID_ARGV.keys():
            print(f"'{i}'{''.join([' ' for j in range(12 - len(i))])} {BATCH_VALID_ARGV[i]}")
        sys.exit(0)

    def wait():
        print_success("Press 'Enter' to continue . . .")
        input()
        os.system(CLR_CMD)

    while True:
        ###
        #   API Initialization.
        ###
        bot = Goof()
        
        ###
        #  APP CODE
        ###
        print("*****************\n*** GOOFY APP ***\n*****************")
        args = input(">>>").split(); 
        cmd_raw = args.pop(0); cmd = cmd_raw.rstrip(AUTO_CONFIRM)
        
        # Check command for errors.
        if cmd not in COMMAND_ARGC.keys():
            print_error(f"'{cmd_raw}' is not a valid command.")
            wait()
            continue
        elif len(args) < COMMAND_ARGC[cmd]:
            print_error("Not enough args.")
            wait()
            continue

        # Once all is valid, generate extra x arguments ...
        cmd_args = [args.pop(0) for i in range(COMMAND_ARGC[cmd])]
        # ... leaving the rest to be the caption.
        contents = ' '.join(args)
        if not cmd_raw.endswith(AUTO_CONFIRM):
            print(f"Command '{cmd}' | Args {cmd_args} | Caption '{contents}'"); 
            consent = input("Confirm with 'go'.\n>>>")
            if consent.lower() != "go":
                print_error("Action cancelled!")
                wait()
                continue

        hard_break(argv[1] != "--hb", BATCH_VALID_ARGV["--hb"])

        match cmd:
            case "fetch":
                os.system(CLR_CMD)
                tweet = bot.get_latest_tweet()
                print_success(f"Latest tweet stats:")
                if tweet.retweeted: print_error("This is a retweet.")
                print(f"\"{tweet.text}\"\nPosted {tweet.created_at}\n")
                print(f"Source      : {tweet.source}")
                print(f"Likes       : {tweet.favorite_count}")
                print(f"Retweets    : {tweet.retweet_count}")
            case "quit":
                sys.exit(0)
            case "tweet":
                tweet(bot, contents)
            case "tstream":
                announce_twitch(bot, contents)
            case "ystream":
                announce_youtube_stream(bot, contents)
            case "media":
                tweet_media(bot, args[0], contents)
        wait()
if __name__ == "__main__":
    main()