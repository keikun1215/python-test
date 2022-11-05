import interactions, os
from dotenv import load_dotenv
load_dotenv("./.env")
bot = interactions.Client(token=os.getenv("token"))

@bot.command(
    name="test",
    description="Test command"
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

bot.start()
