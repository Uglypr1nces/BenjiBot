import os
import time
import discord
from discord.ext import commands
from benjibot.variables.secretkey import botsecretkey
from benjibot.responses import handle_response
from benjibot.tictactoe.game import Game
from benjibot.variables.insults import get_bot_insult
from benjibot.variables.insults import get_emoji_insult
import pdb

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
game = Game()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    is_private = False
    if username == "sleepygirl#4817":
        await message.author.send(get_bot_insult()) if is_private else await message.channel.send(get_bot_insult())
    if "🙂" in user_message:
        await message.author.send(get_emoji_insult()) if is_private else await message.channel.send(get_emoji_insult())
    if user_message.startswith('!'):
        user_message = user_message[1:]
        await send_message(message, user_message, username, False)
    print(f'{username} said: {str(message.content)} in {channel}')


async def send_message(message, user_message, username, is_private):
    try:
        if user_message == "TTT_Start":
            game.gameon = True
            await message.author.send("Game Started, you are playing as X") if is_private else await message.channel.send("Game Started, you are playing as X")
            await message.author.send(game.print_board()) if is_private else await message.channel.send(game.print_board())
        elif "." in user_message:
            choices = user_message.split(".")
            row, index = choices[0], choices[1]
            row, index = int(row), int(index) + 1
            if row < 1 or row > 3 or index < 0 or index > 2:
                await message.author.send("Out of bound, try again") if is_private else await message.channel.send("Out of bound, try again")
            else:
                if not game.check_available_moves(row, index):
                    await message.author.send("Move not available, try again") if is_private else await message.channel.send("Move not available, try again")
                else:
                    await message.author.send("Processing move...") if is_private else await message.channel.send("Processing move...")
                    game.update_board(row, index, "X")
                    await message.author.send(game.print_board()) if is_private else await message.channel.send(game.print_board())
                    await message.author.send("Processing computer move...") if is_private else await message.channel.send("Processing computer move...")
                    time.sleep(1)
                    game.play_move()
                    await message.author.send(game.print_board()) if is_private else await message.channel.send(game.print_board())
                    if game.check_winner() == "X":
                        await message.author.send("https://tenor.com/view/cat-cute-happy-jumping-gif-26555219") if is_private else await message.channel.send("https://tenor.com/view/cat-cute-happy-jumping-gif-26555219")
                        game.reset_board()
                    elif game.check_winner() == "O":
                        await message.author.send("https://tenor.com/view/deadpool-gif-26545415") if is_private else await message.channel.send("https://tenor.com/view/deadpool-gif-26545415")
                        game.reset_board()
        elif user_message == "TTT_End":
            game.gameon = False
            game.reset_board()
            await message.author.send("Game Ended") if is_private else await message.channel.send("Game Ended")
        else:  
            response = handle_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        response = "I'm sorry, I encountered an error: " + str(e)
        await message.channel.send(response)

def run_discord_bot(secretkey):
    TOKEN = secretkey
    bot.run(TOKEN)

