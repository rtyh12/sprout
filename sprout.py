import discord
import os
from dotenv import load_dotenv

from engine.components.sprite import Sprite
from engine.components.transform import Transform
from engine.components.updateable import Updateable
from engine.game import Game
from scripts.plant_script import PlantScript

load_dotenv()

TOKEN = os.getenv('TOKEN')
client_id = os.getenv('BOT_CLIENT_ID')
if client_id is not None:
    BOT_CLIENT_ID = int(client_id)
MOCK = bool(os.getenv('MOCK'))
if MOCK:
    print("Mock mode is on")


class Sprout(discord.Client):
    def __init__(self):
        super().__init__()
        self.game = Game()

        go_hash = self.game.add_game_object(Transform((5, 5)))
        self.game.add_component(go_hash, Sprite())
        self.game.add_component(go_hash, Updateable())
        self.game.add_component(go_hash, PlantScript())

        self.game.update()
        print(self.game.render())

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id == BOT_CLIENT_ID:
            return
        print(f'Message from {message.author}: {message.content}')

        if not MOCK:
            channel = self.get_channel(message.channel.id)
            if channel is not None:
                message = await channel.send('render()')
            await message.add_reaction(emoji="🌱")
        else:
            # print(render())
            pass

    async def on_raw_reaction_add(self, payload):
        print(payload.emoji)

    async def on_raw_reaction_remove(self, payload):
        print("-", payload.emoji)


client = Sprout()
client.run(TOKEN)
