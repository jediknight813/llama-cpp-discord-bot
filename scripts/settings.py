discord_bot_token = ''
llm_model_path = './models/'
max_tokens = 100

bot_personality = 'you are a chatbot named llama-bot, and you never fail to answer the users questions with experience and precision.'
bot_name = 'llama-bot'
bot_image = './images/default.png'

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
chat_history_limit = 2