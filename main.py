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
    
@bot.event
async def on_message(message):
    if "rn" in message.content.split():
        await bot.say("Right now! :rn:")
        
#==============================================================================
# @asyncio.coroutine
# def on_message(self, message):
#     if "rn" in message:
#         await self.bot.say("Right now! <:rn:> ")
#==============================================================================
    
bot.run(os.getenv('BOT_TOKEN'))
