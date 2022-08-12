import lightbulb
import hikari

from ..util import command, option

plugin = lightbulb.Plugin("urls")

flags = hikari.messages.MessageFlag.SUPPRESS_EMBEDS

@command(plugin, "twitter", "Gives you the Twitter account to follow for Delta Client news")
async def twitter_cmd(ctx: lightbulb.Context):
    await ctx.respond("https://twitter.com/stackotter", flags=flags)

@command(plugin, "github", "Gives you the GitHub repository URL")
async def github_cmd(ctx: lightbulb.Context):
    await ctx.respond("https://github.com/stackotter/delta-client", flags=flags)

@command(plugin, "website", "Gives you the website URL")
async def website_cmd(ctx: lightbulb.Context):
    await ctx.respond("https://deltaclient.app", flags=flags)

@command(plugin, "download", "Gives you the link to the downloads page")
async def download_cmd(ctx: lightbulb.Context):
    await ctx.respond("https://deltaclient.app/downloads", flags=flags)

@command(plugin, "sponsor", "Gives you the URL to sponsor Delta Client")
async def sponsor_cmd(ctx: lightbulb.Context):
    await ctx.respond("https://github.com/sponsors/stackotter", flags=flags)

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)
