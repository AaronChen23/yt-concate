import os #2
from dotenv import load_dotenv #1

load_dotenv() #1
API_KEY = os.getenv("API_KEY") #2
# print(api_key)

DOWNLOADS_DIR = "downloads"
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, "videos")
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, "captions")
OUTPUTS_DIR = "outputs"