import discord

async def handle_memberjoin(member):
    username = member.name  # The user's username
    user_id = member.id    # The user's unique ID
    print(f"Member joined: {username}, ID: {user_id}")
    role = discord.utils.get(member.guild.roles, name='Member')
    if role:
            await member.add_roles(role)
    else:
            print("Unable to add main role because it does not exist.")