#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sept  5 17:35:25 2019

@author: phypoh
"""

#==============================================================================
# LEAGUE API COMMANDS
#==============================================================================

import discord
from discord.ext import commands
import os
import requests


class apiCog:
    def __init__(self, bot):
        self.bot = bot

        self.parameters = {"api_key": os.getenv('API_KEY')}

    @commands.command()
    async def api(self,):
        await bot.say("API Cog is loaded.")

    @commands.command()
    async def spy(self, input_name: str):
        request = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + input_name,
                               self.parameters)
        await bot.say(request.text)


def setup(bot):
    bot.add_cog(apiCog(bot))