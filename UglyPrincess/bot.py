import discord
import os
from UglyPrincess.secretkey import secretkey
from discord.ext import commands
from discord import Intents
from UglyPrincess.responses import *

intents = Intents.default()

async def send_message(message, user_message, is_private):
    try:
        respone = responses.handle_response(user_message)
        await message.author.send(respone) if is_private else await message.channel.send(respone)
    except Exception as e:
        response = "I'm sorry, I encountered an error: " + str(e)


def run_discord_bot():
    TOKEN = secretkey

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if user_message.startswith('!'):
            user_message = user_message[1:]
            await send_message(message, user_message, False)
        print(f'{username} said: {str(message.content)} in {channel}')
        
    client.run(TOKEN)