import discord
import nicoocord as nc
from nicoocord.modules import Embeds
from nicoocord.modules import Colors


bot = nc.Bot()


@bot.slash_command(name="test")
async def test(ctx: discord.ApplicationContext) -> None:
    embed = Embeds.embed(
        title="This is a title",
        description="This is a description",
        color=Colors.silver
    )
    await ctx.send(embed=embed)
    await Embeds.success(ctx, "This is a success embed")
    await Embeds.error(ctx, "This is an error embed")

if __name__ == "__main__":
    bot.run("token")
