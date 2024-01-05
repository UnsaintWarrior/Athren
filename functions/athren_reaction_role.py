import discord

from config import (
    DEFAULT_MOD_CHANNEL,
)

async def handle_reaction_role(reaction, user, member):
     username = member.name
     user_id = member.id
     mod_channel = DEFAULT_MOD_CHANNEL
     message_id = '1166339020079497308'

     print('Reaction added')

     
     