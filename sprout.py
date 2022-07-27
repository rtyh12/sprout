import discord
import os
from dotenv import load_dotenv
import numpy as np

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


class Sprout(discord.Client):
    def __init__(self):
        super().__init__()
        self.game = Game()

        bg = self.game.add_game_object(Transform((0, 0)))
        bg_sprite = Sprite(np.zeros((100, 100)))
        bg_sprite.arr[:] = ' '
        bg_sprite.arr[:, [5, 10]] = '-'
        bg_sprite.z_index = -100
        self.game.add_component(bg, bg_sprite)

        go_hash = self.game.add_game_object(Transform((5, 5)))
        sprite1 = Sprite(np.zeros((101, 3)) + 4)
        sprite1.center = (12, 0)
        sprite1.z_index = 3
        sprite2 = Sprite(np.zeros((5, 5)) + 8)
        sprite2.z_index = 4
        self.game.add_component(go_hash, sprite1)
        self.game.add_component(go_hash, sprite2)
        # self.game.add_component(go_hash, Updateable())

        plant = self.game.add_game_object(Transform((10, 1)))
        plant_sprite = Sprite(np.array([['x']]))
        plant_sprite.z_index = 10
        self.game.add_component(plant, plant_sprite)
        self.game.add_component(plant, PlantScript())

        self.game.update()
        self.game.update()
        self.game.update()
        print(self.game.render())

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id == BOT_CLIENT_ID:
            return
        print(f'Message from {message.author}: {message.content}')

        channel = self.get_channel(message.channel.id)
        if channel is not None:
            message = await channel.send(self.game.render())
        await message.add_reaction(emoji="🌱")

    async def on_raw_reaction_add(self, payload):
        print(payload.emoji)

    async def on_raw_reaction_remove(self, payload):
        print("-", payload.emoji)


client = Sprout()
client.run(TOKEN)
