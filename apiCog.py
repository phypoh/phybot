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
        await self.bot.say("API Cog is loaded.")

    @commands.command()
    async def spy(self, input_name: str):
        request = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + input_name,
                               self.parameters)
        summoner_id = request.json()['accountId']

        request = requests.get('https://na1.api.riotgames.com//lol/match/v4/matchlists/by-account/' + summoner_id,
                               self.parameters)
        matches = request.json()['matches']

        output = ''
        i = 0
        for match in matches:
            i += 1
            output += 'Match ' + str(i) + '/n'
            for item in match:
                add_to_output = item + ': ' + str(match[item]) + '/n'
                output += add_to_output

        await self.bot.say(output)


def setup(bot):
    bot.add_cog(apiCog(bot))