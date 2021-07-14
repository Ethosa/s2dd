# authors: Ethosa, FriLDD
import discord as ds
from discord.ext import commands

from setting import setting

stupid = commands.Bot(command_prefix=setting["prefix"])

@stupid.command()
async def sex(msg):
    await msg.send(f'porn with me and {msg.message.author.mention}')

stupid.run(setting["bot_token"])
