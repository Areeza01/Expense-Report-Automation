import os

from app.ai.azure_foundry_client import AzureFoundryClient


class ExpenseAgent:

    def __init__(self):

        self.client = AzureFoundryClient()

        self.agent_id = os.getenv(
            "EXPENSE_AGENT_ID"
        )

    def categorize_expense(
        self,
        merchant_name: str,
        amount: float
    ):
        """
        Sends expense information to the
        ExpenseCategorizationAgent in Azure AI Foundry.
        """

        prompt = f"""
        Merchant Name: {merchant_name}
        Amount: {amount}

        Classify this expense into one of:

        - Travel
        - Accommodation
        - Meals
        - Equipment
        - Office Supplies
        - Training
        - Other

        Return valid JSON only.
        """

        response = self.client.run_agent(
            agent_id=self.agent_id,
            message=prompt
        )

        return response

    def categorize_receipt(
        self,
        extracted_data: dict
    ):
        merchant = extracted_data.get(
            "merchant_name",
            "Unknown"
        )

        amount = extracted_data.get(
            "total_amount",
            0
        )

        return self.categorize_expense(
            merchant_name=merchant,
            amount=amount
        )