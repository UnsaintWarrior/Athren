import discord

async def handle_memberjoin(member):
    print('member_join')
    role = discord.utils.get(member.guild.roles, name='Member')
    if role:
            await member.add_roles(role)
    else:
            print("The role does not exist")