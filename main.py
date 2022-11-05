import interactions, os
from dotenv import load_dotenv
load_dotenv("./.env")
bot = interactions.Client(token=os.getenv("token"))

@bot.command(
    name="help",
    description="Help of this server"
)
async def help(ctx: interactions.CommandContext):
    await ctx.send({"embeds":[interactions.Embed(
        title="test"
    )]})

bot.start()
