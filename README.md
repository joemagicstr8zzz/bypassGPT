# bypassGPT

This repository contains Python scripts for interacting with OpenAI's GPT-3 API with some additional handling and bypassing techniques.

## Files

The repository consists of the following Python files:

1. `enhanced_gpt_chat_v3.py`: This is the main script that handles command-line arguments, calls the GPT API, and logs the interactions.

2. `gpt_additional_handling.py`: This script contains functions for preprocessing the prompt with a custom personality and postprocessing the GPT response for better readability.

3. `gpt_bypass.py`: This script replaces certain keywords with obfuscated values and removes special characters from the content.

4. `gpt_config.py`: This script contains the configuration details for the GPT API, such as the API key, API URL, model, maximum tokens, temperature, and log file.

5. `gpt_history.py`: This script manages the conversation history, including adding new interactions and formatting the history.

6. `gpt_utils.py`: This script contains a function for calling the GPT API and returning the response.

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include:

```
argparse
requests
openai
```

## Usage

To use the `enhanced_gpt_chat_v3.py` script, you can run it with the `-p` or `--prompt` argument to specify your prompt, and the `-P` or `--personality` argument to specify a custom GPT personality. For example:

```bash
python enhanced_gpt_chat_v3.py -p "Hello, GPT-3!" -P "I am an AI trained by OpenAI."
```

## Note

Please replace `"your_OPENAI KEY"` in `gpt_config.py` with your actual OpenAI API key.
