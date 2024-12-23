# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "29648469"))
    API_HASH = getenv("API_HASH", "911348bbad1eaa660a8e1c542dc1b4bf")
    BOT_TOKEN = getenv("BOT_TOKEN", "7805780777:AAFK4LtPVVu6rDrQvOXYYKZTw7Oy1_caqhg")
    FSUB = getenv("FSUB", "@mrdangerbots")
    CHID = int(getenv("CHID", "-1002362240666"))
    SUDO = list(map(int, getenv("SUDO", "7260255450").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sibasahu036:<db_password>@cluster0.7qoey.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
