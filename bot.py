import discord
from discord.ext import commands
import deepl
import os
from dotenv import load_dotenv
from config import FLAG_TO_LANG, LANGUAGES  # Import shared variables

# Load environment variables
load_dotenv()

# Initialize the translator with your DeepL API key
translator = deepl.Translator(os.getenv('DEEPL_API_KEY'))

intents = discord.Intents.default()
intents.message_content = True  # Ensures the bot receives message content
intents.reactions = True  # Enable reaction events

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Import and register commands from commands.py
from commands import setup
setup(bot)

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    flag = str(reaction.emoji)
    if flag not in FLAG_TO_LANG:
        print(f"Ignoring non-flag emoji: {flag}")
        return

    message = reaction.message
    target_lang = FLAG_TO_LANG[flag]

    if not message.content.strip():
        await message.channel.send("⚠️ Cannot translate an empty message.")
        return

    if message.embeds:
        await message.channel.send("⚠️ Cannot translate an embedded message.")
        return

    if message.attachments:
        await message.channel.send("⚠️ Cannot translate an attachment.")
        return

    try:
        translated = translator.translate_text(message.content.strip(), target_lang=target_lang.upper())

        # Create an embed
        embed = discord.Embed(
            title=f"Translation to {LANGUAGES[target_lang]}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Original Message", value=message.content, inline=False)
        embed.add_field(name="Translated Message", value=translated.text, inline=False)
        embed.set_footer(text=f"Requested by {user.name}", icon_url=user.avatar.url if user.avatar else user.default_avatar.url)

        await message.channel.send(embed=embed)

    except Exception as e:
        print(f"Error during translation: {e}")
        await message.channel.send("⚠️ An error occurred during translation.")

# Run the bot
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
