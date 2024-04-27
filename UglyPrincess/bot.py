import os
import discord
from discord.ext import commands
from UglyPrincess.responses import handle_response
from UglyPrincess.variables.secretkey import secretkey
from UglyPrincess.TicTacToe.game import Game

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

    if user_message.startswith('!'):
        await send_message(message, user_message, False)
    print(f'{username} said: {str(message.content)} in {channel}')


async def send_message(message, user_message, is_private):
    try:
        response = handle_response(user_message)
        if "." in user_message:
            choices = response.split(".")
            row,index = choices[0],choices[1]

            print(row,index)
        else:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        response = "I'm sorry, I encountered an error: " + str(e)
        await message.channel.send(response)


def run_discord_bot():
    TOKEN = secretkey
    bot.run(TOKEN)
