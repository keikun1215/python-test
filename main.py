import interactions, os
from dotenv import load_dotenv
load_dotenv("./.env")
bot = interactions.Client(token=os.getenv("token"))

@bot.command(
    name="help",
    description="Help of this server"
)
async def help(ctx: interactions.CommandContext):
    await ctx.send(embeds=[interactions.Embed(
        title="Server help",
        description="""1. **How to report**"""
    )],components=[interactions.Button(
        style=interactions.ButtonStyle.DANGER,
        label="Delete",
        custom_id="delete_message",
    )])

bot.start()
