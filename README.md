# llama-cpp-discord-bot

This Discord bot is written in Python and uses the Discord.py library, it utilizes the llama-cpp-python bindings to generate responses.

## basic chatbot mode.
```python 
@{botname} question 
```

![Screen Shot 2023-04-24 at 4 34 42 PM](https://user-images.githubusercontent.com/17935336/234122023-23e9c60d-cf4e-4282-ad17-26b25b047c8b.png)

## List All Models Command.
This will list every model in your models folder.
```python 
/list_models 
```

![Screen Shot 2023-04-24 at 4 37 46 PM](https://user-images.githubusercontent.com/17935336/234123323-5c0c6c92-17f1-4ac1-b420-fa08815290e4.png)

## Switch Model Command.
Put the name of the model you want to switch to.
```python 
/change_model {model_name} 
```

![Screen Shot 2023-04-24 at 4 38 16 PM](https://user-images.githubusercontent.com/17935336/234123353-179b632c-809b-412d-9323-391500099623.png)

## Shutdown bot Command.
Shuts down the bot.
```python
/shutdown 
```

![Screen Shot 2023-04-24 at 5 07 20 PM](https://user-images.githubusercontent.com/17935336/234127186-a4cb0ffc-37b5-45fa-92f5-6d608a739685.png)

# Quick Setup

1. Clone this repository:
```bash 
git clone https://github.com/jediknight813/llama-cpp-discord-bot.git 
```
3. Install the dependencies: 
```python
pip install -r requirements.txt
```

3. Set your discord bot token to the settings.py file.
```python
discord_bot_token = '1234'
```
4. Add a llama.cpp compatible model in the models folder.
5. Set the model path in the settings.py file.
```python
llm_model_path = './models/ggml-vicuna-7b-1.1-q4_0.bin'
```
6. Run the bot: 
```python 
scripts/main.py
```

# Using Docker

1. Clone this repository: 
```bash 
git clone https://github.com/jediknight813/llama-cpp-discord-bot.git 
```
4. Set your discord bot token to the settings.py file.
```python
discord_bot_token = '1234'
```
3. Add a llama.cpp compatible model in the models folder.
4. Set the model path in the settings.py file.
```python
llm_model_path = './models/ggml-vicuna-7b-1.1-q4_0.bin'
```

5. Build the container 
```bash 
docker build -t llama-cpp-discord-bot:latest . 
```
7. Run the container 
```bash 
docker run llama-cpp-discord-bot:latest . 
```

# Customization
I've tried to make it as easy as possible to customize the bot the settings.py file.

## Bot Name 
To change the bot name go to the settings.py file and change this to whatever you like.

```python
bot_name = 'llama-bot'
```

## Bot Personality
To change the bot Personality go to the settings.py file and change this to whatever you like, keep in mind that the longer this is the more time it will take for the bot to respond.

```python
bot_personality = 'you are a chatbot named llama-bot, and you never fail to answer the users questions with experience and precision.' 
```

## Bot Profile Picture

Add the image you want for the bot in the images folder, then go to the setting.py folder and change the bot_image path.
```python 
bot_image = './images/default.png' 
```

## bot permissions

If you don't want users without permissions running the bot commands (change model, list_models, shutdown) add the role name to the bot_allowed_channels in the settings.py file.

```python 
bot_allowed_command_roles = ['admin']
```

 If you don't want the bot to reply in every channel on the server, add the channel name to the bot_allowed_channels in the settings.py file.
 
 ```python 
 bot_allowed_channels = ['general]
 ```
