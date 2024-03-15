import os

from dotenv import load_dotenv

load_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"), verbose=True
)


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
