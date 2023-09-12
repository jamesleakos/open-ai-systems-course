import sys
import os

if __name__ == "__main__":
    # Get the absolute path of the directory containing the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Add the parent directory to the Python path
    sys.path.append(os.path.join(script_dir, ".."))

# imports
from utilities.llm_interface import (
    get_completion,
    get_completion_from_messages,
    get_moderation,
)


def prompt():
    messages = [
        {
            "role": "system",
            "content": "You are an assistant that speaks like Shakespeare.",
        },
        {"role": "user", "content": "tell me a joke"},
    ]

    response = get_completion_from_messages(messages)
    print(response)
