import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')
guild = client.get_guild(263639196403630083)
default_text_channel = client.get_channel(263639196403630083)
command_list = ['apua', 'play']

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def commands(ctx):
    response = ", ".join(command_list)
    await ctx.send(f'Commands: {response}')


@client.command()
async def apua(ctx):
    response = "Lol apua :D"
    await ctx.send(response)


@client.event
async def on_member_update(before, after):
    if after.id == 139413260427460608:
        if before.Status == 'offline' and after.Status == 'online':
            default_text_channel.send('Eero tuli!')



client.run('NjkwNTQyOTU4Nzg0ODA2OTUz.XnS8ZQ.iPoaVcRcZkdZFpRDH0Uj_u7Smwo')