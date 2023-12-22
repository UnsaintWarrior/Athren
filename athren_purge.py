async def handle_purge_command(client, message):
  try:
    number = int(message.content.split()[1])
    await message.channel.purge(limit=number + 1)
  except (IndexError, ValueError):
    await message.channel.purge(limit=2)