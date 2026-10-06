import base64
import json
import mimetypes

from openai import AzureOpenAI

from app.config import settings


class VisionService:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_KEY,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_version="2024-02-15-preview"
        )

    def extract_receipt(self, image_path):

        mime_type, _ = mimetypes.guess_type(
            image_path
        )

        if mime_type is None:
            mime_type = "image/jpeg"

        print(f"Image Path: {image_path}")
        print(f"MIME Type: {mime_type}")

        with open(image_path, "rb") as image_file:

            encoded_image = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        try:

            response = self.client.chat.completions.create(
                model=settings.AZURE_MODEL_DEPLOYMENT,
                messages=[
                    {
                        "role": "system",
                        "content": """
You are an expense receipt extraction assistant.

Extract information from the receipt.

Return ONLY valid JSON in this format:

{
    "merchant_name": "",
    "receipt_date": "",
    "total_amount": 0,
    "tax": 0,
    "currency": ""
}
"""
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": """
Extract:

- merchant_name
- receipt_date
- total_amount
- tax
- currency

Return only JSON.
"""
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{mime_type};base64,{encoded_image}"
                                }
                            }
                        ]
                    }
                ],
                temperature=0
            )

            content = response.choices[0].message.content

            print("Model Response:")
            print(content)

            try:
                return json.loads(content)

            except json.JSONDecodeError:

                return {
                    "error": "Response is not valid JSON",
                    "raw_response": content
                }

        except Exception as e:

            print("VISION ERROR:")
            print(str(e))

            return {
                "error": str(e)
            }
