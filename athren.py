#import libraries
import os
import time
import discord
from dotenv import load_dotenv
from discord.utils import get

from athren_purge import handle_purge_command
from athren_quotes import handle_quote_command
from athren_wizard import handles_setup_command
from athren_join import handle_memberjoin

#Load enviroment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

#Bot permissions
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#Global variables
client = discord.Client(intents=intents)
activity = ('Playing in the shadows.')
defaultsleeptime = 2

#Initialization
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(activity=discord.CustomActivity(name=activity))
    time.sleep(defaultsleeptime)
    print("Initializing checks")

    # Run the checks for each guild the bot is in
    for guild in client.guilds:
        all_checks_passed = await checks(guild)
        if all_checks_passed:
            print(f"Initialization complete, no errors found for {client.user}")
        else:
            print(f"Initialization checks failed for {guild.name}")

    async def checks(guild):
        # Flags for each check
        role_exists = True
        category_exists = True

        # Check for role existence
        existing_role = get(guild.roles, name="Athren.Mod")
        if not existing_role:
            print("Athren.Mod role doesn't exist")
            role_exists = False  # Set flag to False if the role doesn't exist

        # Check for category existence
        existing_categories = get(guild.categories, name="athren-logs")
        if not existing_categories:
            print("Missing Athren-Logs category, probably missing channels too")
            category_exists = False  # Set flag to False if the category doesn't exist

        # Return True if all checks passed
        return role_exists and category_exists

#Command handlers
@client.event
async def on_message(message):
    if message.content.startswith('$setup'):
        await handles_setup_command(client, message)

async def on_member_join(member):
     await handle_memberjoin(member)

async def on_message(message):
    #Call for athren_purge.py
    if message.content.startswith('$rm'):
        print('purge_command')
        await handle_purge_command(client, message)
    #Call for athren_quotes.py
    if message.content.startswith('$inspire'):
        print('quote_command')
        await handle_quote_command(client, message)
     

client.run(os.environ['token'])