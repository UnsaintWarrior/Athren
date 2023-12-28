import discord
from config import DEFAULT_MOD_ROLE, DEFAULT_MOD_CHANNEL

async def handle_purge_command(message):
    #Grab the role and channel form the guild
    required_role_name = DEFAULT_MOD_ROLE
    required_role = discord.utils.get(message.guild.roles, name=required_role_name)
    defaultModChannel = DEFAULT_MOD_CHANNEL
    modchannel = discord.utils.get(message.guild.channels, name=defaultModChannel)
    # Check if the author has the required role
    if required_role in message.author.roles:
        try:
            number = int(message.content.split()[1])
            await message.channel.purge(limit=number + 1)
        except (IndexError, ValueError):
            await message.channel.purge(limit=2)
        if modchannel:
            await message.channel.send(f"{message.author.display_name} used the purge command!")
    else:
        await message.channel.send("You do not have permission to use this command!")
        if modchannel:
            await modchannel.send(f"{message.author.display_name} attempted to use the purge command without the required role.")


