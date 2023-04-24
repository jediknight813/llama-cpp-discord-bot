# llama-cpp-discord-bot

This Discord bot is written in Python and uses the Discord.py library, it utilizes the llama-cpp-python bindings to generate responses.

# Installation

Clone the repository: git clone https://github.com/jediknight813/llama-cpp-discord-bot.git
Install the dependencies: pip install -r requirements.txt

Add your discord bot token to the setting.py file.
```python
discord_bot_token = ''  <---
llm_model_path = './models/ggml-vicuna-7b-1.1-q4_0.bin'
max_tokens = 50

bot_personality = 'you are a chatbot named llama-bot, and you never fail to answer the users questions with experience and precision.'
bot_name = 'llama-bot'
bot_image = './images/default.png'

# leave empty for if you want to be able to talk to it from any channel.
bot_allowed_channels = []

# leave empty for if you want anyone to be able to use commands.
bot_allowed_command_roles = []
```

Run the bot: python scripts/main.py
