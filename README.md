# llama-cpp-discord-bot

This Discord bot is written in Python and uses the Discord.py library, it utilizes the llama-cpp-python bindings to generate responses.

## basic chatbot mode.
``` @{botname} question ```

![Screen Shot 2023-04-24 at 4 34 42 PM](https://user-images.githubusercontent.com/17935336/234122023-23e9c60d-cf4e-4282-ad17-26b25b047c8b.png)

## list all models command.
This will list every model in your models folder.
``` /list_models ```

![Screen Shot 2023-04-24 at 4 37 46 PM](https://user-images.githubusercontent.com/17935336/234123323-5c0c6c92-17f1-4ac1-b420-fa08815290e4.png)

## switch model command.
Put the name of the model you want to switch to.
``` /change_model {model_name} ```

![Screen Shot 2023-04-24 at 4 38 16 PM](https://user-images.githubusercontent.com/17935336/234123353-179b632c-809b-412d-9323-391500099623.png)

# Quick Setup

1. Clone this repository: ``` git clone https://github.com/jediknight813/llama-cpp-discord-bot.git ```
2. Install the dependencies: ``` pip install -r requirements.txt ```

3. Set your discord bot token to the settings.py file.
```python
discord_bot_token = '1234'
```
4. Add a llama.cpp compatible model in the models folder.
5. Set the model path in the settings.py file.
```python
llm_model_path = './models/ggml-vicuna-7b-1.1-q4_0.bin'
```
6. Run the bot: ```python scripts/main.py ```


# Using Docker

1. Clone this repository: ``` git clone https://github.com/jediknight813/llama-cpp-discord-bot.git ```
2. Set your discord bot token to the settings.py file.
```python
discord_bot_token = '1234'
```
3. Add a llama.cpp compatible model in the models folder.
4. Set the model path in the settings.py file.
```python
llm_model_path = './models/ggml-vicuna-7b-1.1-q4_0.bin'
```

5. Build the container ``` docker build -t llama-cpp-discord-bot:latest . ```
6. Run the container ``` docker run llama-cpp-discord-bot:latest . ```
