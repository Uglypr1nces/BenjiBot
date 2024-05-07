import sys
import time

from UglyPrincess.bot import run_discord_bot
from UglyPrincess.variables.secretkey import check_key, save_key_to_file, botsecretkey

def waiting_animation(wait_time):
    symbols = ['|', '/', '-', '\\']
    while wait_time > 0:
        for symbol in symbols:
            sys.stdout.write(f'\rloading {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)
            wait_time -= 1
    sys.stdout.write('\rDone!     ')
    sys.stdout.flush()

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
    run_discord_bot(botsecretkey)
