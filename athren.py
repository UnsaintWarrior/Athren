#import libraries
import os
import discord
from dotenv import load_dotenv
from athren_purge import handle_purge_command
from athren_quotes import handle_quote_command
from athren_join import handle_memberjoin

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
activity = ('Playing in the shadows.')

#Initialization
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  await client.change_presence(activity=discord.CustomActivity(name=activity))
  for guild in client.guilds:
        # Check if the role exists
        role = discord.utils.get(guild.roles, name="Athren.Mod")
        if not role:
            try:
                # Create the role if it doesn't exist
                await guild.create_role(name="Athren.Mod")
                print(f'Created role "Athren.Mod" in {guild.name}')
            except discord.Forbidden:
                print(f"I don't have permissions to create roles in {guild.name}")
            except discord.HTTPException:
                print(f"Failed to create role in {guild.name}")
        else:
            print("Initialization complete, No errors found.")
##
            
#Command handlers
@client.event
async def on_member_join(member):
     await handle_memberjoin(member)

@client.event
async def on_message(message):
    #Call for the Remove Message (purge) code
    if message.content.startswith('$rm'):
        print('purge_command')
        await handle_purge_command(client, message)
    #Call for the Quotes code (use API)
    if message.content.startswith('$inspire'):
        print('quote_command')
        await handle_quote_command(client, message)
##     
        
client.run(os.environ['token'])
