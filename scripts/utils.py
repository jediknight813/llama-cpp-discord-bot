import subprocess 
import openai
from settings import bot_personality, max_tokens, llm_model_path, bot_name, bot_image, stop_text_generation_on, bot_repeat_penalty
import os
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # can be anything
openai.api_base = "http://localhost:8000/v1"


def get_llama_response(question, model_path):
    # using this lets us have an easy queue system for questions.
    print("\n\n### System: "+bot_personality+"\n\n### Instructions:\n"+question+"\n\n### Response:\n",)
    response = openai.Completion.create(
        model=model_path,
        prompt="\n\n### System: "+bot_personality+"\n\n### Instructions:\n"+question+"\n\n### Response:\n",
        max_tokens=max_tokens,
        stop=stop_text_generation_on,
        repeat_penalty=bot_repeat_penalty,

    )

    return response['choices'][0]["text"]


def get_llama_models():
    models = []
    for file in os.listdir('./models'):
        if file.endswith('.bin'):
            models.append(file)

    return models


async def start_up(client):
    # starts up the llama server.
    command = "python3 -m llama_cpp.server --model "+llm_model_path
    subprocess.Popen(command, shell=True)

    # changes the bot name.
    for guild in client.guilds:
        await guild.me.edit(nick=bot_name)

    # sets the bot profile image.
    fp = open(bot_image, 'rb')
    pfp = fp.read()
    await client.user.edit(avatar=pfp)

    # sync the bot commands.
    await client.tree.sync()


# there is probably a better way to do this.
def change_model(model):
    # kill the old llama server
    subprocess.run(['npx', 'kill-port', '8000'])          
    # start the llama server.
    command = "python3 -m llama_cpp.server --model "+model
    subprocess.Popen(command, shell=True)   