import discord
from config import DEFAULT_MOD_ROLE

async def handle_purge_command(message):
    # Hardcode the role name for testing purposes
    required_role_name = DEFAULT_MOD_ROLE
    required_role = discord.utils.get(message.guild.roles, name=required_role_name)
    # Check if the author has the required role
    if required_role and required_role in message.author.roles:
        try:
            number = int(message.content.split()[1])
            await message.channel.purge(limit=number + 1)
        except (IndexError, ValueError):
            await message.channel.purge(limit=2)
    else:
        await message.channel.send("You do not have permission to use this command!")

        modchannel = discord.utils.get(message.guild.channels, name='moderation')
        if modchannel:
            await modchannel.send(f"{message.author.display_name} attempted to use the purge command without the required role.")
