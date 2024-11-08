import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "25206101"))
    API_HASH = os.getenv("API_HASH", "2135724a8fdecb737f31d22ec8e6894b")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7519586705:AAEPvYf5XKXre0eF6QI6q1Ne50sshH3ti04")
    sudo = os.getenv("SUDO", "7601457849")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
