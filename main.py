import interactions, os
bot = interactions.Client(token=os.getenv("token"))

@bot.command(
    name="test",
    description="Test command"
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

bot.start()
