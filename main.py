import discord
from discord.ext import commands
from discord.ext.commands.errors import UserInputError
from discord.utils import get
import time
import asyncio
from SecretToken import TOKEN #Import from a separate python file to get token to run bot
                              #You will have a different token if you are trying to test this bot
                              #In your Discord Developers site

client = commands.Bot(command_prefix= '!')
sList=[]
r=0

@client.event   #Will state when bot is active
async def on_ready():
    print("Bot is ready!")


@client.command() #!schedule command
async def schedule(ctx, *, user_input=None):
    await ctx.send(f"Please Enter Your Work Schedule {user_input} (✿◠‿◠)")
    await ctx.send(f"```[Month][Date][Work Time, eg. Jan 27, 12:00pm-5:00pm]```")
    sList.append(user_input)
    def check(msg):
        return msg.author == ctx.author
    msg = await client.wait_for("message", check=check)
    await ctx.send("Your Shift has been Saved for: " "``"+msg.content+"``")
    sList.append(msg.content)
   
        
@client.command() #!calendar command
async def calendar(ctx):
    for i in sList:
           await ctx.send("``"+i+"``")
    if len(sList)==0:
        await ctx.send("No One Is Currently Scheduled")
    
        
@client.command() #!remove command
async def remove(ctx, *, user_input=None):
    if len(sList)==0:
        await ctx.send("No One Is Currently Scheduled, There Is No One To Remove")
    if len(sList)>0:
        await ctx.send(f"Type the number corresponding to the list below to which it will remove. The first item is number 0!")
        def check(msg):
            return msg.author == ctx.author
        msg = await client.wait_for("message", check=check)
        if int(msg.content) % 2 != 0:
            r = int(msg.content)-1
        else:
            r = int(msg.content)
        for i in range(2):
            sList.pop(r)
            await ctx.send(msg.content+" has been removed" "``"+msg.content+"``")
        await ctx.send(f"The Current People Schedule Are Now")
    for i in sList:
        await ctx.send("``"+i+"``")


@client.command() #!poll command
async def poll(ctx,*,message):
    emb=discord.Embed(title="POLL", description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')


client.run(TOKEN) #token