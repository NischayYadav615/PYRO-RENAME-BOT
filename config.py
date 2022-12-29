import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "19911978")

API_HASH = os.environ.get("API_HASH", "e3f5848d4c384af9e6f1f52ca84c19c7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5638535250") 

FORCE_SUB = os.environ.get("FORCE_SUB", "https://t.me/Legendbotupdates") 

DB_NAME = os.environ.get("DB_NAME","Nischayrobot")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Nischaybot:Nischaybot@cluster0.thf9kzz.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/ace2e5c2b733bfbdf8266.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5265175025').split()]

PORT = os.environ.get("PORT", "8080")
