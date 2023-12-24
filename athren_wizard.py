import discord
from discord.utils import get
from config import ROLES_TO_CREATE

intents = discord.Intents.default()
intents.members = True  # Enable member intent

async def handle_setup_command(message):
    guild = message.guild

    # Check if the command has already been executed
    if all(get(guild.roles, name=role) for role in ROLES_TO_CREATE) and get(guild.categories, name="athren-logs"):
        await message.channel.send("Setup command has already been executed.")
        return  # Early return if setup has already been completed

    # Start setup
    embed = discord.Embed(title="Setting Up Athren", description="Please wait, setting up roles and channels...", color=0x00ff00)
    setup_message = await message.channel.send(embed=embed)

    # Setup roles
    role_feedback = await setup_roles(guild, ROLES_TO_CREATE)

    # Setup channels
    category_feedback = await setup_category(guild)

    # Finalize setup
    embed = discord.Embed(title="Setup Complete", description=f"{role_feedback}\n{category_feedback}", color=0x00ff00)
    await setup_message.edit(embed=embed)

async def setup_roles(guild, role_names):
    feedback_messages = []
    
    for role_name in role_names:
        existing_role = get(guild.roles, name=role_name)
        if not existing_role:
            await guild.create_role(name=role_name)
            feedback_messages.append(f"{role_name} role created!")
        else:
            feedback_messages.append(f"{role_name} role already exists.")
    
    return "\n".join(feedback_messages)

async def setup_category(guild):
    existing_category = get(guild.categories, name="athren-logs")
    if not existing_category:
        category = await guild.create_category("athren-logs")
        await guild.create_text_channel("internal", category=category)
        await guild.create_text_channel("moderation", category=category)
        return "athren-logs category and channels created!"
    else:
        return "athren-logs category already exists."
