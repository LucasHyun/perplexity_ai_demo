import os
import requests

# Get API key from environment variables
api_key = os.getenv('PERPLEXITY_API_KEY')

# Perplexity API endpoint
url = "https://api.perplexity.ai/chat/completions"

# Data to request
payload = {
    "model": "llama-3.1-sonar-small-128k-online",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": "How many stars are there in our galaxy?"
        }
    ],
    # "max_tokens": 100,  # This value can be set as an integer or omitted.
    "temperature": 0.2,
    "top_p": 0.9,
    "return_citations": True,
    "search_domain_filter": ["perplexity.ai"],
    "return_images": False,
    "return_related_questions": False,
    "search_recency_filter": "month",
    "top_k": 0,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 1
}

# Add API key to headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Send API request
response = requests.post(url, json=payload, headers=headers)

# Print response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")

# /Users/lucashyun/PycharmProjects/perplexity_api_demo/.venv/bin/python /Users/lucashyun/PycharmProjects/perplexity_api_demo/perplexity_api.py
# /Users/lucashyun/PycharmProjects/perplexity_api_demo/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
#   warnings.warn(
# {'id': '6856c069-d562-4cff-8632-fd2b03a65deb', 'model': 'llama-3.1-sonar-small-128k-online', 'created': 1729391194, 'usage': {'prompt_tokens': 14, 'completion_tokens': 17, 'total_tokens': 31}, 'object': 'chat.completion', 'choices': [{'index': 0, 'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': 'There are approximately 100 billion stars in the Milky Way galaxy.'}, 'delta': {'role': 'assistant', 'content': ''}}]}
