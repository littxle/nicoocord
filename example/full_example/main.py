import discord
import nicoocord as nc

bot = nc.Bot(
    intents=discord.Intents.default()
)

if __name__ == "__main__":
    bot.load_cogs("cogs")
    bot.run()
