import discord
import random
from config import (
    DEFAULT_JOIN_ROLE, 
    DEFAULT_WELCOME_CHANNEL,
    EFFECT_PHRASE_LIST
)

async def handle_memberjoin(member):
    
    username = member.name  # The user's username
    user_id = member.id    # The user's unique ID
 
      # Get the 'moderation' channel object
    modchannel = discord.utils.get(member.guild.channels, name='moderation')
    # Get the welcome channel object based on DEFAULT_WELCOME_CHANNEL from config
    welcomechannel = discord.utils.get(member.guild.channels, name=DEFAULT_WELCOME_CHANNEL)
    effectphrase = random.choice(EFFECT_PHRASE_LIST)


    #DEGUB
    print(f"Member joined: {username}, ID: {user_id}")
    ##

    if modchannel:
        await modchannel.send(f"Member joined: {username}, ID: {user_id}")
    else:
        print("Moderation channel not found.")
    
    if welcomechannel:
        await welcomechannel.send(f'Member joined! {member.mention} {effectphrase}')
    else:
        print("Welcome channel not found.")

    for role_name in DEFAULT_JOIN_ROLE:
        role = discord.utils.get(member.guild.roles, name=role_name)
        if role:
            await member.add_roles(role)
        else:
            print(f"Unable to add {role_name} role because it does not exist.")