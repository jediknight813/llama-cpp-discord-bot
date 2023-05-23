# llama-cpp-discord-bot

This Discord bot, which is written in Python and uses the Discord.py library, leverages the llama-cpp-python bindings to generate responses. It offers several commands for controlling the bot and interacting with the models it has access to.

llama-cpp-python: https://github.com/abetlen/llama-cpp-python

Discord.py: https://github.com/Rapptz/discord.py

## basic chatbot mode.
```python 
@{botname} question 
```

![Screen Shot 2023-04-24 at 4 34 42 PM](https://user-images.githubusercontent.com/17935336/234122023-23e9c60d-cf4e-4282-ad17-26b25b047c8b.png)

## List All Models Command.
You can list every model in your models folder with the following command:
```python 
/list_models 
```
This will provide you with a list of all the models available to the bot.

![Screen Shot 2023-04-24 at 4 37 46 PM](https://user-images.githubusercontent.com/17935336/234123323-5c0c6c92-17f1-4ac1-b420-fa08815290e4.png)

## Switch Model Command.
To switch to a different model, simply specify the name of the model you want to switch to:
```python 
/change_model {model_name} 
```
This will change the bot's active model.

![Screen Shot 2023-04-24 at 4 38 16 PM](https://user-images.githubusercontent.com/17935336/234123353-179b632c-809b-412d-9323-391500099623.png)

## Shutdown bot Command.
To shut down the bot, use the following command:
```python
/shutdown 
```
This will terminate the bot.

![Screen Shot 2023-04-24 at 5 07 20 PM](https://user-images.githubusercontent.com/17935336/234127186-a4cb0ffc-37b5-45fa-92f5-6d608a739685.png)

## List All Bot Personalities Command.
You can list every personality in your bot_personality folder with the following command:
```python 
/list_personalities
```
This will provide you with a list of all the personalities available to the bot.
![Screen Shot 2023-05-23 at 4 05 43 PM](https://github.com/jediknight813/llama-cpp-discord-bot/assets/17935336/533e7603-e102-4634-9213-965419669332)

## Switch Bot Personality Command.
To switch to a different Personality, simply specify the name of the Personality you want to switch to:
```python 
/change_bot_personality {personality_name} 
```
This will change the bot's active personality.

![Screen Shot 2023-05-23 at 4 15 18 PM](https://github.com/jediknight813/llama-cpp-discord-bot/assets/17935336/5fc2826c-5240-41b1-a2b2-f1f683adac87)

# Quick Setup
To get started quickly, follow these steps:

1. Clone this repository:
```bash 
git clone https://github.com/jediknight813/llama-cpp-discord-bot.git 
```
2. Install the dependencies: 
```python
pip install -r requirements.txt
```
3. Add a llama.cpp compatible model in the models folder.
 
![Screen Shot 2023-04-24 at 5 23 43 PM](https://user-images.githubusercontent.com/17935336/234129631-1667f4a8-2ffd-4303-83a5-d55795b16008.png)

4. Rename the .env.example file to .env.

![Screen Shot 2023-05-23 at 4 11 17 PM](https://github.com/jediknight813/llama-cpp-discord-bot/assets/17935336/6e03b7de-ba62-479e-926e-1907271a56c6)

5. Set your discord bot token and model path in the .env file.
```python
discord_bot_token = '1234'
llm_model_path = './models/ggml-vicuna-7b-1.1-q4_0.bin'
```

6. Run the bot: 
```python 
python scripts/main.py
```

# Using Docker
Make sure you have docker desktop installed and running.

1. Clone this repository: 
```bash 
git clone https://github.com/jediknight813/llama-cpp-discord-bot.git 
```
4. Rename the .env.example file to .env.

![Screen Shot 2023-05-23 at 4 11 17 PM](https://github.com/jediknight813/llama-cpp-discord-bot/assets/17935336/6e03b7de-ba62-479e-926e-1907271a56c6)

3. Add a llama.cpp compatible model in the models folder.

![Screen Shot 2023-04-24 at 5 23 43 PM](https://user-images.githubusercontent.com/17935336/234129495-bfcf34ae-26fb-48c4-af53-9e9383be4fa9.png)

4. Set your discord bot token and model path in the .env file.
```python
discord_bot_token = '1234'
llm_model_path = './models/ggml-vicuna-7b-1.1-q4_0.bin'
```

5. Build the docker image 
```bash 
docker build -t llama-cpp-discord-bot:latest . 
```
6. Run it
```bash 
docker run llama-cpp-discord-bot:latest
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

If you don't want users without permissions running the bot commands (change model, list_models, shutdown) add the role name to the bot_allowed_command_roles in the settings.py file.

```python 
bot_allowed_command_roles = ['admin']
```

 If you don't want the bot to reply in every channel on the server, add the channel name to the bot_allowed_channels in the settings.py file.
 
 ```python 
 bot_allowed_channels = ['general']
 ```
