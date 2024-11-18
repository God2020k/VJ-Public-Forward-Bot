from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "17627887")
    API_HASH = environ.get("API_HASH", "d14e54b0791ca1f8b0f26786439e336e")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7144831299:AAFAG5xpXE2PHo2USbtIP2TL8CwaG6U7sAI")
    STRING_SESSION = environ.get("STRING_SESSION", "BQEXr9MAcnl2a6ZgDoCiRjomra8J1AaCPX8uPEif_20J9Y29at89M7eX4PVT4gnaEC1QGH_f3xicSAvLxJ8tTrfmIYF0HvOeLDRqcV0iImJwSHQRs7fOCiS7yLLMGC5qdRlr-X7FG7QdEuT9HBq4jyo73JsrKFmgwOhg7MwesBj1RflC3XwyU0SvS7NK565VE9U-AWRj6VFUI_tCtSoDxaI5JaipOK_PGR_SlK1VL6YacuoECEHh6adNGK1aOINxuyOAKGbyl40mIbrhpUv9f1dflg_n_f8MrhDNwljP_b_GTNPAXpXqqfDvh5Zf-P0HTK8LamVl7s9WWMz0aNN67wAbHUnYQwAAAABW22yGAA")
    SUDO_USERS = environ.get("SUDO_USERS", "5211097531")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@KingVJ01**
    """
