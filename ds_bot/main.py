# authors: Ethosa, FriLDD
import random
import discord as ds
from discord.ext import commands
from mchains import AMarkovChains

from setting import setting


chains = AMarkovChains()

class Bot(commands.Bot):
    async def on_message(self, msg):
        if msg.content.startswith("/sex"):
            await msg.channel.send(f"sex with {msg.author.mention}")
        elif msg.content.startswith("/g"):
            with open("text.secret", "r", encoding="utf-8") as f:
                content = f.read()
            await chains.to_chains(content)
            try:
                await msg.channel.send(await chains.genstr(random.randint(2, 10)))
            except:
                await msg.channel.send("неизвестная тупая ашыбка пашол нахуй")
        elif not msg.content.startswith("/"):
            with open("text.secret", "a", encoding="utf-8") as f:
                f.write(msg.content + " ")


stupid = Bot(command_prefix=setting["prefix"])



stupid.run(setting["bot_token"])
