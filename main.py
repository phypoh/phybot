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


parameter = {"api_key": os.getenv('API_KEY')}


@bot.command()
async def get(self, input_url):
    request = requests.get('https://na1.api.riotgames.com/' + input_url, parameter)
    await bot.say(request.text)


bot.run(os.getenv('BOT_TOKEN'))
