import nicoocord as nc
import discord
from discord.ext import commands
from discord.commands import slash_command


class Test(commands.Cog):
    def __init__(self, bot: nc.Bot) -> None:
        self.bot = bot

    @slash_command(name="test")
    async def _test(self, ctx: discord.ApplicationContext) -> None:
        await nc.Embeds.info(ctx, "Test")

    @slash_command(name="add_user")
    async def _add_user(self, ctx: discord.ApplicationContext, member: discord.Member) -> None:
        result = await self.bot.execute_query("INSERT INTO users VALUES (?, ?)", (member.id, member.name))


def setup(bot: nc.Bot) -> None:
    bot.add_cog(Test(bot))
