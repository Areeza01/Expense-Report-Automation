import json

from openai import AzureOpenAI
from app.config import settings


class CategorizationService:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_KEY,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_version="2024-02-15-preview"
        )

    def categorize(self, merchant, amount):

        prompt = f"""
        Merchant: {merchant}
        Amount: {amount}

        Classify this expense into ONE category:

        - Travel
        - Accommodation
        - Meals
        - Equipment
        - Office Supplies
        - Training
        - Other

        Return ONLY valid JSON:

        {{
            "category": ""
        }}
        """

        response = self.client.chat.completions.create(
            model=settings.AZURE_MODEL_DEPLOYMENT,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        try:
            return json.loads(
                response.choices[0].message.content
            )

        except Exception:

            return {
                "category": "Other"
            }