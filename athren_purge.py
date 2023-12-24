async def handle_purge_command(client, message):
  required_role_name = "Athren.Mod"
  if any(role.name == required_role_name for role in message.author.roles):
    try:
      number = int(message.content.split()[1])
      await message.channel.purge(limit=number + 1)
    except (IndexError, ValueError):
      await message.channel.purge(limit=2)
  else:
    await message.channel.send("You do not have permission to use this command!")

    