import os # for getting API token from env variable OPENAI_API_KEY
from openai import OpenAI # for calling the OpenAI API

# Initialize the shared client instance
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))