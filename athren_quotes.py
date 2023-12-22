import requests
import json

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]["a"]
  return (quote)

async def handle_quote_command(client, message):   
    quote = get_quote()
    await message.delete()
    await message.channel.send(quote)