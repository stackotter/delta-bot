from dotenv import load_dotenv
from .util import required_env_var

load_dotenv()

bot_token = required_env_var("DELTA_BOT_TOKEN")
