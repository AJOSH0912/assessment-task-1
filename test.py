import random
from tkinter import * 
import time
import sys
import time
import random
import shelve
import pygame
from simple_colors import *

pygame.mixer.init()
pygame.mixer.music.load('Sound.mp3')
pygame.mixer.music.play(1)

def f_gameOver(players):
    #* This function checks if the game is over
  ret = False
  won = 0
  for player in players:
    if players[player] != 0:
      won += 1
    if won == len(players):
      ret = True
    return ret

def init_briefcases():
    #* This function initialises the briefcases with random amounts of money using the random module
    briefcases = {}
    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000,
              750000, 1000000]
    for i in range(1, 27):
        briefcases[str(i)] = amount.pop(amount.index(random.choice(amount)))
    return briefcases

def list_to_string(list):
    #* This function converts a list to a string. It is used with the remaining briefcases
    #* It works by adding each element of the list to a string and adding a space after each element
    string = ""
    for i in list:
        string += i + " "
    return string

def makePlayers(number):
    #* This function makes a dictionary with the keys being the player numbers and the values being the player's money
    players = {}
    for i in range(1, number+1):
        players[str(i)] = 0
    return players

def multiplayer(numberOfPlayers):
    #* This is the main function for the multiplayer mode and works slightly differently to the single player mode
    #* Initialise all the variables
    briefcases = init_briefcases()
    players = makePlayers(numberOfPlayers) #* This creates a dictionary of players to keep track of their earnings
    remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    remaining_briefcases_for_display = [blue(1, "bold"), blue(2, "bold"), blue(3, "bold"), blue(4, "bold"), blue(5, "bold"), 
                                        blue(6, "bold"), blue(7, "bold"), blue(8, "bold"), blue(9, "bold"), blue(10, "bold"), 
                                        blue(11, "bold"), blue(12, "bold"), blue(13, "bold"), blue(14, "bold"), blue(15, "bold"),
                                        blue(16, "bold"), blue(17, "bold"), blue(18, "bold"), blue(19, "bold"), blue(20, "bold"),
                                        blue(21, "bold"), blue(22, "bold"), blue(23, "bold"), blue(24, "bold"), blue(25, "bold"), blue(26, "bold")]
    remaining_money_for_display =       [blue(0.1, "bold"), blue(1, "bold"), blue(5, "bold"), blue(10, "bold"), blue(25, "bold"), 
                                        blue(50, "bold"), blue(75, "bold"), blue(100, "bold"), blue(200, "bold"), blue(300, "bold"), 
                                        blue(400, "bold"), blue(500, "bold"), blue(750, "bold"), blue(1000, "bold"), blue(5000, "bold"),
                                        blue(10000, "bold"), blue(25000, "bold"), blue(50000, "bold"), blue(75000, "bold"), blue(100000, "bold"),
                                        blue(200000, "bold"), blue(300000, "bold"), blue(400000, "bold"), blue(500000, "bold"), 
                                        blue(750000, "bold"), blue(1000000, "bold")]
    briefcases_to_eliminate = 1


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
delay_print("\033[3;33;1m DEAL OR NO DEAL\n")

#The above code is the title of the game. It is in yellow and is in bold. It also has a delay print so it looks like the letters are being typed out.

briefcases = {1:1, 2:5, 3:10, 4:20, 5:50, 6:100, 7:200, 8:300, 9:1000, 10:1500, 11:2000, 12:3000, 13:5000, 14:7000, 15:10000, 16:20000, 17:30000, 18:50000, 19:70000, 20:100000, 21:150000, 22:200000, 23:300000, 24:500000, 25:750000, 26:1000000}
#This shows the amount of values each briefcase.
remaining_briefcases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#The above code shows the remaining briefcases.



def f_briefcases():
  briefcases = {}
  value = [1, 5, 10, 20, 50, 100, 200, 300, 1000, 1500, 2000, 3000, 5000, 7000, 10000, 20000, 30000, 50000, 70000, 100000, 150000, 200000, 300000, 500000, 750000, 1000000]
  for i in range(1,27):
    briefcases[str(i)] = value.pop(value.index(random.choice(value)))
  return briefcases

