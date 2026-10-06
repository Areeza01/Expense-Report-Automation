import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    AZURE_OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

    AZURE_OPENAI_KEY = os.getenv(
        "AZURE_OPENAI_KEY"
    )

    AZURE_MODEL_DEPLOYMENT = os.getenv(
        "AZURE_MODEL_DEPLOYMENT"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///expense.db"
    )

settings = Settings()