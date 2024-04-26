def handle_response(message):
    message = str(message).lower()

    if message == "hi":
        return "Hello! How can I help you?"

    return "I'm sorry, I don't understand that."