import time
import random


def print_pause(messagestoprint):
    print(messagestoprint)
    time.sleep(2)
    

def questionare():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?')
    while True:
        response = input("(Please enter 1 or 2.)")
        if response == "1":
           house()
           break
        elif response == "2"
           cave()
           break
    return response
                
                
def adventure_game():
    questionare()
                
                
def house():
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a dragon")
    print_pause("Eep! This is the dragon's house!)
    print_pause("The dragon attacks you!)
    while reply != 1 and reply != 2:
        reply = input("What would you like to (1) fight or (2) run away?)
        if reply == "1":
            print_pause("As the dragon moves to attack you unsheath your new sword")
            print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
            print_pause("But the dragon takes on look at your shiny new toy and run away")
            print_pause("You have rid of the town of the dragon. You are victorious")
        elif reply == "2":
            print_pause("You run back into the field. Luckly, you don't seem to have been followed.")
            print_pause("You feel a bit under_prepared for this, what with only having a tiny dagger")
            reply = input("Would you like to (1) fight or (2) run away?)
            print_pause("You do your best..")
            print_pause("but your dagger is no much for the dragon.")
            print_pause("You have been defeated!)
                        
            
def cave():
    # Things that happen to the player in the cave
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the sword with you.")
                        
            
def field():
   # Things that happen to the player in the field
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumour has it that a dragon is somewhere around here and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")
    print_pause("Would you like to play again? (y/n)")



advemture_game()
