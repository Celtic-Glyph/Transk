# config.py

# Mapping country flag emojis to language codes (DeepL-supported codes)
FLAG_TO_LANG = {
    "🇩🇪": "de",  # Germany
    "🇪🇸": "es",  # Spain
    "🇫🇷": "fr",  # France
    "🇨🇳": "zh",  # China (Simplified Chinese)
    "🇵🇹": "pt-pt",  # Portugal (European Portuguese)
    "🇮🇹": "it",  # Italy
    "🇯🇵": "ja",  # Japan
    "🇬🇧": "en-gb",  # United Kingdom (English)
    "🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f": "en-gb",  # England flag (full Unicode)
    "🇷🇺": "ru",  # Russia
    "🇵🇱": "pl",  # Poland
    "🇹🇷": "tr",  # Turkey
}

# A dictionary to map language codes to human-readable language names
LANGUAGES = {
    "de": "German",
    "es": "Spanish",
    "fr": "French",
    "zh": "Chinese (Simplified)",
    "pt-pt": "Portuguese (Portugal)",
    "pt-br": "Portuguese (Brazil)",
    "it": "Italian",
    "ja": "Japanese",
    "en-gb": "English (UK)",
    "us": "English (US)",
    "ru": "Russian",  # Russian
    "pl": "Polish",  # Polish
    "tr": "Turkish",  # Turkish
}