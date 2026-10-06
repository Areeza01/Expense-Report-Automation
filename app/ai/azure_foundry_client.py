import os
from openai import AzureOpenAI

from app.config import settings


class AzureFoundryClient:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_KEY,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_version="2024-02-15-preview"
        )

    def run_agent(
        self,
        agent_id: str,
        message: str
    ):
        """
        Sends a message to an Azure AI Foundry Agent.

        Replace implementation with the
        Agent SDK invocation method used
        in your Azure AI Foundry project.
        """

        response = self.client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": f"Agent ID: {agent_id}"
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content