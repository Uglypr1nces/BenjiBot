import sys
import time
from benjibot.bot import run_discord_bot
from benjibot.variables.secretkey import *
from utils.waitinganimation import waiting_animation

if not check_key():
    secretkey = input("Please enter your bot token: ")
    save_key_to_file(secretkey)
    waiting_animation(5)
    print("\nKey has been set successfully!")
    print("Starting the bot...")
    waiting_animation(5)
    run_discord_bot(secretkey)
else:
    print("Starting the bot...")
    waiting_animation(5)
    run_discord_bot(load_key())
