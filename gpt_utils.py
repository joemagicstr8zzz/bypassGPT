import requests
from gpt_config import API_KEY, API_URL, MODEL, MAX_TOKENS, TEMPERATURE

def call_gpt_api(prompt):
    """
    Sends the given prompt to GPT API and returns the response.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    data = {
        "prompt": prompt,
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response_json = response.json()

    print("API Response:", response_json)  # Add this line to print the full API response

    if 'choices' in response_json:
        return response_json['choices'][0]['text']
    else:
        print("Error:", response_json.get("error", "Unknown error"))
        return ""