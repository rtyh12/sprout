import discord
import os
from dotenv import load_dotenv
from render import *

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOT_CLIENT_ID = int(os.getenv('BOT_CLIENT_ID'))


class Sprout(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if (message.author.id == BOT_CLIENT_ID):
            return
        print(f'Message from {message.author}: {message.content}')
        message = await self.get_channel(message.channel.id).send(render())
        await message.add_reaction(emoji="🌱")

    async def on_raw_reaction_add(self, payload):
        print(payload)

    async def on_raw_reaction_remove(self, payload):
        print(payload)


client = Sprout()
client.run(TOKEN)
