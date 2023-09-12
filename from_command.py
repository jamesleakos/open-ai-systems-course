import sys
from utilities.llm_interface import get_completion

# This script allows you to use the get_completion function from the command line.
# It takes one argument: the prompt you want to complete.

# To use this script, run it from the command line with the prompt as an argument.
# For example, if you want to complete the prompt "tell me a joke", you would run:
# python from_command.py "tell me a joke"


def main():
    # Check if the user provided a prompt
    if len(sys.argv) < 2:
        print("Please provide a prompt as a command line argument.")
        return

    # Get the prompt from the command line arguments
    prompt = sys.argv[1]

    # Get the completion
    completion = get_completion(prompt)

    # Print the completion
    print(completion)


if __name__ == "__main__":
    main()
