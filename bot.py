import discord
from discord.ext import commands
import youtube_dl
import requests
import json
from datetime import date


korona_url = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/finnishCoronaData'

client = commands.Bot(command_prefix='.')

kamari_id = 265500255099944980
general_id = 263639196403630083

command_list = ['apua', 'connect', 'leave', 'korona', 'rukatj']

eero_id = 139413260427460608
oma_id = 217704748982206464

players = {}

@client.event
async def on_ready():
    print("Bot is ready")
    
# Eero annoyer
@client.event
async def on_typing(chn, user, when):
    if user.id == eero_id:
        await chn.send("Turpa kii Eero")


# Command lister
@client.command()
async def commands(ctx):
    response = ", ".join(command_list)
    await ctx.send(f'Commands: {response}')


# Test function
@client.command()
async def apua(ctx):
    response = "Lol apua :D"
    await ctx.send(response)


# Bot joins voice
@client.command()
async def connect(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


# Bot leaves voice
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


# RukaTJ counter
@client.command()
async def rukatj(ctx):
    today = str(date.today()).split('-')
    ruka_date = "2020-04-23".split('-')
    tj = 0
    if today[1] == '03':
        tj = 23 + (31 - int(today[2]))
    else:
        tj = 23 - today[2]
    await ctx.send(f'RukaTJ: {tj}')


# WIP music player
@client.command()
async def play(ctx, url):

    guild = ctx.message.guild
    voice_channel = client.voiceState.channel

    player = await voice_channel.create_ytdl_player(url)
    players[guild.id] = player
    player.start()




# @client.command()
# async def skip(ctx):



# COVID cases in Finland
@client.command()
async def korona(ctx):
    korona_json = requests.get(korona_url).json()
    korona_amount = len(korona_json["confirmed"])
    await ctx.send(f'Tapaukset Suomessa: {korona_amount}')


# Eeron tunnistin
@client.event
async def on_member_update(before, after):
    if after.id == eero_id:
        if before.status == discord.Status.offline and after.status == discord.Status.online:
            await client.get_channel(general_id).send('Eero tuli!')

        if before.status == discord.Status.invisible and after.status == discord.Status.online:
            await client.get_channel(general_id).send('Eero oli piilosilla')



client.run('NjkwNTQyOTU4Nzg0ODA2OTUz.XnS8ZQ.iPoaVcRcZkdZFpRDH0Uj_u7Smwo')