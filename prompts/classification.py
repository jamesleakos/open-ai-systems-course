import sys
import os

if __name__ == "__main__":
    # Get the absolute path of the directory containing the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Add the parent directory to the Python path
    sys.path.append(os.path.join(script_dir, ".."))

# imports
from utilities.llm_interface import get_completion, get_completion_from_messages

delimiter = "####"


def customer_service_bot():
    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be delimited with \
    {delimiter} characters.
    Classify each query into a primary category \
    and a secondary category. 
    Provide your output in json format with the \
    keys: primary and secondary.

    Primary categories: Billing, Technical Support, \
    Account Management, or General Inquiry.

    Billing secondary categories:
    Unsubscribe or upgrade
    Add a payment method
    Explanation for charge
    Dispute a charge

    Technical Support secondary categories:
    General troubleshooting
    Device compatibility
    Software updates

    Account Management secondary categories:
    Password reset
    Update personal information
    Close account
    Account security

    General Inquiry secondary categories:
    Product information
    Pricing
    Feedback
    Speak to a human

    """
    # user_message = f"""\
    # I want you to delete my profile and all of my user data"""
    user_message = f"""\
    Hello there, I hope that you're having a great day. I sadly think I forgot me code
    could you give me a new one? """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{delimiter}{user_message}{delimiter}"},
    ]
    response = get_completion_from_messages(messages)
    print(response)


if __name__ == "__main__":
    customer_service_bot()
