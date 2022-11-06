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
        title="Server help menu"
    )],components=[interactions.SelectMenu(
        options=[interactions.SelectOption(
            label="How to report",
            value="hm_htr",
            description="How to report message",
        )],
        placeholder="CLICK ME",
        custom_id="helpmenu",
    )])
@bot.selectmenu("hm_htr")
async def selectmenu_response(ctx):
    await ctx.send("test", ephemeral=True)

bot.start()
