import discord 
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = self.bot.get_channel(870203284445626418)
        if not welcome_channel:
            print("Failed to get welcome channel")
            return

        message = f"**Welcome** {member.mention}! I'm **DeltaBot**, the server's official bot. Type `/` to see available commands\n"
        message += "Please support the project by **leaving us a star on GitHub** :star: (<https://github.com/stackotter/delta-client>)\n"
        message += "And if you want to go above and beyond, **please consider sponsoring the project** :heart: (<https://github.com/sponsors/stackotter>)"

        await welcome_channel.send(message)