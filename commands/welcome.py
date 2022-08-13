import discord
from discord.ext import commands
from os import getenv

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = self.bot.get_channel(int(getenv("WELCOME_CHANNEL")))
        if not welcome_channel:
            print("Failed to get welcome channel")
            return

        message = f"I'm **DeltaBot**, the server's official bot. Type `/` to see available commands.\n"
        message += "Please support the project by **leaving us a star on [GitHub](https://github.com/stackotter/delta-client)** :star:\n"
        message += "If you want to go above and beyond, **please consider [sponsoring](https://github.com/sponsors/stackotter) the project** :heart:"
        embed = discord.Embed(color = discord.Colour.dark_gray())
        embed.add_field(name = "**Welcome!**", value = message)

        await welcome_channel.send(f"{member.mention}", embed = embed)
