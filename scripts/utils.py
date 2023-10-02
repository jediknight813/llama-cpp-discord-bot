import subprocess 
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # can be anything
openai.api_base = "http://localhost:8000/v1"
from settings import max_tokens, stop_text_generation_on, bot_repeat_penalty, chat_history_limit
from tinydb import TinyDB, Query
import json


def get_llama_response(question, model_path, current_bot_personality):
    bot_data = get_bot_data(current_bot_personality)

    # store chat history in a local database.
    chat_history = get_chat_history(current_bot_personality)

    # temp solution to handle chat history, will need to look into a better long term memory solution.
    chat_history_string = ""
    if len(chat_history) >= 1:
        for message_and_response in chat_history:
            chat_history_string += message_and_response["user_message"]
            chat_history_string += message_and_response["bot_message"]

    # using this lets us have an easy queue system for questions.
    response = openai.Completion.create(
        model=model_path,
        prompt="### System: "+bot_data["bot_personality"]+chat_history_string+"\n\n### Instructions:\n"+question+"\n\n### Response:\n",
        max_tokens=max_tokens,
        stop=stop_text_generation_on,
        repeat_penalty=bot_repeat_penalty,
    )

    return response['choices'][0]["text"]


def get_llama_models():
    models = []
    for file in os.listdir('./models'):
        if file.endswith('.ggml'):
            models.append(file)

    return models


def get_bot_personalities():
    personalities = []
    for file in os.listdir('./bot_personalities'):
        if file.endswith('.json'):
            personalities.append(file)

    return personalities


async def start_up(current_model):
    # starts up the llama server.
    command = "python3 -m llama_cpp.server --model "+current_model
    subprocess.Popen(command, shell=True)


# there is probably a better way to do this.
def change_model(model):
    # kill the old llama server
    subprocess.run(['npx', 'kill-port', '8000'])          
    # start the llama server.
    command = "python3 -m llama_cpp.server --model "+model
    subprocess.Popen(command, shell=True)   


# load the bots personality
def get_bot_data(name):
    with open('./bot_personalities/'+name, "r") as json_file:
        data = json.load(json_file) 

    return data


def get_chat_history(current_bot_personality):
    db = TinyDB('./bot_memories/'+current_bot_personality)
    database = db.all()
    if "0" not in database:
        db.insert({'messages': []})

    database = db.all()

    messages = database[0]["messages"]
    if len(messages) > chat_history_limit:
        while len(messages) > chat_history_limit and chat_history_limit != 0:
            messages.pop(0)

    return messages


def add_message(current_bot_personality, message):
    db = TinyDB('./bot_memories/'+current_bot_personality)
    database = db.all()
    database[0]["messages"].append(message)
    db.update({"messages": database[0]["messages"]})


async def set_bot_personality(client, current_bot_personality):

    db = TinyDB("./bot_memories/bot_state.json")
    db.update({'bot_personality': current_bot_personality}) 
    current_bot_personality = db.all()[0]["bot_personality"]
    print(current_bot_personality)
    
    bot_data = get_bot_data(current_bot_personality)
    # changes the bot name.
    for guild in client.guilds:
        await guild.me.edit(nick=bot_data["bot_name"])

    # sets the bot profile image.
    fp = open(bot_data["bot_image"], 'rb')
    pfp = fp.read()
    await client.user.edit(avatar=pfp)

    # sync the bot commands.
    await client.tree.sync()

