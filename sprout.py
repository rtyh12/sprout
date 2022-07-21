import discord
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

TOKEN = os.getenv('TOKEN')
BOT_CLIENT_ID = int(os.getenv('BOT_CLIENT_ID'))

X_AXIS_LABELS = (
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '!@#$%^&*()-=_+/.,:;{}[]<>?~αβγδεζηθικλμνξοπρστυφχψω'
)


class Sprout(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    def add_borders(self, arr):
        max_number_width = (len(str(arr.shape[0])), len(str(arr.shape[1])))

        x_axis_numbers = []
        for x in range(arr.shape[0]):
            s = X_AXIS_LABELS[x]
            s += '|-'
            a = np.array(list(s), dtype=np.str_)
            x_axis_numbers.append(a)
        x_axis_numbers = np.stack(x_axis_numbers)

        y_axis_numbers = []
        for x in range(arr.shape[1]):
            s = str(x + 1).rjust(max_number_width[1]) + ": "
            a = np.array(list(s), dtype=np.str_)
            y_axis_numbers.append(a)
        y_axis_numbers = np.stack(y_axis_numbers)

        arr = np.concatenate([x_axis_numbers, arr], axis=1)

        y_axis_numbers = np.rot90(y_axis_numbers)[::-1]

        y_axis_numbers = np.pad(y_axis_numbers,
                                (
                                    (0, 0),
                                    (x_axis_numbers.shape[1], 0),
                                ),
                                'constant',
                                constant_values=(' '))

        print(y_axis_numbers)
        print(arr)

        arr = np.concatenate([y_axis_numbers, arr], axis=0)

        return arr

    def array_to_string(self, arr):
        out = '```'

        for y in reversed(range(arr.shape[1])):
            for x in range(arr.shape[0]):
                out += arr[x, y]
            out += '\n'

        out += '```'

        return out

    def render(self):
        size = (100, 15)
        out = np.zeros(size, np.str_)
        for x in range(size[0]):
            col = np.zeros(size[1], np.str_)
            plant_height = 5
            col[:plant_height] = '|'
            col[plant_height:] = '-'
            out[x, :] = col
        return self.array_to_string(self.add_borders(out))

    async def on_message(self, message):
        if (message.author.id == BOT_CLIENT_ID):
            return
        print(f'Message from {message.author}: {message.content}')
        message = await self.get_channel(message.channel.id).send(self.render())
        await message.add_reaction(emoji="🌱")

    async def on_raw_reaction_add(self, payload):
        print(payload)

    async def on_raw_reaction_remove(self, payload):
        print(payload)


client = Sprout()
client.run(TOKEN)
