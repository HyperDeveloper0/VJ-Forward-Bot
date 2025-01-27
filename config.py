# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "27358729"))
    API_HASH = environ.get("API_HASH", "6910fe5c69fb5fb2214162099ffe526c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://codecanvas93:MOgWu6DhrRYqunsc@rapid-forwarder.ankh5.mongodb.net/?retryWrites=true&w=majority&appName=rapid-forwarder")
    DATABASE_NAME = environ.get("DATABASE_NAME", "rapid-forwarder")
    BOT_OWNER = int(environ.get("BOT_OWNER", "7265713248"))

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


API = environ.get("API", "8551e30d52309a18d0c02a1162d8baa506ca9e5d") # shortlink api
URL = environ.get("URL", "instantearn.in") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/Reconic_Bots") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "RapidForwarderBot") # bot username without @
VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital