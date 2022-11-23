import interactions, os
from dotenv import load_dotenv
load_dotenv("./.env")
bot = interactions.Client(token=os.getenv("token"))

@bot.event
async def on_ready():
    bot.change_presence(name="keikun1215")

@bot.command(
    name="ping",
    description="Help of this server"
)
async def ping(ctx: interactions.CommandContext):
    await ctx.send(embeds=[interactions.Embed(
        title="🏓Pong!",
        description=f"ping: {bot.latency}"
    )])

bot.start()
