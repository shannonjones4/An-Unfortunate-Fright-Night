# name: Shannon Jones and Sydney Elledge
# date: 2018-10-23
# description: Text-based horror adventure game

import random
import time

def displayIntro():
    print("It was a dark and spooky night.")
    time.sleep(3)
    print("You come across a haunted, abandoned house on your way to your friend's Halloween party.")
    time.sleep(3)
    print("There's a creepy clown standing at the stop sign near you.")
    time.sleep(2)
    print("The clown starts heading in your direction, laughing.")
    time.sleep(2)
    print("You are curious to see what is inside.")
    time.sleep(3)
    print('Go inside or Go to the party?')
    time.sleep(3)
    print('...')

def chooseOption():
    chooseOption = input("What would you like to do? Type in 'party' to continue going to the party or 'house' to go inside the house: " )
    return chooseOption
    anotherOption = input("If you do not want to choose \"party\" or \"house\" you may also choose to \"run\" or \"go home\".  What would you like to do?: ")
    return anotherOption
    print("You have made a decision.")
    time.sleep(2) 

def checkOption(chooseOption):
    option = ""
    another_option = ""
    if option == "party":
        print("The clown was just a figment of your imagination.")
        time.sleep(3)
        print("Your friend pulls up and asks if you want a lift to the party.")
        print("You have chosen wisely.  You are safe...for now...")
    elif option == "house":
        print("A burst of cold air brushes your shoulder and the door to the house slams shut.")
        time.sleep(3)
        print("A masked man comes out of the kitchen with an electric chainsaw.")
        time.sleep(3)
        print("He walks towards you, reving the saw.")
        time.sleep(3)
        print("You stumble as you flee to escape.")
        time.sleep(3)
        print("The masked man stands over your body and ends your existance.")
def checkOption(anotherOption):
    if another_option == "run":
        print("You run away from the clown, terrified for your life.")
        time.sleep(3)
        print("You accidently trip and fall, but when you try to get up, you are greeted by the terrifying grin of the creepy clown.")
        time.sleep(3)
        print("You open your mouth to scream for help, but it is too late!")
        time.sleep(3)
        print("The clown puts you in a bag, picks you up, and walks away laughing")
        time.sleep(3)
        print("You are now a prisoner of the clown.")
    elif another_option == "go home":
        print("The sound of the piano and the eeriness of the abandoned house make you want to skip the party.")
        print("You turn around, and head home.")  

checkOption(chooseOption)
checkOption(anotherOption)
        

playAgain = "Yes"
while playAgain == "Yes" or playAgain == "y" or playAgain == "Y" or playAgain == "yes":
    displayIntro()
    choice = chooseOption()
    checkOption(choice)
    playAgain = input("Do you want to play again? (Yes or y to go again.) ")
    
    if playAgain == "No" or playAgain =="n":
        print("Better luck next time.  Happy Halloween! (:")
