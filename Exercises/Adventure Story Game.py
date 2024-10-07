import time

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("To your left is a dense forest.")
    print_pause("Behind you is a river.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")

def house(items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a fairie.")
    print_pause("Eep! This is the wicked fairie’s house!")
    print_pause("The fairie attacks you!")
    if "sword" in items:
        print_pause("As the fairie moves to attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
        print_pause("But the fairie takes one look at your shiny new toy and runs away!")
        print_pause("You have rid the town of the fairie. You are victorious!")
    else:
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the fairie.")
        print_pause("You have been defeated!")
    play_again()

def cave(items):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        items.append("sword")
    print_pause("You walk back out to the field.")
    field(items)

def forest(items):
    print_pause("You venture into the dense forest.")
    print_pause("The trees are tall and the forest is dark.")
    print_pause("You hear the sound of animals rustling in the underbrush.")
    if "shield" in items:
        print_pause("You've been here before and found the shield. There's nothing more to find here.")
    else:
        print_pause("As you walk deeper into the forest, you find a hidden path.")
        print_pause("Following the path, you come across an old chest.")
        print_pause("You open the chest and find a sturdy shield inside.")
        print_pause("You take the shield with you.")
        items.append("shield")
    print_pause("You walk back out to the field.")
    field(items)

def river(items):
    print_pause("You walk towards the river.")
    print_pause("The river is wide and the current is strong.")
    print_pause("You see a boat tied to a tree on the riverbank.")
    if "boat" in items:
        print_pause("You've been here before and taken the boat. There's nothing more to find here.")
    else:
        print_pause("You untie the boat and decide to take it with you.")
        items.append("boat")
    print_pause("You walk back out to the field.")
    field(items)

def mountain(items):
    print_pause("You decide to climb the mountain.")
    print_pause("The climb is steep and treacherous.")
    print_pause("As you reach the summit, you find a wise old sage.")
    print_pause("The sage offers you a choice: wisdom or strength.")
    choice = input("Do you choose wisdom or strength? (wisdom/strength)\n").lower()
    if choice == "wisdom":
        print_pause("The sage grants you a book of ancient knowledge.")
        items.append("wisdom")
    elif choice == "strength":
        print_pause("The sage grants you a potion of immense strength.")
        items.append("strength")
    else:
        print_pause("The sage does not understand your choice and disappears.")
    print_pause("You climb back down the mountain.")
    field(items)

def village(items):
    print_pause("You walk towards the village.")
    print_pause("The villagers are in a state of panic.")
    print_pause("They tell you that the wicked fairie has been causing havoc.")
    if "sword" in items and "shield" in items:
        print_pause("With your sword and shield, you feel ready to face the fairie.")
        print_pause("You head back to the field to confront the fairie.")
    else:
        print_pause("You feel unprepared to face the fairie without better equipment.")
        print_pause("You decide to explore more before confronting the fairie.")
    field(items)

def field(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("Enter 3 to venture into the forest.")
    print_pause("Enter 4 to walk towards the river.")
    print_pause("Enter 5 to climb the mountain.")
    print_pause("Enter 6 to walk towards the village.")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1, 2, 3, 4, 5, or 6.)\n")
    if choice == '1':
        house(items)
    elif choice == '2':
        cave(items)
    elif choice == '3':
        forest(items)
    elif choice == '4':
        river(items)
    elif choice == '5':
        mountain(items)
    elif choice == '6':
        village(items)
    else:
        field(items)

def play_again():
    print_pause("Would you like to play again? (y/n)")
    choice = input().lower()
    if choice == 'y':
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif choice == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()

def play_game():
    items = []
    intro()
    field(items)

play_game()