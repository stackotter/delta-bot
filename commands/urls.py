import discord 
from discord.ext.commands import Cog
from dislash import slash_command

class Urls(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(description = "Gives you the Twitter account to follow for Delta Client news")
    async def twitter(self, ctx):
        await ctx.send("https://twitter.com/stackotter")

    @slash_command(description = "Gives you the GitHub repository URL")
    async def github(self, ctx):
        await ctx.send("https://github.com/stackotter/delta-client")

    @slash_command(description = "Gives you the website URL")
    async def website(self, ctx):
        await ctx.send("https://deltaclient.app")

    @slash_command(description = "Gives you the link to the downloads page")
    async def download(self, ctx):
        await ctx.send("https://deltaclient.app/downloads")

    @slash_command(description = "Gives you the URL to sponsor Delta Client")
    async def sponsor(self, ctx):
        await ctx.send("https://github.com/sponsors/stackotter")