import discord
from discord.ext.commands import Cog
from discord.app_commands import command

class Urls(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @command(description = "Gives you the Twitter account to follow for Delta Client news")
    async def twitter(self, ctx):
        embed = discord.Embed(color = discord.Colour.blue(), title = "https://twitter.com/stackotter")
        embed.set_author(name = "Twitter", icon_url = "https://img.icons8.com/color/344/twitter--v1.png")
        await ctx.response.send_message(embed = embed)

    @command(description = "Gives you the GitHub repository URL")
    async def github(self, ctx):
        embed = discord.Embed(color = discord.Colour.dark_gray(), title = "https://github.com/stackotter/delta-client")
        embed.set_author(name = "GitHub", icon_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
        await ctx.response.send_message(embed = embed)

    @command(description = "Gives you the website URL")
    async def website(self, ctx):
        embed = discord.Embed(color = discord.Colour.greyple(), title = "https://deltaclient.app")
        embed.set_author(name = "Website", icon_url = "https://deltaclient.app/favicon@2x.png")
        await ctx.response.send_message(embed = embed)

    @command(description = "Gives you the link to the downloads page")
    async def download(self, ctx):
        embed = discord.Embed(color = discord.Colour.dark_green(), title = "https://deltaclient.app/downloads")
        embed.set_author(name = "Download", icon_url = "https://img.icons8.com/android/344/download.png")
        await ctx.response.send_message(embed = embed)

    @command(description = "Gives you the URL to sponsor Delta Client")
    async def sponsor(self, ctx):
        embed = discord.Embed(color = discord.Colour.red(), title = "https://github.com/sponsors/stackotter")
        embed.set_author(name = "Sponsor", icon_url = "https://img.icons8.com/fluency/344/like.png")
        await ctx.response.send_message(embed = embed)
