import discord
from settings import discord_bot_token, llm_model_path, bot_allowed_channels, bot_allowed_command_roles
from llama_cpp import Llama
from utils import get_llama_response, start_up, get_llama_models, change_model
from discord.ext import commands


llm = Llama(model_path=llm_model_path)
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
current_model = llm_model_path


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await start_up(client)


@client.tree.command(name='shutdown', description='Shut down the bot.')
async def shutdown(interaction: discord.Integration):
    guild = client.get_guild(interaction.guild_id)
    member = guild.get_member(interaction.user.id)

    if bot_allowed_command_roles:
        # If the roles list is not empty, check if the user has any of the roles in the list.
        if not any(role.name in bot_allowed_command_roles for role in member.roles):
            await interaction.response.send_message(content='Sorry, you are not authorized to use this command.')
            return

    await interaction.response.send_message(content='Goodbye.')
    await client.close()


@client.tree.command(name='list_models', description='List available llama models.')
async def list_models(interaction: discord.Integration):
    guild = client.get_guild(interaction.guild_id)
    member = guild.get_member(interaction.user.id)

    if bot_allowed_command_roles:
        # If the roles list is not empty, check if the user has any of the roles in the list.
        if not any(role.name in bot_allowed_command_roles for role in member.roles):
            await interaction.response.send_message(content='Sorry, you are not authorized to use this command.')
            return

    await interaction.response.send_message(content=str('\n'.join(get_llama_models())))


@client.tree.command(name='change_model', description='Change llama model.')
async def list_models(interaction: discord.Integration, model: str):
    guild = client.get_guild(interaction.guild_id)
    member = guild.get_member(interaction.user.id)

    if bot_allowed_command_roles:
        # If the roles list is not empty, check if the user has any of the roles in the list.
        if not any(role.name in bot_allowed_command_roles for role in member.roles):
            await interaction.response.send_message(content='Sorry, you are not authorized to use this command.')
            return

    # check if model exists.
    if model.strip() not in get_llama_models():
        await interaction.response.send_message(content='Incorrect model name.')
        return
    
    change_model('./models/'+model)
    await interaction.response.send_message(content='Swiched model to '+model)


@client.event
async def on_message(server_message):
    # ignore messages sent by the client.
    if server_message.author == client.user:
        return

    # check if client should respond to question.
    allowed_channel = False
    if len(bot_allowed_channels) == 0 or server_message.channel.name in bot_allowed_channels:
        allowed_channel = True

    # make sure the question is addressed to the client and not empty.
    if server_message.content.startswith('<@'+str(client.user.id)+'>') and len(server_message.content.split(' ')) >= 2 and allowed_channel == True:
        await server_message.channel.typing()

        print(current_model)
        # generate the llama model response to the user question.
        output = get_llama_response(server_message.content.replace('<@'+str(client.user.id)+'>', ""), current_model)

        # send llama response to the user.
        await server_message.channel.send(output, reference=server_message)


client.run(discord_bot_token)

