import json

from openai import AzureOpenAI

from app.config import settings


class ApprovalService:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_KEY,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_version="2024-02-15-preview"
        )

    def evaluate(
        self,
        merchant,
        amount,
        category,
        validation_result
    ):

        prompt = f"""
        Review this expense.

        Merchant: {merchant}
        Amount: {amount}
        Category: {category}

        Policy Validation:

        Valid: {validation_result['valid']}
        Reason: {validation_result['reason']}

        Return ONLY valid JSON:

        {{
            "recommendation": "APPROVE",
            "reason": "short explanation"
        }}

        or

        {{
            "recommendation": "REJECT",
            "reason": "short explanation"
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
                "recommendation": "MANUAL_REVIEW",
                "reason": "Unable to parse AI response"
            }