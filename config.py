import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "7713526"))
    API_HASH = os.environ.get("API_HASH", "6f87b351ddf6c8c56999f8ba5b19cc7c")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7053758018:AAGsfN8CwYDP39LnONcR623E9MdzkxIW5RA")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5071463525")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://win3298:QgcZpBkFdb14jKY7@cluster0.jdyos0q.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001580437794"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "autofrwd_robot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
