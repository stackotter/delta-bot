import lightbulb
import os

from functools import wraps
from dataclasses import dataclass
from hikari.undefined import UndefinedType, UNDEFINED

def command(bot, name: str, description: str, **kwargs):
    def decorator(func):
        options = []
        wrapped = func
        while isinstance(wrapped, OptionWrappedFunction):
            options.append(wrapped)
            wrapped = wrapped.wrapped

        @lightbulb.command(name, description, **kwargs)
        @lightbulb.implements(lightbulb.SlashCommand)
        @wraps(wrapped)
        async def wrapper(*args, **kwargs):
            await wrapped(*args, **kwargs)

        for option in options:
            wrapper = lightbulb.option(option.name, option.description, **option.kwargs)(wrapper)

        wrapper = bot.command(wrapper)
        return wrapper
    return decorator

@dataclass
class OptionWrappedFunction:
    name: str
    description: str
    kwargs: dict
    wrapped: any

    def __call__(self):
        self.wrapped()

def option(name, description, **kwargs):
    def decorator(func):
        if isinstance(func, lightbulb.CommandLike):
            raise "'option' decorator must be below 'command' decorator"
        return OptionWrappedFunction(name, description, kwargs, func)
    return decorator

def required_env_var(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"Missing environment variable: '{name}'")
        exit(1)
    return value

def optional_env_var(name: str, default=None):
    return os.environ.get(name, default)
