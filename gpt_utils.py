import requests
from gpt_config import API_KEY, API_URL, MODEL, MAX_TOKENS, TEMPERATURE

def call_gpt_api(messages):
    """
    Sends the given structured messages to the OpenAI Chat Completions API and returns the response.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    data = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response_json = response.json()
    except Exception as e:
        print(f"Request failed: {e}")
        return ""

    # Print the full API response for debugging
    print("API Response:", response_json)  

    if 'choices' in response_json and len(response_json['choices']) > 0:
        return response_json['choices'][0]['message']['content']
    else:
        error_msg = response_json.get("error", {}).get("message", "Unknown error")
        print("Error:", error_msg)
        return ""
