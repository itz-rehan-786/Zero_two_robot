
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "27744639" # integer value, dont use ""
    API_HASH = "a5e9da62bcd7cc761de2490c52c89ccf"
    TOKEN = "8167388254:AAE5Fbts2L8erz7Sa_t4pqFqziQi9g06DXc"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 2145093972 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "the_support_chat"  # Your own group for support, do not add the @
    START_IMG = "https://i.ibb.co/Y8tMqkB/photo-2024-10-29-17-43-43.jpg"
    EVENT_LOGS = (-1002272021040)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://waifuuu0786:sungjinwoo@cluster0.uctgneu.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://inrxxedz:HzJvAfoh73yRlx64xGp8Bg2WA0XVR5oa@tiny.db.elephantsql.com/inrxxedz"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "BUATLRCHB18ICFC0"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "3LPPBQ5DET7O"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = [-1002272021040]  # List of groups that you want blacklisted.
    DRAGONS = [7775259302]  # User id of sudo users
    DEV_USERS = [7775259302]  # User id of dev users
    DEMONS = [7775259302]  # User id of support users
    TIGERS = [7775259302]  # User id of tiger users
    WOLVES = [7775259302]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
