# llama-cpp-discord-bot

This Discord bot is written in Python and uses the Discord.py library, it utilizes the llama-cpp-python bindings to generate responses.

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
