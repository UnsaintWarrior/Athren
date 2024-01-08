import discord, random
from discord.ui import Button, View
from config import (
    DEFAULT_MOD_CHANNEL,
    EFFECT_PHRASE_LIST,
    DEFAULT_WELCOME_CHANNEL
)
async def handle_memberjoin(member):
    mod_channel = DEFAULT_MOD_CHANNEL

    # Get the channels based on the config file
    modchannel = discord.utils.get(member.guild.channels, name=mod_channel)
    welcomechannel = discord.utils.get(member.guild.channels, name=DEFAULT_WELCOME_CHANNEL)
    effectphrase = random.choice(EFFECT_PHRASE_LIST)

    async def handle_verification_embed():
        embed = discord.embed(title = 'Verification Captcha',)

    async def handle_verification(member):
        # Create a DM channel
        dm_channel = await member.create_dm()
        # Send a message to the user
        await dm_channel.send('Hi')
    









    async def handle_join_messages():
        #Moderation channel message
        if modchannel:
            await modchannel.send(f"Member joined: {member.nam}, ID: {member.id}")
        else:
            print("Moderation channel not found.")
        #Welcome channel message
        if welcomechannel:
            await welcomechannel.send(f'Member joined! {member.mention} {effectphrase}')
        else:
            print("Welcome channel not found.")

    await handle_verification(member)
    await handle_join_messages()