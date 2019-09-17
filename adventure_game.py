import time
import random
creature = ['gorggon', 'troll', 'dragon', 'pirate']
creature = random.choice(creature)


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
    items = []
    field()     
    questionare()
                
                
def house(items):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out steps a " +
        creature)
    print_pause("Eep! This is the " + creature + "'s house!")
    print_pause("The " + creature + " attacks you!")
    if "sword" in items:
        reply = ''
        while reply != 1 and reply != 2:
            reply = input("What would you like to (1) fight or (2) run away?")
            if reply == "1":
                print_pause("As the " + creature +
                            " moves to attack you unsheath your new sword")
                print_pause("The Sword of Ogoroth shines brightly in your hand"
                            " as you brace yourself for the attack.")
                print_pause("But the " + creature +
                            " takes on look at yur shiny new toy and run away")
                print_pause("You have rid the town of the " +
                            creature + ". You are victorious")
                play_again()
                break
            elif reply == "2":
                print_pause(
                    "You run back into the field. "
                    "Luckly, you don't seem to have been followed.")
                questionare(items)
            break
    else:
        print_pause(
            "You feel a bit under_prepared for this,"
            " what with only having a tiny dagger")
        reply = ""
        while reply != 1 and reply != 2:
            reply = input("Would you like to (1) fight or (2) run away?")
            if reply == "1":
                print_pause("You do your best...")
                print_pause("but your dagger is no much for the " + creature)
                print_pause("You have been defeated!")
                play_again()
                break
            elif reply == "2":
                print_pause(
                    "You run back into the field."
                    " Luckly, you don't seem to have been followed.")
                questionare(items)
                        
            
def cave(items):
    # Things that happen to the player in the cave
     print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field")
        questionare(items)
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause(
            "You discard your silly old dagger and take the sword with you.")
        items.append("sword")
        print_pause("You walk back out to the field.")
        questionare(items) 
                
                
def field():
   # Things that happen to the player in the field
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + creature + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effective) dagger.")
 
                
def play_again():
    answer = input("Would you like to play again? (y/n)")
    if answer == "y":
        print_pause("Excellent! Restrating the game..")
        adventure_game()
    elif answer == "n":
        print_pause("Thanks for playing. come play again soon.")
    else:
        print('Sorry I did not understand that!')
        play_again()
                
                
advemture_game()
