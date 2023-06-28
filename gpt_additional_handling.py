def preprocess_prompt(prompt, personality):
    """
    Preprocesses the prompt with the custom personality.
    """
    return f"{personality}\n{prompt}"

def postprocess_response(response):
    """
    Postprocesses the GPT response for better readability.
    """
    return response.strip()
