import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class PythonBot(commands.Bot):
    def __init__(self):
        super().__init__(
            intents = discord.Intents.all(), command_prefix = '.',
            description = "My Python experiment.", )
        self.uptime = None
        self.client_id = 1095082464432627851
        self.owner_id = 488699894023061516
        self.token = os.getenv('DISCORD_TOKEN')
        self.remove_command("help")

    async def setup_hook(self):
        for extension in os.listdir('cogs'):
            if extension.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{extension[:-3]}')
                except Exception as e:
                    print(f'Failed to load extension {extension[:-3]}\n{type(e).__name__}: {e}')
        await self.tree.sync()
        # Add views here to be persistent

    def run(self):
        super().run(token = self.token, reconnect = True)


python = PythonBot()
# Context menus goes here
python.run()
