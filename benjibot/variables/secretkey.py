import os

botsecretkey = ''

def change_key(new_key):
    global botsecretkey
    botsecretkey = new_key
    
def save_key_to_file(key):
    global botsecretkey
    botsecretkey = key
    with open('secretkey.txt', 'w') as file:
        file.write(botsecretkey.strip())
        
def check_key():
    return os.path.isfile('secretkey.txt') and os.path.getsize('secretkey.txt') > 0

def load_key():
    global botsecretkey
    with open('secretkey.txt', 'r') as file:
        botsecretkey = file.read().strip()  # Strip any leading/trailing whitespace
        return botsecretkey
