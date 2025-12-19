from email.mime import message
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Create the bot object
bot = commands.Bot(command_prefix="$", intents=intents)

# Create the client object
# client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# @client.event
# async def on_ready():
#     print(f"Logged in as {client.user}")

def get_driver(headless=True):
    options = Options()
    
    # Core options
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    options.add_argument("window-size=1920x1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Optional: simulate incognito or custom user-agent
    options.add_argument("--incognito")
    # options.add_argument("user-agent=Mozilla/5.0 ...")

    # Launch Chrome with WebDriver Manager
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver

# options = Options()
# options.add_argument("--headless")  # Run in background
# driver = webdriver.Chrome(options=options)

# driver.get("https://wuwaflex.com/upload")

# # Locate the upload field and submit button
# upload_field = driver.find_element("name", "image")
# upload_field.send_keys("path/to/image.jpg")

# submit_button = driver.find_element("id", "submit")
# submit_button.click()

@bot.command()
async def upload(ctx):
    driver = get_driver()
    driver.get("https://wuwaflex.com")
    # continue automation steps...

# This is just a simulation
# @bot.command()
# async def upload(ctx, image_url: str):
#     await ctx.send(f"Uploading image to WuwaFlex: {image_url}")
#     # Simulate success
#     result = True
#     if result:
#         await ctx.send("✅ Image successfully sent to WuwaFlex!")
#     else:
#         await ctx.send("❌ Failed to upload image.")

# Testing on how to make a simple function
@bot.event
async def on_message(message):
    if message.content == '!hello':
        await message.channel.send('Hi there!')
    await bot.process_commands(message)

@bot.command()
async def pingping(ctx):
    await ctx.send('Pong!')

@bot.command()
# dlt stands for delete
async def dlt(ctx, limit: int = 100):
    deleted = await ctx.channel.purge(limit=limit)
    await ctx.send(f'Deleted {len(deleted)} messages', delete_after=3)

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
# client.run(token)
bot.run(token)