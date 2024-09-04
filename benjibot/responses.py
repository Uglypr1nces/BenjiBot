from benjibot.variables.insults import get_insult
from benjibot.tictactoe.game import Game

def handle_response(message):
    message = str(message).lower()
    
    if message == "hi":
        return "Hello!"

    if message == "help":
        commands = open("benjibot/variables/commands.txt", "r")
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
    
    if "insult" == message:
        return get_insult()

    if "say" in message:
        return message[4:]

    if ":slight_Smile:" in message or "🙂" in message:
        return get_bot_insult()


    return "I'm sorry, I don't understand that."

