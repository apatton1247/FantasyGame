############### Monster Methods Manuscript ###############

########## Bad Stuff Methods ##########

def lose_level(number, character):
    character.level -= 1
    if number == 1:
        print("%s lost 1 level!" % (character.name))
    else:
        print("%s lost %d levels!" % (character.name, number))

def lose_lower_items(character):
    for item in character.equipment:
        pass

def no_bad_stuff():
    print("No bad stuff has happened to %s.  Move along." % (character.name))
    pass

def lose_headgear(character):
    for item in character.equipment["headgear"]:
        discard(item, character.equipment["headgear"])
        print("%s lost the %s" % (character.name, item.name))

def lose_armor(character):
    for item in character.equipment["armor"]:
        discard(item, character.equipment["armor"])
        print("%s lost the %s" % (character.name, item.name))

def lose_weapons(character):
    for item in character.equipment["weapons"]:
        discard(item, character.equipment["weapons"])
        print("%s lost the %s" % (character.name, item.name))
        
def lose_footgear(character):
    for item in character.equipment["footgear"]:
        discard(item, character.equipment["footgear"])
        print("%s lost the %s" % (character.name, item.name))

def lose_slotless(character):
    for item in character.equipment["slotless"]:
        discard(item, character.equipment["slotless"])
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

def empty_backpack(character):
    for backpack_item in character.backpack:
        discard(backpack_item, character.backpack)
        print("%s lost the %s" % (character.name, item_name))

def lose_field_item(number, character):
    print(character.equipment, character.closet)
    for item in range(number):
        item_name = input("Which item (%d of %d) from your equipment/closet will you drop?" % (item+1, number)).lower()
        for field_item in character.equipment:
            if field_item.name == item_name:
                discard(field_item, character.equipment)
                print("%s lost the %s" % (character.name, item_name))
                break
        else:
            for field_item in character.closet:
                if field_item.name == item_name:
                    discard(field_item, character.closet)
                    print("%s lost the %s" % (character.name, item_name))
                    break
            else:
                print("You must choose an item you have in your backpack. Try again.")
                item -= 1

def empty_equipment(character):
    lose_headgear(character)
    lose_armor(character)
    lose_weapons(character)
    lose_footgear(character)
    lose_slotless(character)

def empty_closet(character):
    for item in character.closet:
        discard(item, character.closet)

def lose_race(character):
    if len(character.char_race) == 2:
        print(character.char_race)
        choice = input("Which race will you lose? ").lower()
        discard(choice, character.char_race)
        print("%s lost their %s-ness." % (character.name, choice))
    elif character.char_race[0] == "human":
        print("No effect.  You are already just a human.")
    else:
        discard(character.char_race[0], character.char_race)
        print("%s lost their %s-ness." % (character.name, choice))

def lose_races(character):
    if character.char_race[0] != "human":
        for char_race in character.char_race:
            discard(char_race, character.char_race)
            print("%s went back to being just a human." % (character.name))
    else:
        print("No effect.  You are already just a human.")

def lose_class(character):
    if len(character.char_class) == 2:
        print(character.char_class)
        choice = input("Which class will you lose? ").lower()
        discard(choice, character.char_class)
        print("%s lost their %s-ness." % (character.name, choice))
    elif character.char_class[0] == "classless":
        print("No effect.  You already had no class.")
    else:
        discard(character.char_class[0], character.char_class)
        print("%s lost their %s-ness." % (character.name, choice))

def lose_classes(character):
    if character.char_class[0] != "classless":
        for char_class in character.char_class:
            discard(char_class, character.char_class)
            print("%s went back to being classless." % (character.name))
    else:
        print("No effect.  You already had no class.")

def font_italic(character):
    #Somehow italicize the font of whatever the person says until their next turn.
    pass

def death(character):
    character.level = 1
    #Need some way to get their items in their backpack and on the field visible, and then
    # allow the other non-dead players (in level order) to pick something from them, while
    # the rest is discarded.  Their turn must end.  They then respawn at the start of
    # the next player's turn, and the get_supplies() at the beginning of their next turn.
    # Maybe most of that should happen outside of the death() method, back in gameplay?

########## Fight Methods ##########			

def bribe(item):
    pass


########## Bias Methods ##########

def monster_bias(number1, number2):
    return (number1 * number2)

def classless(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "normal" in char_obj.char_class:
                num_bias += 1
    return num_bias	
	
def clerics(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "cleric" in char_obj.char_class:
                num_bias += 1
    return num_bias

def warriors(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "warrior" in char_obj.char_class:
                num_bias += 1
    return num_bias

def bards(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "bard" in char_obj.char_class:
                num_bias += 1
    return num_bias

def thieves(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "thief" in char_obj.char_class:
                num_bias += 1
    return num_bias

def wizards(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "wizard" in char_obj.char_class:
                num_bias += 1
    return num_bias

def humans(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "human" in char_obj.char_race:
                num_bias += 1
    return num_bias

def elves(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "elf" in char_obj.char_race:
                num_bias += 1
    return num_bias

def dwarves(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "dwarf" in char_obj.char_race:
                num_bias += 1
    return num_bias

def halflings(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "halfling" in char_obj.char_race:
                num_bias += 1
    return num_bias

def orcs(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "orc" in char_obj.char_race:
                num_bias += 1
    return num_bias

def gnomes(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if "gnome" in char_obj.char_race:
                num_bias += 1
    return num_bias

def males(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if char_obj.gender == "male":
                num_bias += 1
    return num_bias

def females(battle_dict):
    num_bias = 0
    for character in battle_dict["character"].values():
        for char_obj in character.keys():
            if char_obj.gender == "female":
                num_bias += 1
    return num_bias

########## Chase Methods ##########

def auto_escape():
    pass

########## Pursuit Methods ##########

def will_not_pursue():
    pass

########## Good Stuff Methods ##########

