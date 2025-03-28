# commands.py

import discord
from discord.ext import commands
from config import FLAG_TO_LANG, LANGUAGES  # Import shared variables

def setup(bot):
    """
    Registers the `!languages` command with the bot.
    """
    @bot.command(name="languages")
    async def languages(ctx):
        """
        Displays the list of supported languages and their corresponding flag emojis.
        """
        # Create an embed to display the supported languages
        embed = discord.Embed(
            title="Supported Languages",
            description="Here are the languages supported by the translation bot:",
            color=discord.Color.blue(),
        )

        # Add supported languages to the embed
        for flag, lang_code in FLAG_TO_LANG.items():
            language_name = LANGUAGES.get(lang_code, "Unknown Language")
            embed.add_field(name=f"{flag} {language_name}", value=f"Code: `{lang_code}`", inline=False)

        # Add a note about unsupported languages
        embed.add_field(
            name="Unsupported Languages",
            value="If a language is not listed above, it is currently not supported.",
            inline=False,
        )

        # Send the embed to the channel
        await ctx.send(embed=embed)