# authors: Ethosa, FriLDD
import discord as ds
from discord.ext import commands

from setting import setting


class Bot(commands.Bot):
    async def on_message(self, msg):
        if msg.content.startswith("/sex"):
            await msg.channel.send(f"sex with {msg.author.mention}")


stupid = Bot(command_prefix=setting["prefix"])

stupid.run(setting["bot_token"])
