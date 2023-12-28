#import libraries
import os
import discord
from dotenv import load_dotenv

#import the package functions
from functions import *

from config import (
    PREFIX,
    ACTIVITY_TEXT,
)

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

#Bot permissions
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#Global variables
client = discord.Client(intents=intents)
activity = discord.Game(name=ACTIVITY_TEXT)

#Initialization
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(activity=activity)
    await handle_initialchecks(client)

#Command handlers
@client.event
async def on_member_join(member):
     await handle_memberjoin(member)

@client.event
async def on_member_remove(member):
    await handle_memberleave(member)

@client.event
async def on_message(message):
    # Check if the message is from the bot itself to prevent it from responding to its own messages
    if message.author == client.user:
        return
    # Check if the message starts with the defined prefix and the command name
    if message.content.startswith(f'{PREFIX}rm'):
        print('purge_command')
        await handle_purge_command(message)
    elif message.content.startswith(f'{PREFIX}inspire'):
        print('quote_command')
        await handle_quote_command(message)
    elif message.content.startswith(f'{PREFIX}setup'):
        print('setup_command')
        await handle_setup_command(message)

    # Process other commands as needed

client.run(os.environ['TOKEN'])