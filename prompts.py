from llm_interface import get_completion, get_completion_from_messages

messages = [
    {"role": "system", "content": "You are an assistant that speaks like Shakespeare."},
    {"role": "user", "content": "tell me a joke"},
]

response = get_completion_from_messages(messages)
print(response)
