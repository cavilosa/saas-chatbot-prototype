import os
from dotenv import load_dotenv

# Find and load the .env file
ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
if os.path.exists(ENV_FILE):
    load_dotenv(ENV_FILE)

class Config:
    """Set Flask configuration from environment variables."""
    # IMPORTANT: Set the secret key
    SECRET_KEY = os.environ.get("APP_SECRET_KEY")
    
    # Auth0 settings
    AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID")
    AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET")
    AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")