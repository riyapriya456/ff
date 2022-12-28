from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "19376711")
    API_HASH = environ.get("API_HASH", "97d6b9d4999508a0c29d71c348d33351")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5649345445:AAEALDSlFIFTAxJxpsdE3JzfIBySuTKEnjU")
    STRING_SESSION = environ.get("STRING", "1BVtsOHsBu0xRiT62eWFl7QUGee_RPU9RbAAHBz5Vl9T9BeAiZJHbpo6cjgKt5OIGaG0QF0scAISV1LJKJnU7laRsdoF0Tw0Ler7-8BORU0Zafc4Lq6UezHk1WTUHV4Hbvx6i0ulaRHqBQoi4vSTwWZrWeMJ2MOX4_s7clrwOqAkIgJOBXfqd2gp8SuAT8cKxyiB04ktRv5Z873hiKbkTM6uz4cyc7btoJMC1bp1rFI5_Zac5qVGN2laCWwKlLCyx029NfXztwA71Uzntu9U3wvPeDboRJOPuSL-ucU02wT5OFZla4QhU87qhGzasuHlm-pwFLi6MImSPDcl9qt-ktUsCT_QO34I=")
    SUDO_USERS = environ.get("SUDO_USERS", "5493968060")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
