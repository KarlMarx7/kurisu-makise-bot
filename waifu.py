import discord
from discord.ext import commands
import asyncio
#from .opus_loader import load_opus_lib
from discord import opus
import youtube_dl

songQueue = []

bot = commands.Bot(description="The best waifu", command_prefix = (";", "Kurisu, ", "kurisu, "))


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='with Space Time'))
    server = bot.get_server("328798170027130880")
    await bot.send_message(bot.get_channel("328798170027130880"), "I'm online")
    print("Online")

@bot.command()
async def ping():
    await bot.say("W-What?")


@bot.command(pass_context = True)
async def say(ctx, *something):
    something = ' '.join(something)
    if ctx.message.author.id == "325940797893509120":
        await bot.delete_message(ctx.message)
        return await bot.say(something)
    else:
        await bot.say("Who said you could say that to me idiot?")
        await bot.say("I'm not just an object you use. I'm a person")

class Music():
    @bot.command(pass_context = True)
    async def join(ctx):
        channel = None
        author = ctx.message.author
        channel = author.voice_channel
        if channel == None:
            await bot.say("You have to be in a voice channel first (;join), isn't this basic knowledge. Honestly.")
        else:
            await bot.say("I joined a voice channel")
            await bot.join_voice_channel(channel)
    
    @bot.command(pass_context = True)
    async def leave(ctx):
        channel = None
        channel = ctx.message.author.voice_channel
        if channel == None:
            await bot.say("I have to be in a voice channel before disconnecting me")
        else:
            channel.disconnect()


    @bot.command(pass_context = True)
    async def play(ctx, url):
        author = ctx.message.author
        server = author.server
        voice_channel = None
        voice_channel = author.voice_channel
        if bot.is_voice_connected(server) == False:
            vc = await bot.join_voice_channel(voice_channel)
            player = await vc.create_ytdl_player(url)
            player.start()

        if bot.is_voice_connected(server) == True:
            if voice_channel == None:
                await bot.say("You have to be in a voice channel first (;join), isn't this basic knowledge. Honestly.")
            else:
                if not songQueue:
                    vc = bot.voice_client_in(server)
                    songQueue.append(url)
                    nextSong = songQueue(0)
                    player = await vc.create_ytdl_player(nextSong)
                    player.start()
                    while player.is_playing() == False:
                        if not songQueue:
                            bot.say("The queue is empty")
                        else:
                            songQueue.pop(0)
                            nextSong = songQueue(0)
                            vc.create_ytdl_player(nextSong)
                            player.start()


                else:
                    await bot.say("Adding your song to the queue")
                    printSongQueue = ''.join(songQueue)
                    songQueue.append(url)


    @bot.command(pass_context = True)
    async def pause(ctx):
        if player.is_playing() == True:
            player.pause()
        if player.is_playing() == False:
            await bot.say("I have to be playing a song first")
    
    @bot.command(pass_context = True)
    async def queue(ctx):
        if not songQueue:
            bot.say("The queue is empty")
        else:
            for x in songQueue:
                print("hi")
            printSongQueue = ''.join(songQueue)
            await bot.say(songQueue)
        



bot.run('process.env.BOT_TOKEN')
