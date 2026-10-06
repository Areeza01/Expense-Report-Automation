import os

from app.ai.azure_foundry_client import AzureFoundryClient


class ApprovalAgent:

    def __init__(self):

        self.client = AzureFoundryClient()

        self.agent_id = os.getenv(
            "APPROVAL_AGENT_ID"
        )

    def evaluate_expense(
        self,
        merchant: str,
        amount: float,
        category: str,
        policy_valid: bool,
        policy_reason: str
    ):
        """
        Sends expense data to the
        ExpenseApprovalAgent in Azure AI Foundry.
        """

        prompt = f"""
        Review this expense.

        Merchant: {merchant}
        Amount: {amount}
        Category: {category}

        Policy Validation Result:
        Valid: {policy_valid}
        Reason: {policy_reason}

        Return only valid JSON:

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

        response = self.client.run_agent(
            agent_id=self.agent_id,
            message=prompt
        )

        return response