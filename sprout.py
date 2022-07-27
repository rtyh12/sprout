import discord
import os
from dotenv import load_dotenv
from systems.render import render
from game import Game

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOT_CLIENT_ID = int(os.getenv('BOT_CLIENT_ID'))
MOCK = bool(os.getenv('MOCK'))      # comment/comment out MOCK; value doesn't matter
if MOCK:
    print("Mock mode is on")


class Sprout(discord.Client):
    def __init__(self):
        super().__init__()
        self.game = Game()
        self.game.render()
        
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id == BOT_CLIENT_ID:
            return
        print(f'Message from {message.author}: {message.content}')

        if not MOCK:
            message = await self.get_channel(message.channel.id).send(render())
            await message.add_reaction(emoji="🌱")
        else:
            print(render())

    async def on_raw_reaction_add(self, payload):
        print(payload.emoji)

    async def on_raw_reaction_remove(self, payload):
        print("-", payload.emoji)


client = Sprout()
client.run(TOKEN)
