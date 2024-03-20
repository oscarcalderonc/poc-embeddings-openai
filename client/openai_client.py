import os
from openai import OpenAI, AzureOpenAI

def create_openai_client():
    USE_AZURE = os.environ.get("USE_AZURE", "False").lower() in ['true', '1', 't', 'y', 'yes']

    if USE_AZURE:
        return AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2023-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
    else:
        return OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))

# Usage example:
client = create_openai_client()