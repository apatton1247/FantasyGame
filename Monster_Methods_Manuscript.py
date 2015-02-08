############### Monster Methods Manuscript ###############

########## Bad Stuff Methods ##########

def lose_level(number, character):
    character.level -= 1
    if number == 1:
	print("%s lost 1 level!" % (character.name))
    else:
	print("%s lost %d levels!" % (character.name, number))

def lose_lower_items(character):
	pass

def no_bad_stuff():
    print("No bad stuff has happened to %s.  Move along." % (character.name))
    pass

def lose_footgear(character):
    for item in self.equipment["footgear"]:
        discard(item, self.equipment["footgear"])
        print("%s lost the %s" % (character.name, item.name))

def lose_big_items(character):
    pass

#Maybe we should define different paths to take with this and the related lose_field_item
# functions based on whether the character is choosing their own stuff to lose or whether
# another player is choosing for them.
def lose_backpack_item(number, character):
    print(character.backpack)
    for item in range(number):
        item_name = input("Which item (%d of %d) from your backpack will you drop?" % (item+1, number)).lower()
        for backpack_item in character.backpack:
            if backpack_item.name == item_name:
                discard(backpack_item, character.backpack)
                print("%s lost the %s" % (character.name, item_name))
                break
        else:
            print("You must choose an item you have in your backpack. Try again.")
            item -= 1

def lose_race(character):
    if len(character.char_race) == 2:
        print(character.char_race)
        choice = input("Which race will you lose? ").lower()
        discard(choice, character.char_race)
        print("%s lost their %s-ness." % (character.name, choice))
    elif character.char_race[0] == "human":
        print("No effect.  You are already just a human.")
    else:
        discard(character.race[0], character.char_race)
        print("%s lost their %s-ness." % (character.name, choice))

def lose_races(character):
    if character.char_race[0] != "human":
        for char_race in character.char_race:
            discard(char_race, character.char_race)
            print("%s went back to being just a human." % (character.name))
    else:
        print("No effect.  You are already just a human.")

def font_italic(character):
    #Somehow italicize the font of whatever the person says until their next turn.
    pass

########## Fight Methods ##########			

def bribe(item):
    pass


########## Bias Methods ##########

def monster_bias(number1, number2)
    return (number1 * number2)

def classless(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
	if character.char_class == "normal":
	    num_bias += 1
    return num_bias	
	
def clerics(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
	if character.char_class == "cleric":
	    num_bias += 1
    return num_bias

def warriors(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
	if character.char_class == "warrior":
            num_bias += 1
    return num_bias

def bards(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
        if character.char_class == "bard":
            num_bias += 1
    return num_bias

def thieves(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
        if character.char_class == "thief":
            num_bias += 1
    return num_bias

def wizards(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
        if character.char_class == "wizard":
            num_bias += 1
    return num_bias

def humans(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
        if character.char_race == "human":
            num_bias += 1
    return num_bias

def elves(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
        if character.char_race == "elf":
            num_bias += 1
    return num_bias

def dwarves(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
        if character.char_race == "dwarf":
            num_bias += 1
    return num_bias

def halflings(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
        if character.char_race == "halfling":
            num_bias += 1
    return num_bias

def orcs(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
        if character.char_race == "orc":
            num_bias += 1
    return num_bias

def gnomes(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].keys():
        if character.char_race == "gnome":
            num_bias += 1
    return num_bias

########## Chase Methods ##########

def auto_escape():
    pass


########## Good Stuff Methods ##########