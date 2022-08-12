import lightbulb
import logging
import hikari

plugin = lightbulb.Plugin("welcome")

@plugin.listener(hikari.MemberCreateEvent)
async def member_creation_handler(event: hikari.MemberCreateEvent):
    if event.member.is_bot:
        return

    welcome_channel = None
    for channel in await plugin.bot.rest.fetch_guild_channels(event.guild_id):
        if channel.name == "testing":
            welcome_channel = channel
    if not welcome_channel:
        logging.error("Failed to get welcome channel")

    mention = event.member.mention
    message = f"**Welcome** {mention}! I'm **DeltaBot**, the server's official bot. Type `/` to see available commands\n"
    message += "Please support the project by **leaving us a star on GitHub** :star: (<https://github.com/stackotter/delta-client>)\n"
    message += "And if you want to go above and beyond, **please consider sponsoring the project** :heart: (<https://github.com/sponsors/stackotter>)"

    await plugin.bot.rest.create_message(welcome_channel.id, message)

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)
