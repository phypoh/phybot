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
        response = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + input_name,
                               self.parameters)

        if response.status_code == 200:

            summoner_id = response.json()['accountId']

            response = requests.get('https://euw1.api.riotgames.com//lol/match/v4/matchlists/by-account/' + summoner_id,
                                   self.parameters)
            matches = response.json()['matches']

            output = ''
            i = 0
            for match in matches:
                i += 1
                output += '\nMatch ' + str(i) + '\n'
                for item in match:
                    add_to_output = item + ': ' + str(match[item]) + '\n'
                    output += add_to_output

                if i > 10:
                    break

        else:
            output = "Error code " + str(response.status_code)

        await self.bot.say(output)


    @commands.command()
    async def spyInt(self, input_name: str, region: str):
        region = region.lower()
        response = requests.get('https://' + region + '1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + input_name,
                               self.parameters)
        summoner_id = response.json()['accountId']

        response = requests.get('https://' + region + '1.api.riotgames.com//lol/match/v4/matchlists/by-account/' + summoner_id,
                               self.parameters)
        matches = response.json()['matches']

        output = ''
        i = 0
        for match in matches:
            i += 1
            output += '\nMatch ' + str(i) + '\n'
            for item in match:
                add_to_output = item + ': ' + str(match[item]) + '\n'
                output += add_to_output

            if i > 10:
                break

        await self.bot.say(output)


def setup(bot):
    bot.add_cog(apiCog(bot))