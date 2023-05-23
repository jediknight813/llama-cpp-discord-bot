from dotenv import load_dotenv
load_dotenv()
import os


discord_bot_token = os.getenv('discord_bot_token')
llm_model_path = os.getenv('llm_model_path')
max_tokens = os.getenv('max_tokens')

bot_personality = os.getenv('bot_personality')
bot_name = os.getenv('bot_name')
bot_image = os.getenv('bot_image')

# leave empty for if you want to be able to talk to it from any channel.
bot_allowed_channels = []

# leave empty for if you want anyone to be able to use commands.
bot_allowed_command_roles = []

# this will set what will stop the text generation.
stop_text_generation_on = ["###"]

# A penalty applied to each token that is already generated. This helps prevent the model from repeating itself.
# minimum: 0  default: 1.1
bot_repeat_penalty = 1.1

# this will set chat history limit, the question and response.
chat_history_limit = os.getenv('chat_history_limit')
