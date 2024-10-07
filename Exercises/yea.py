import random
import time

def type_text(text, speed):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)
    print()

name_dialogue = "Hello! What is your name?"
