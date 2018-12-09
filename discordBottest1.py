import discord
from discord.ext import commands
import discord
from discord import *
import asyncio
from nacl import *
import youtube_dl 

TOKEN = 'NTE5NjI4NzIwODI3MjY5MTgw.DuiIiQ.9mqRo2aU3KZcND9Nr76PCqKH7I8'

client = commands.Bot(command_prefix = ".")
app = discord.Client()




@client.event
async def on_ready(): 
    print("bot is ready")



@client.command(pass_context=True)
async def on_message(message):

     if message.content.startswith("https://www.youtube.com"):
        #msg = "Fuck off {0.author.mention}".format(message)
        #await client.send_message(message.channel, msg)
        global i
        i = message.content
         

     await client.process_commands(message)

on_message()
print(i)


@client.command(pass_context=True)
async def join(ctx):

    channel = ctx.message.author.voice.voice_channel
    vc = await client.join_voice_channel(channel)
    player = await vc.create_ytdl_player(i)
    player.start()
        

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice = client.voice_client_in(server)
    await voice.disconnect()

    


client.run(TOKEN)
app.run(TOKEN)
