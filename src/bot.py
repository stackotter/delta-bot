import lightbulb
import hikari
import os

from .env import bot_token

def main():
    intents = hikari.intents.Intents(
        hikari.intents.Intents.GUILD_MEMBERS |
        hikari.intents.Intents.GUILD_MESSAGES
    )

    bot = lightbulb.BotApp(token=bot_token, intents=intents)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    bot.load_extensions_from(f"{dir_path}/commands")

    activity = hikari.Activity(
        name="Delta Client",
        url="https://www.youtube.com/watch?v=xvFZjo5PgG0",
        type=hikari.ActivityType.STREAMING
    )

    bot.run(activity=activity)

if __name__ == "__main__":
    main()
