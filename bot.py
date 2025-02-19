import discord
from discord.ext import commands

# Set up bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Create buttons for Q&A
class QuestionView(discord.ui.View):
    def __init__(self):
        super().__init__()
        questions = [
            ("What is this bot?", "This is an automated Q&A bot!"),
            ("How do I use this bot?", "Just click a question and get an instant answer!"),
            ("Who created this bot?", "You did! With some help 😆"),
            ("Can I add more questions?", "Yes! Just edit the code and add new ones."),
            ("Is this bot smart?", "It’s getting smarter every update! 😈🔥"),
        ]
        for label, answer in questions:
            self.add_item(QuestionButton(label=label, answer=answer))

class QuestionButton(discord.ui.Button):
    def __init__(self, label, answer):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.answer = answer

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(self.answer, ephemeral=True)

# ✅ FIXED: Only ONE @bot.command() for "ask"
@bot.command(name="askme")  
async def askme(ctx):  
    embed = discord.Embed(  
        title="Frequently Asked Questions",  
        description="Click a question below to get an instant answer!",  
        color=discord.Color.blue()  
    )  
    embed.set_thumbnail(url="https://static.vecteezy.com/system/resources/thumbnails/024/553/676/small_2x/skull-wearing-crown-logo-skull-king-sticker-pastel-cute-colors-generative-ai-png.png")  

    view = QuestionView()  # Initialize buttons
    await ctx.send(embed=embed, view=view)  


@bot.command(name="support")
async def support(ctx):
    embed = discord.Embed(
        title="📌 Support Menu",
         description="Here are some commands you can use...",

        color=discord.Color.green()
    )
    embed.set_image(url="https://t3.ftcdn.net/jpg/02/15/61/92/360_F_215619203_9mmrDaPnSHOUBfz9XVkjBAknw5XFEK0D.jpg")  # Banner here!
    await ctx.send(embed=embed)
@bot.command(name="inf")  # This sets the command name
async def inf(ctx):  # This renames the function
    embed = discord.Embed(
        title="📌 Bot Information",
        description="This bot was created to provide instant answers!",
        color=discord.Color.blue()
    )
    embed.set_footer(text="Made by a legend 🔥")
    await ctx.send(embed=embed)


@bot.event
async def on_member_join(member):
    role_name = "Member"  # Change this to your role name
    guild = member.guild

    role = discord.utils.get(guild.roles, name=role_name)
    if role:
        await member.add_roles(role)
        print(f"✅ {member.name} was given the '{role_name}' role!")

class QuestionView(discord.ui.View):  
    def __init__(self):  
        super().__init__(timeout=None)  

        # Add buttons here
        self.add_item(QuestionButton("What is this bot?", "This is a bot who give you some info about this serveur !"))
        self.add_item(QuestionButton("Who created this bot?", "This bot was created by Mehdidou ! 🚀🔥"))
        self.add_item(QuestionButton("Who created this serveur ?", "This serveur was created by two Friends Mehdidou And Ibrahimovic in 2022 "))
        self.add_item(QuestionButton("The purpose of creating this serveur?", "Just to chill with friends and find someone to play with !"))
        self.add_item(QuestionButton("Can i be and admin in this serveur ?", " Actually we dont accept any one to be an admin , or we can only accpet old members "))
        self.add_item(QuestionButton("Games we support ?", "Valorant , Minecraft , One Arme coocked , Roblox , Combat Master , Mta , ...... Etc "))
class QuestionButton(discord.ui.Button):  
    def __init__(self, label, response):  
        super().__init__(label=label, style=discord.ButtonStyle.danger)  
        self.response = response  

    async def callback(self, interaction: discord.Interaction):  
        await interaction.response.send_message(self.response, ephemeral=True)  

bot.run("YOUR_BOT_TOKKEN")
