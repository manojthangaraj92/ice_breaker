from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Print the API key to verify it is loaded correctly
print(f"Loaded API Key: {api_key}")

# Example use of the API key (assuming OpenAI library is installed)
# import openai
# openai.api_key = api_key
