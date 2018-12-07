import discord
from discord.ext import commands
import discord
from discord import *
import asyncio
from nacl import *
import youtube_dl 

TOKEN = 'NTE5NjI4NzIwODI3MjY5MTgw.DuiIiQ.9mqRo2aU3KZcND9Nr76PCqKH7I8'

client = commands.Bot(command_prefix = ".")



@client.event
async def on_ready(): 
    print("bot is ready")

@client.command(pass_context=True)
async def join(ctx): 
    channel = ctx.message.author.voice.voice_channel
    vc = await client.join_voice_channel(channel)
    player = vc.create_ffmpeg_player("C:/Users/tishel18noaand/Desktop/disbot-master/disbot-master/peg.mp3", after=lambda: print('done'))
    player.start()
        

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice = client.voice_client_in(server)
    await voice.disconnect()




client.run(TOKEN)