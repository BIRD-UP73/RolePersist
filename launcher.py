from discord.ext.commands import Bot

from config import token
from events import RoleHandler

bot = Bot(command_prefix='!', help_command=None)
bot.add_cog(RoleHandler())
bot.run(token)
