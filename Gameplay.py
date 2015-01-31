from Character_Class import *
from Monster_Class import *
from random import randint  
    
#Runs gameplay

character_list = []
door_deck = []
treasure_deck = []
game_not_over = True

#Adds characters to the game.  To be called at the beginning of the game
# and may be called if new characters wish to enter mid-game.
def add_characters():

    num_characters = input("How many characters are in the garrison? ")
    while not num_characters.isnumeric():
        num_characters = input("Please enter a number of characters. ")
    else:
        num_characters = int(num_characters)

    for character_number in range(len(character_list), len(character_list) + num_characters):
        name = input("\nCharacter %d Name: " % (character_number + 1))
        gender = input("Character %d Gender: " % (character_number + 1))
        character = Character(name, gender)
        character_list.append(character)

#Reads in the card names from appropriate text files, creates card objects, and populates
# the door and treasure decks with those card objects.
def create_decks():
    door_card_list = []
    with open("door_card_list.txt", "r") as door_card_file:
        for line in door_card_file:
            door_card_list.append(door_card_file.readline().rstrip())
    print("Door card list: ", door_card_list)
    #TBD - create DoorCard objects
    door_deck = []
    door_list_len = len(door_card_list)
    for x in range(door_list_len):
        next_card_index = randint(0, len(door_card_list)-1)
        door_deck.append(door_card_list.pop(next_card_index))
    if not door_card_file.closed:
        door_card_file.close()
    print("Door deck: ", door_deck)

    treasure_card_list = []
    with open("treasure_card_list.txt", "r") as treasure_card_file:
        for line in treasure_card_file:
            treasure_card_list.append(treasure_card_file.readline().rstrip())
    print("Treasure card list: ", treasure_card_list)
    #TBD - create TreasureCard objects
    treasure_deck = []
    treasure_list_len = len(treasure_card_list)
    for x in range(treasure_list_len):
        next_card_index = randint(0, len(treasure_card_list)-1)
        treasure_deck.append(treasure_card_list.pop(next_card_index))
    if not treasure_card_file.closed:
        treasure_card_file.close()
    print("Treasure deck: ", treasure_deck)

    return door_deck, treasure_deck

def create_decks_2():
    door_card_list = ["Mr. Bones", "Cat Girl", "Tentacle Demon", "Plutonium Dragon",
                      "Lord Yahoo", "Were-Turtle", "Tequila Mockingbird",
                      "Perfectly Ordinary Bunny Rabbit", "Rapier Twit", "Face Sucker",
                      "Bigfoot", "Seven Year Lich", "Undead Horse", "Potted Plant",
                      "Poison Ivy Kudzu", "Maul Rat", "Large Angry Chicken", "3,872 Orcs",
                      "Plague Rats", "Shrieking Geek", "Scary Clowns", "Flying Frogs",
                      "Auntie Paladin", "M.T. Suit", "Gazebo", "Male Chauvinist Pig",
                      "The Dead Sea Trolls", "Frost Giant", "Hydrant", "Hungry Backpack"]
    #TBD - create DoorCard objects
    door_list_len = len(door_card_list)
    for x in range(door_list_len):
        next_card_index = randint(0, len(door_card_list)-1)
        door_deck.append(door_card_list.pop(next_card_index))

    treasure_card_list = ["Wishing Ring", "Reloaded Die", "Deus Ex Machinegun",
                          "Invisibility Potion", "Instant Wall", "Feline Intervention",
                          "Wishing Ring", "Itching Powder", "Loaded Die", "Flask of Glue",
                          "Loaded Die", "Wishing Ring", "Wand of Dowsing", "Doppleganger",
                          "Loaded Die", "Steal a Level", "Boots of Running Really Fast",
                          "Ghoul Lash", "Foot-Mounted Mace",
                          "Sword of Slaying Everything Except Squid", "Vorpal Blade"]
    #TBD - create TreasureCard objects
    treasure_list_len = len(treasure_card_list)
    for x in range(treasure_list_len):
        next_card_index = randint(0, len(treasure_card_list)-1)
        treasure_deck.append(treasure_card_list.pop(next_card_index))

    return door_deck, treasure_deck
    
#Whenever a character has to (re)supply at the garrison, this function places
# 4 DoorCard objects and 4 TreasureCard objects in their backpack
def get_supplies(character, door_deck, treasure_deck):

    supplies = []
    for x in range(4):
      supplies.append(door_deck.pop(0))
    for x in range(4):
      supplies.append(treasure_deck.pop(0))
    for thing in supplies:
        character.backpack.append(thing)

#Shuffles a deck's discard pile if the deck is completely empty, returning a new draw deck
def shuffle(discards):
  #Once we have a discard deck, shuffle it similarly to how we shuffled the start decks
  pass

def open_door(character, door_deck):
    print(character.backpack)
    if door_deck[0].type == "monster":
        monster = door_deck.pop(0)
        battle(character, monster)
    else:
        #TBD - create cases for curse cards and action cards
        pass

def battle(character, monster):
    battle_dict = {}
    battle_dict[character] = character.level
    battle_dict[character_bonus] = character.bonus
    battle_dict[monster] = monster.level
    pass

#Starts the game.  Adds characters to the character list, prepares the decks,
# and gives the characters their starting supplies
def start_game(door_deck, treasure_deck):
    add_characters()
    door_deck, treasure_deck = create_decks_2()
    for character in character_list:
        get_supplies(character, door_deck, treasure_deck)
def take_turn(character, door_deck):
    opening_statement = input("\n").lower()
    if opening_statement == "open door":
        open_door(character, door_deck)


start_game(door_deck, treasure_deck)
turn = 0
turn_round = 1
while game_not_over:
    take_turn(character_list[turn], door_deck)
    turn = (turn+1)%(len(character_list))
    if turn == 0:
        turn_round += 1


#We used the double-commented lines below to test the game's add_characters function.
#It totally worked as planned and we're awesome at coding.
##add_characters()
##
##for character in character_list:
##    print(character.name,  character.gender)
