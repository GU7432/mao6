import random


with open("messages.txt", 'r', encoding="utf-8") as file:
    messages = file.readlines()

def getmes():
    n = random.randint(1, 4)
    random_message = ""
    for _ in range(n): random_message += random.choice(messages).rstrip("\n")
    # print(random_message)
    return random_message
getmes()