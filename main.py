import discord
from discord.ext.commands import Bot as dBot

from dotenv import load_dotenv
from os import getenv

from commands.welcome import Welcome
from commands.urls import Urls

load_dotenv()

class Bot(dBot):
    async def setup_hook(self) -> None:
        await self.add_cog(Urls(bot))
        await self.add_cog(Welcome(bot))
        await self.tree.sync()
        self.remove_command("help")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = Bot(command_prefix = "?", intents = intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Streaming(
        name = "Delta Client",
        url = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
    ))
    print("Delta Bot is ready!")

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    print("Missing 'BOT_TOKEN'")
    exit(1)

bot.run(bot_token)
