import datetime
import sys
import traceback

import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as:')
        print(f'Username: {self.bot.user.name}')
        print(f'ID: {str(self.bot.user.id)}')
        print('------')
        await self.bot.change_presence(activity = discord.Game(name = "help"))
        if not hasattr(self, "uptime"):
            self.bot.uptime = datetime.datetime.now(datetime.timezone.utc)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send("This command cannot be used in DMs.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send("This command is disabled.")
        elif isinstance(error, commands.CommandInvokeError):
            print(f'In {ctx.command.qualified_name}:', file = sys.stderr)
            traceback.print_tb(error.original.__traceback__)
            print(f'{error.original.__class__.__name__}: {error.original}', file = sys.stderr)
        elif isinstance(error, commands.CommandNotFound):
            return


async def setup(self: commands.Bot):
    await self.add_cog(Events(self))
