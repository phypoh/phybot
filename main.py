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
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    
@bot.command()
async def hello():    
    await bot.say("Hola. :wave: ")
  
    
@bot.command()
async def rn():    
    emoji = bot.get_emoji(440727873196916737)
    await bot.say("Right now!")
    await bot.say(emoji)
    
    
#==============================================================================
# @bot.command()
# async def rn():    
#     await bot.say("Don't quit! <:440727873196916737:> ")
#==============================================================================

#==============================================================================
# @bot.listen
# async def on_message(message):
#     if message.content.endswith('rn'):
#         await bot.say('Right now! :rn:')
#     await bot.process_commands(message)
#         
#==============================================================================
#==============================================================================
# @asyncio.coroutine
# def on_message(self, message):
#     if "rn" in message:
#         await self.bot.say("Right now! <:rn:> ")
#==============================================================================
    
bot.run(os.getenv('BOT_TOKEN'))
