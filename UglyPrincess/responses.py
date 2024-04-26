from UglyPrincess.variables.insults import get_insult

def handle_response(message):
    message = str(message).lower()

    if message == "hi":
        return "Hello!"

    if message == "help":
        commands = open("UglyPrincess/variables/commands.txt", "r")
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

    if "*" in message:
        numbers = message.split("*")
        try:
            return int(numbers[0]) * int(numbers[1])
        except:
            return "I'm sorry, I can't multiply those numbers."
    
    if "/" in message:
        numbers = message.split("/")
        try:
            return int(numbers[0]) / int(numbers[1])
        except:
            return "I'm sorry, I can't divide those numbers."
    
    if "insult" in message:
        return get_insult()

    if "say" in message:
        return message[4:]

    return "I'm sorry, I don't understand that."
