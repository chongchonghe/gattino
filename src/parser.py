import re

def extract_first_code_block(text: str) -> str:
    """Extract the first code block from AI response, preserving original formatting"""
    text = text.replace('```bash', '```')
    match = re.search(r"```(.*?)```", text, re.DOTALL)
    if match:
        # Only strip leading/trailing whitespace, preserve internal formatting
        return match.group(1).strip()
    return ""
