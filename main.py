import interactions, os
from dotenv import load_dotenv
load_dotenv("./.env")
bot = interactions.Client(token=os.getenv("token"))

@bot.command(
    name="hello",
    description="Test command"
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hello!")

bot.start()
