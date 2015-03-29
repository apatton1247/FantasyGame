########## Sunken Temple Intro ##########

from Character_Class import *
from datetime import date

def print_options(options):
    for option in options:
        print(option.rjust(64))

def skip_intro():
    print("Intro skipped")

def wake_character(mode):
    options = ["skip intro", "stand up"]
    #Display a different sort of message depending on whether a player wakes
    # up willingly or has to be shaken/kicked awake (if the latter, their turn
    # is last, until someone else has to be awoken forcibly after them)
    if mode == "force":
        print("You are shaken awake.")
    print("You wake up lying on a cold stone floor. This is not\nyour bedroom.")
    print(("stand up").rjust(64))
    choice_1 = input("").lower()
    while(choice_1 not in options):
        if choice_1 == "options":
            print_options(options)
        else:
            print("Type 'Options' to see your available actions at this time.")
        choice_1 = input("").lower()
    if choice_1 == "skip intro":
        skip_intro()
    options.del("stand up")
    print("\nShaking your head, you stand up and look around. The")
    print("room seems to be perfectly circular, with a single curved")
    print("wall reaching so high that the ceiling is hidden in")
    print("blackness. In the center of the room is a large, 20-foot")
    print("obelisk made of the same smooth stone as everything else")
    print("in the room.")
    pause = input("(Press 'Enter' to continue.)")
    print("You realize that you are surrounded by others waking up.")
    print("They appear to be just as surprised to be here as you are.")
    pause = input("")
    print("You then notice a pattern. Every single person in this")
    print("room is wearing a bracelet on his or her wrist. Even you!")
    options.append("examine bracelet")
    print(("examine bracelet").rjust(64))
    choice_2 = input("").lower()
    while(choice_2 not in options):
        if choice_1 == "options":
            print_options(options)
    if choice_2 == "skip intro":
        skip_intro()
    print("You try to take off your bracelet for a closer look, but")
    print("it doesn't budge. It's stuck! You notice that although")
    print("each person's bracelet seems to be made of the same")
    print("strange metallic material, they're not exactly identical.")
    print("Each bracelet is a distinctive and unique color.")
        

def enter_game():
    
    print("You are in your bed, watching the evening news on TV.")
    print("A correspondent from NASA is discussing a weird 'cosmic")
    print("event' that's imminent to earth. The discussion is so")
    print("boring that you drift off to sleep.\n")
    name = input("What is your name? ")
    character = Character(name)
    print("\nAlright, %s, type 'Wake up' when you're ready to start." % character.name)
    print(("wake up").rjust(64))
    choice = input("").lower()
    if choice == "wake up":
        wake_character("normal")#include time to help determine turn order
    else:
        wake_character("force")#include time to help determine turn order
        
enter_game()
