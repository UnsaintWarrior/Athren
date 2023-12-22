#import libraries
import os
import discord

#imports command code
from athren_purge import handle_purge_command
from athren_quotes import handle_quote_command

#define variables
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = os.environ['token']

#DEGUB
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  await client.change_presence(activity=discord.Game(name="Embracing the shadows"))

#Command handlers
@client.event
async def on_message(message):
    if message.content.startswith('$rm'):
        await handle_purge_command(client, message)

    if message.content.startswith('$inspire'):
        await handle_quote_command(client, message)
 
client.run(token)