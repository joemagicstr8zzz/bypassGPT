def preprocess_prompt(prompt, personality):
    """
    Preprocesses the prompt and personality into the Chat Completions message format.
    """
    return [
        {"role": "system", "content": personality},
        {"role": "user", "content": prompt}
    ]

def postprocess_response(response):
    """
    Postprocesses the GPT response for better readability.
    """
    return response.strip()
