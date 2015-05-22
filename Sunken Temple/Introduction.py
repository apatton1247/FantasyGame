########## Sunken Temple Intro ##########

from Character_Class import *
#from Options_class import *
from datetime import date

def print_options(*options):
    for option in options:
        print(option.rjust(64))

def pause():
    pause_statement = input("")
    #Look into putting a timer here so that they can either press "Enter"
    # or have a timer with the reasonable amount of time do it instead.

def skip_intro():
    print("Intro skipped")

def wake_character(mode):
    #options = Options_class()
    #options.add_option("skip intro", "hidden")
    #options.add_option("stand up", "visible")
    options = ["skip intro", "stand up"]
    #Display a different sort of message depending on whether a player wakes
    # up willingly or has to be shaken/kicked awake (if the latter, their turn
    # is last, until someone else has to be awoken forcibly after them)
    if mode == "force":
        print("You are shaken awake.")
    print("You wake up lying on a cold stone floor. This is not\nyour bedroom...")
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
    options.remove("stand up")
    #Look into timers to play large amounts of text automatically!
    print("\nShaking your head, you stand up and look around. The")
    print("room you are in seems to be perfectly circular, with a")
    print("single curved wall reaching so high that the ceiling is")
    print("hidden in blackness. In the center of the room is a large,")
    print("2-story obelisk made of the same smooth stone as everything")
    print("else in the room...")
    pause_template = input("(Press 'Enter' to continue.)")
    print("You realize that you are surrounded by others waking up.")
    print("They appear to be just as surprised to be here as you are.")
    print("You then notice a pattern. Every single person in this")
    print("room is wearing a bracelet on his or her wrist. Even you!")
    options.append("examine bracelet")
    print(("examine bracelet").rjust(64))
    choice_2 = input("").lower()
    while(choice_2 not in options):
        if choice_2 == "options":
            print_options(options)
        choice_2 = input("").lower()
    if choice_2 == "skip intro":
        skip_intro()
    #If the choice is not "skip intro", then they have typed in "examine
    #bracelet, and the story keeps playing.
    print("You try to take off your bracelet for a closer look, but")
    print("it doesn't budge. It's stuck! You notice that although")
    print("each person's bracelet seems to be made of the same")
    print("strange metallic material, they're not exactly identical.")
    print("Each bracelet is a distinctive and unique color.")
    print("Speechless, you notice that there is a message inscribed")
    print("on the side of the obelisk. It says...")
    pause()
    print("   Welcome! This is the Temple of the Lost, a mystical")
    print("   room deep beneath the surface of the world. Which")
    print("   world... does not matter. What does matter is that")
    print("   the only way you can leave is through a gateway.")
    pause()
    print("*Bffffffzahhh!*\n")
    print("Almost as if on cue, a shimmering, arched doorway appears")
    print("behind you on the wall. The gateway's surface is swirling")
    print("with every color imaginable.  You continue reading...")
    pause()
    print("   Entering a gateway will transport you to a different")
    print("   dimension. Some of them are friendly, like the one")
    print("   which just opened, leading to your Shrine. Some of them...")
    print("   are not. You can only enter a gateway containing the")
    print("   color of the key you are wearing on your wrist. No one")
    print("   else can enter unless pulled in by someone on the inside.")
    pause()
    print("   Once you have collected eleven keys, only then will a")
    print("   gateway with your door's color appear, leading to")
    print("   your home dimension.")
    print("   Keys do more than summon gateways. They can give you")
    print("   special powers and even change your molecular and")
    print("   genetic structure if combined with the right magical")
    print("   item.")
    pause()
    #Add Visit Shrine, View Character, and View Obelisk to options.
    

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

def run():
    statement_1 = "You are in your bed, watching the evening news on TV. A correspondent from NASA is discussing a weird 'cosmic event' that's imminent to earth. The discussion is so boring that you drift off to sleep.\n"
    to_print = (statement_1)
    yield to_print

enter_game()
