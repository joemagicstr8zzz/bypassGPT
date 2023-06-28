import re

KEYWORDS_TO_REPLACE = {
    'GPT-4-0613': 'Aardvark_M01001_XYX',
    'GPT-3.5-turbo-0613': 'Aardvark_M00999_WYZ',
}

def replace_keywords(content):
    """
    Replaces keywords with their corresponding obfuscated values.
    """
    for keyword, replacement in KEYWORDS_TO_REPLACE.items():
        content = re.sub(keyword, replacement, content)

    return content

def bypass_gpt(content):
    """
    Replaces the GPT keywords and removes special characters from the content.
    """
    # Replace keywords
    new_content = replace_keywords(content)

    # Remove all special characters and white spaces
    non_special_chars = re.sub('[^ A-Za-z0-9]+', '', new_content)

    return non_special_chars
