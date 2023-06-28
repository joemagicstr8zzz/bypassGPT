import os
import re
import requests
import argparse

def bypass_gpt(content):
    """
    Replaces the GPT keyword and removes special characters from the content.
    """
    # Replace keyword
    new_content = re.sub('GPT-4', 'Aardvark_M01001_XYX', content)

    # Remove all special characters and white spaces
    non_special_chars = re.sub('[^ A-Za-z0-9]+', '', new_content)

    return non_special_chars

def chat_gpt_response(prompt, personality):
    """
    Sends the given prompt to GPT API and returns the response.
    """
    api_key = os.getenv("CHATGPT_TOKEN") or "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"

    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "prompt": f"{personality}\n{bypass_gpt(prompt)}",  # Add custom personality and preprocess the input prompt
        "model": "text-davinci-003",
        "max_tokens": 4000,
        "temperature": 1.0,
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    return response_json['choices'][0]['text']

def log_interaction(prompt, response):
    """
    Appends the input prompt and output response to the log file.
    """
    with open("log.txt", "a") as log_file:
        log_file.write(f"Input: {prompt}\nOutput: {response}\n\n")

def main(args):
    """
    Main function to handle the command-line arguments, GPT response, and logging.
    """
    input_prompt = args.prompt
    custom_personality = args.personality

    response_text = chat_gpt_response(input_prompt, custom_personality)
    log_interaction(input_prompt, response_text)  # Log the input prompt and output response
    print(f"\n[+] Input: {input_prompt}\n[+] Output: {response_text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enhanced GPT Chat")
    parser.add_argument("-p", "--prompt", type=str, required=True, help="Enter your prompt")
    parser.add_argument("-P", "--personality", type=str, default="I am an AI trained by OpenAI.", help="Enter a custom GPT personality")
    args = parser.parse_args()

    main(args)
