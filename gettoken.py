#!/usr/bin/python3

from requests import post
from dotenv import load_dotenv

import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTH_URL = "https://accounts.spotify.com/api/token"

resp = post(AUTH_URL, {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}).json()

print(resp["access_token"])
