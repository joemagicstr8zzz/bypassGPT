import os
import argparse
from gpt_bypass import bypass_gpt
from gpt_additional_handling import preprocess_prompt, postprocess_response
from gpt_config import LOG_FILE
from gpt_utils import call_gpt_api

def chat_gpt_response(prompt, personality):
    """
    Sends the given prompt to GPT API with custom personality and returns the response.
    """
    preprocessed_prompt = preprocess_prompt(bypass_gpt(prompt), personality)
    response_text = call_gpt_api(preprocessed_prompt)
    return postprocess_response(response_text)

def log_interaction(prompt, response):
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
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
