import openai


def initialize_messages() -> list:
    """Initialize the chat messages with system and user messages."""
    # Load custom knowledge from file
    with open('/Users/saimethukupally/chatgpt-custom-knowledge-chatbot/knowledge/nato_wikipedia_export.txt', 'r') as f:
        custom_knowledge = f.read()
    return [
        {"role": "system", "content": "You’re a kind helpful assistant, only respond with knowledge knowledge you "
                                      "know for sure, dont hallucinate information."},
        {"role": "user", "content": custom_knowledge}

    ]


def get_user_input() -> str:
    """Get user input from the command line."""
    return input("User: ")


def add_message(messages: list, role: str, content: str):
    """Add a message to the list of chat messages."""
    messages.append({"role": role, "content": content})


def generate_chat_response(messages: list) -> str:
    """Generate a chat response using the OpenAI API."""
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message.content


def main():
    messages = initialize_messages()

    while True:
        user_message = get_user_input()
        add_message(messages, "user", user_message)

        chat_response = generate_chat_response(messages)
        print(f'ChatGPT: {chat_response}')
        add_message(messages, "assistant", chat_response)


if __name__ == '__main__':
    main()
