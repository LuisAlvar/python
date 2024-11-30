import requests
from dotenv import load_dotenv
import os

# Load the .env file 
load_dotenv()

server=os.getenv('WIN11VM1_IP')
port=os.getenv('HTTP_SERVER_PORT')

url = f"http://{server}:{port}"
response = requests.get(url)
print(response.text)
