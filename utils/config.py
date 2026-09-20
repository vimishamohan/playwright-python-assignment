import os
from dotenv import load_dotenv

environment = os.getenv("TEST_ENV", "qa")

load_dotenv(f".env.{environment}")

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

print("Environment:", environment)
print("Base URL:", BASE_URL)
print("Username:", USERNAME)
print("Password:", PASSWORD)
