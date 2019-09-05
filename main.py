#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:35:25 2018

@author: phypoh
"""

import os 
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    bot.load_extension("apiCog")
    print("apiCog loaded")

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    
@bot.command()
async def hello():    
    await bot.say("Hola. :wave: ")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')



bot.run(os.getenv('BOT_TOKEN'))
