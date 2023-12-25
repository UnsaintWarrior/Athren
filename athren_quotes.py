import requests
import json
from config import REQUESTS_API_LINK

def get_quote():
  response = requests.get(REQUESTS_API_LINK)
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]["a"]
  return (quote)

async def handle_quote_command(message):   
    quote = get_quote()
    await message.delete()
    await message.channel.send(quote)