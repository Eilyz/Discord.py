import discord
from discord import app_commands
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = 'ping', description = 'Check latency of the bot.')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! {round(self.bot.latency * 1000)}ms')


async def setup(self: commands.Bot):
    await self.add_cog(Utility(self))
