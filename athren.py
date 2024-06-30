#import libraries
import os
import discord
from dotenv import load_dotenv
from discord.utils import get 

#import rest of the code
from athren_joinleave import handle_memberjoin, handle_memberleave
from athren_checks import handle_initchecks
from athren_purge import handle_purge_command
from athren_quotes import handle_quote_command
from athren_wizard import handle_setup_command


from config import (
    PREFIX,
    ACTIVITY_TEXT,
)

#Load enviroment variables
load_dotenv()

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
    await handle_initchecks(client)

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
        for guild in client.guilds:
            print(f'purge_command {guild.name}')
        await handle_purge_command(message)
    elif message.content.startswith(f'{PREFIX}inspire'):
        for guild in client.guilds:
            print(f'quote_command {guild.name}')
        await handle_quote_command(message)
    elif message.content.startswith(f'{PREFIX}setup'):
        for guild in client.guilds:
            print(f'setup_command {guild.name}')
        await handle_setup_command(message)

    # Process other commands as needed

client.run(os.environ['TOKEN'])