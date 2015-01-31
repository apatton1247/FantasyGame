#Character class only included in the gameplay main file until we figure out how to import
# it correctly from another .py file in the same folder or something.
class Character(object):
  def __init__(self, name, gender):
    #This initializes basic Character traits
    self.name = name
    self.level = 0
    self.char_class = "normal"
    self.char_race = "human"
    self.gender = gender
    #This initializes equipment (equipped items)
    self.equipment = {}
    #This initializes equipment slots
    self.hand_slots = 2
    self.hand_slots_used = 0
    self.footgear_slots = 1
    self.footgear_slots_used = 0
    self.headgear_slots = 1
    self.headgear_slots_used = 0
    self.armor_slots = 1
    self.armor_slots_used = 0
    self.big_item_slots = 1
    self.big_item_slots_used = 0
    #This initializes backpack (hand)
    self.backpack_size = 5
    self.backpack = {}
    #This initializes closet (unequipped items)
    self.closet = {}
    #This initializes curses
    self.curses = {}
    self.bad_stuff = {}
  def open_door(in_the_room):
    pass
  def pick_up_treasure(treasure):
    pass
  def discard(thing):
    pass
  def equip(equipment):
    pass
  def unequip(equipment):
    pass
  def view_char(character):
    pass
  def view_hand(char_hand):
    pass


#TBD - import Character    
from random import randint  
    

#Runs gameplay

character_list = []
door_deck = []
treasure_deck = []

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
def create_decks()
    door_card_file = open(door_card_list.txt, "r")
    door_card_list = []
    door_card_list.append(door_card_file.readline())
    #TBD - create DoorCard objects
    door_deck = []
    next_card_index = randint(0, len(door_card_list)-1)
    door_deck.append(door_card_list.pop(next_card_index))

    treasure_card_file = open(treasure_card_list.txt, "r")
    treasure_card_list = []
    treasure_card_list.append(treasure_card_file.readline())
    #TBD - create TreasureCard objects
    treasure_deck = []
    next_card_index = randint(0, len(treasure_card_list)-1)
    treasure_deck.append(treasure_card_list.pop(next_card_index))

    door_card_file.close()
    treasure_card_file.close()

    return door_deck, treasure_deck
    
#Whenever a character has to (re)supply at the garrison, this function places
# 4 DoorCard objects and 4 TreasureCard objects in their backpack
def get_supplies(character):

    supplies = {}
    for thing in supplies:
        character.backpack.append(thing)

#Starts the game.  Adds characters to the character list, prepares the decks,
# and gives the characters their starting supplies
def start_game(deck):
    add_characters()
    door_deck, treasure_deck = create_decks()
    for character in character_list:
        get_supplies(character)

#We used the double-commented lines below to test the game's add_characters function.
#It totally worked as planned and we're awesome at coding.
##add_characters()
##
##for character in character_list:
##    print(character.name,  character.gender)
