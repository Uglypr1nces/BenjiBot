def handle_response(message):
    message = str(message).lower()

    if message == "hi":
        return "Hello!"

    if message == "help":
        commands = open("UglyPrincess/commands.txt", "r")
        return commands.read()

    if message == "suck":
        return "guck guck guck"

    if "+" in message:
        numbers = message.split("+")
        try:
            return int(numbers[0]) + int(numbers[1])
        except:
            return "I'm sorry, I can't add those numbers."

    if "-" in message:
        numbers = message.split("-")
        try:
            return int(numbers[0]) - int(numbers[1])
        except:
            return "I'm sorry, I can't subtract those numbers."

            
    return "I'm sorry, I don't understand that."