def offer(briefcases):
  val = 0
  for x in briefcases.values():
    val = val+x
  return val/len(briefcases)   

def f_select_briefcases(val):
  global briefcases
  while len(remaining_briefcases) > val:  
    delay_print("Choose a briefcase to eliminate\n ")
    user_choice = input()
    if int(user_choice) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases between 1 to 26")
    else:
      pygame.mixer.music.play(1)
      pygame.mixer.music.stop(1)
      delay_print("You eliminated " + str(briefcases[user_choice]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice)))
      briefcases.pop(user_choice)
  
    print()
#The above code asks to pick a personal briefcase between 1- 26. You then choose a breifcase to eliminate. If the player chooses a briefcases that is not between numbers 1-26 it will ask them to. It then tells them what briefcase they eliminated and how much money you have lost.
  delay_print("The banker is thinking of a deal")
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
#This informs the player that the banker is thinking of a deal while making "waiting emojis".
  delay_print("The banker offers you $" + str(offer(briefcases))) 
  print()
  time.sleep(2)
  delay_print("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  deal_or_no = input()
  delay_print(deal_or_no)
  if deal_or_no == "deal":
    print()
    delay_print("You have won " + str(offer(briefcases) + "dollars"))
    exit()
  else:
    print()
    delay_print("Ok, let's continue!")


#The above code shuffles all the briefcases from their original position.
delay_print("Welcome new player! Would you like to play a game of deal no deal?\n ")
yes_or_no = input() 
#This welcomes the player and asks them if they would like to play deal or no deal. If they reply "yes", it says "Great" and explains them the rules.

if yes_or_no.lower() == "yes":
  delay_print("Do you want to play as a guest(1) or do you want to sign in(2)? ")
  guest_or_sign_in = input()
  if guest_or_sign_in.lower() == "2":
  
    root = Tk()
    root.geometry("500x300")

    def getvals():
      print("Accepted")

    Label(root, text="Login Credentials", font ="arial 15 bold").grid(row=0, column=3)

    name= Label(root, text="Name")
    password= Label(root, text="Password")

    name.grid(row=1, column= 2)
    password.grid(row=2, column= 2)

    namevalue = StringVar
    passwordvalue = StringVar
    checkvalue = IntVar

    nameentry = Entry(root, textvariable=namevalue)
    #passwordentry = Entry(root, textvariable=passwordvalue)
    passwordentry = Entry(root, show="*")


    nameentry.grid(row=1, column=3)
    passwordentry.grid(row=2, column=3)

    checkbtn = Checkbutton(text="remember me?", variable= checkvalue)
    checkbtn.grid(row=6, column=3)

    #Button(text="Submit", command=getvals).grid(row=7, column=3 )
    Button(text="Submit", command=getvals).grid(row=7, column=3 )
    root.mainloop()

    


    delay_print("Do you know the rules\n")
    user_tutorial = input()
  
  elif guest_or_sign_in.lower() == "1":
    delay_print("You are playing as a guest and your high scores will not be recorded")
    delay_print("Do you know the rules\n")
    user_tutorial = input()
  
  else:
    delay_print("Please restart and enter a valid answer")
    exit()
else: 
  delay_print("Ok, bye!")
  exit()
#The code above asks the player if they want to go through the tutorial using an if then statement
if user_tutorial.lower() == "no":
  time.sleep(1)
  delay_print("There are 26 briefcases ranging from values from one dollar to one million dollars. ")
  time.sleep(1)
  delay_print("You must now choose to keep one briefcase safe from elimination this is known as your personal briefcase. ")
  time.sleep(1)
  delay_print("You will eliminate 6 briefcases of your choice. ")
  time.sleep(1)
  delay_print("After this the bank will make an offer, it is your choice to accept the offer or not. ")
  time.sleep(1)
  delay_print("If you take the deal then you will walk away with that amount of money and the game will end. ")
  time.sleep(1)
  delay_print("If you do not take the offer then you will choose another six briefcases to eliminate. ")
  time.sleep(1)
  delay_print("Then the banker will make another offer this will continue until either the contestant chooses a deal or they reach the last two remaining briefcases. ")
  time.sleep(1)
  delay_print("If the contestant reaches the last two remaining briefcases then the contestant must select one and the contestant will get the amount of money in the leftover briefcase. ")
else:
  delay_print("Let's Start\n")

delay_print("Do you want to play single player(1) or multiplayer(2)? ")
multplayer = input()


for player in players:
        print(yellow("Player " + player + "'s turn!", ["bold", "italic"])) #* Tells the user which player's turn it is
        print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nRemaining money", list_to_string(remaining_money_for_display),"Pick", briefcases_to_eliminate, "that you will discard.")
        #* Checks to see if the user has entered a valid number
        while True:
            try:
                number_to_eliminate = int(input("Briefcase to eliminate: "))
                money = briefcases[str(number_to_eliminate)]
                break
            except Exception:
                continue
        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
        #* Removes the briefcase from the list of remaining briefcases and updates the display
        remaining_briefcases.remove(number_to_eliminate)
        remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
        remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
        time.sleep(3)
        os.system("cls") #* Clears the screen to make it look cleaner

while briefcases_to_eliminate >= 1:
        #* Check to see if the game is over
        if gameOver(players):
            print(cyan("Good game players!. At the end the winner is: ", "bold"))
            print(cyan(dict(sorted(players.items(), key=lambda x:x[1], reverse=True)), "bold"))
            break
        for player in players:
            #* Check to see if the player has won some money
            if players[player] == 0:
                os.system("cls")
                print(yellow("Player " + player + "'s turn!", ["bold", "italic"]))
                offer = get_offer(briefcases) #
                print("Remaining briefcases:", list_to_string(remaining_briefcases_for_display), "\nRemaining money", list_to_string(remaining_money_for_display), "\nOffer: $", offer, "Deal or no deal?")
                choice = input("[D]eal or [N]o Deal? ")
                #* Allows the user to view the offer and choose to take it
                if choice.lower() == "d":
                    os.system("cls")
                    #* Stops the game and congratulates the user for accepting the offer
                    print("Good game Player", player, "! You got an offer of $", offer, "and you took it! You won $", offer, "! See you next time!")
                    choice = "n"
                    numberOfPlayers -= 1
                    players[player] = offer
                elif choice.lower() == "n":
                    os.system("cls")
                    #* If there is only one briefcase left, the user must take it
                    if len(remaining_briefcases) == 1:
                        print("You have one briefcase left. You must take it.")
                        offer = briefcases.pop(str(remaining_briefcases[0]))
                        print("You won $", offer, "!")
                        players[player] = offer
                        if not gameOver(players): #* Checks to see if there is only more than one player left
                            print(cyan("Good game players!. At the end the winner is: ", "bold"))
                            print(cyan(dict(sorted(players.items(), key=lambda x:x[1], reverse=True)), "bold"))
                            break
                    elif briefcases_to_eliminate == 1:
                        #* Runs the standard logic from the for loop above
                        print("The briefcases are", list_to_string(remaining_briefcases_for_display), "\nLeft over money is:", list_to_string(remaining_money_for_display), "\nPick", briefcases_to_eliminate, "that you will discard.")
                        while True:
                            try:
                                number_to_eliminate = int(input("Briefcase to eliminate: "))
                                money = briefcases[str(number_to_eliminate)]
                                break
                            except Exception:
                                continue
                        print("You removed briefcase", number_to_eliminate, "Which contained", briefcases.pop(str(number_to_eliminate)))
                        remaining_briefcases.remove(number_to_eliminate)
                        remaining_briefcases_for_display[number_to_eliminate - 1] = black(str(number_to_eliminate), "bold")
                        remaining_money_for_display[remaining_money_for_display.index(blue(money, "bold"))] = black(str(money), "bold")
                else:
                    #* If the input is incorrect, the loop restarts
                    continue

multiplayer(2) 