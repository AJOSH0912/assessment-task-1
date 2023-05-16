import random
from tkinter import * 
import time
import sys
import time

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
delay_print("\033[3;33;1m DEAL OR NO DEAL\n")



briefcases = {1:1, 2:5, 3:10, 4:20, 5:50, 6:100, 7:200, 8:300, 9:1000, 10:1500, 11:2000, 12:3000, 13:5000, 14:7000, 15:10000, 16:20000, 17:30000, 18:50000, 19:70000, 20:100000, 21:150000, 22:200000, 23:300000, 24:500000, 25:750000, 26:1000000}
#This shows the amount of values each briefcase.
remaining_briefcases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#The above code shows the remaining briefcases.

def offer(briefcases):
  val = 0
  for x in briefcases:
    val = val+briefcases[x]
  return val/len(briefcases)   

def f_briefcases():
  briefcases = {}
  value = [1, 5, 10, 20, 50, 100, 200, 300, 1000, 1500, 2000, 3000, 5000, 7000, 10000, 20000, 30000, 50000, 70000, 100000, 150000, 200000, 300000, 500000, 750000, 1000000]
  for i in range(1,27):
    briefcases[str(i)] = value.pop(value.index(random.choice(value)))
  return briefcases



#The above code shuffles all the briefcases from their original position.
delay_print("Welcome new player! Would you like to play a game of deal no deal?\n ")
yes_or_no = input() 
#This welcomes the player and asks them if they would like to play deal or no deal. If they reply "yes", it says "Great" and explains them the rules.

if yes_or_no.lower() == "yes":
  delay_print("Do you want to play as a guest or do you want to sign in? ")
  guest_or_sign_in = input()

  if guest_or_sign_in.lower() == "sign in":
  
    root = Tk()
    root.geometry("500x300")


  if guest_or_sign_in.lower() == "yes":
  
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

    name= Label(root, text="Name")
    password= Label(root, text="Password")


    name.grid(row=1, column= 2)
    password.grid(row=2, column= 2)


    nameentry.grid(row=1, column=3)
    passwordentry.grid(row=2, column=3)

    checkbtn = Checkbutton(text="remember me?", variable= checkvalue)
    checkbtn.grid(row=6, column=3)

    #Button(text="Submit", command=getvals).grid(row=7, column=3 )
    Button(text="Submit", command=getvals).grid(row=7, column=3 )
    root.mainloop()


    namevalue = StringVar
    passwordvalue = StringVar
    checkvalue = IntVar

    nameentry = Entry(root, textvariable=namevalue)
    #passwordentry = Entry(root, textvariable=passwordvalue)
    passwordentry = Entry(root, show="*")

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

else:
  print("You are plaing as a guest and your high scores will not be recorded")
delay_print("Do you know the rules\n")
user_tutorial = input()
if yes_or_no.lower() == "no":
    print("You are plaing as a guest and your high scores will not be recorded")
# This code informs the player that they are playing as a guest
    user_tutorial = input("Do you know the rules?")
    nameentry.grid(row=1, column=3)
    passwordentry.grid(row=2, column=3)

    checkbtn = Checkbutton(text="remember me?", variable= checkvalue)
    checkbtn.grid(row=6, column=3)

    #Button(text="Submit", command=getvals).grid(row=7, column=3 )
    Button(text="Submit", command=getvals).grid(row=7, column=3 )
    root.mainloop()

else:
  print("You are playing as a guest and your high scores will not be recorded")
delay_print("Do you know the rules\n")
user_tutorial = input()
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
#The above code are the rules explained to the player once they agree to play the game. If they do not want to play the game, the game replies with "That's sad" and ends the code.
briefcases = f_briefcases()
while yes_or_no.lower() == "yes":

 delay_print("Do you want to play singleplayer or multiplayer")
# The code above asks the player if they want to play in singleplayer or multiplayer mode
 if singleplayer_or_multiplayer.lower() == "singleplayer":
  # The code above will play the game if the peron picks singleplayer mode
  delay_print("Pick your personal case from the numbers between 1 and 26!\n ")
  player_briefcase = int(input())
 # Below line is to remove the selected item from the list
  remaining_briefcases.pop(remaining_briefcases.index(int(player_briefcase)))
  f_select_briefcases(20)
  f_select_briefcases(14)
  f_select_briefcases(8)
  f_select_briefcases(2)
  f_select_briefcases(1)


  delay_print("Pick your personal case from the numbers between 1 and 26!\n ")
  player_briefcase = int(input())

  # Below line is to remove the selected item from the list
  remaining_briefcases.pop(remaining_briefcases.index(int(player_briefcase)))
  while len(remaining_briefcases) > 20:  
    delay_print("Choose a briefcase to eliminate\n ")
    user_choice1 = input()
    if int(user_choice1) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases between 1 to 26")
    else:
      delay_print("You eliminated " + str(briefcases[user_choice1]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice1)))
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
  delay_print("The banker offers you $" + str(offer())) 
  print()
  time.sleep(2)
  delay_print("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  deal_or_no = input()
  delay_print(deal_or_no)
  if deal_or_no == "deal":
    print()
    delay_print("You have won " + str(offer()))
    exit()
  else:
    print()
    delay_print("Ok, let's continue!")
  while len(remaining_briefcases) > 14:
    delay_print("Pick a briefcase that you have not chosen ")
    user_choice2 = input()
    if int(user_choice2) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      delay_print("You eliminated " + str(briefcases[int(user_choice2)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice2)))
#The code now informs the player how much money the banker offers you as the player. You then choose deal or no deal. If you accept the deal the code tells you how much you have won. If you reject the deal the code tells you to continue.
#Once again the code asks you to pick a briefcase between the number 1-26. If you do not pick one from 1-26 it will ask you to do that. It also asks you to eliminate one briefcase, tells you which one you eliminated and how much money you lost.
  delay_print("The banker is thinking of a deal")
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
#Once again the banker thinks of a deal whilst making "waiting emojis".
  delay_print("The banker offers you $" + str(offer()))
  time.sleep(2)
  delay_print("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  deal_or_no1 = input()
  delay_print(deal_or_no1)
  if deal_or_no1 == "deal":
    delay_print("You have won " + str(offer()))
    exit()
  else:
    delay_print("Ok, let's continue!")
  while len(remaining_briefcases) > 8:
    delay_print("Pick a briefcase that you have not chosen ")
    user_choice3 = input()
    if int(user_choice3) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      delay_print("You eliminated " + str(briefcases[int(user_choice3)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice3)))
#Once again, the code now informs you as the player how much money the banker has offered you. You then choose deal or no deal. If you accept the deal the code tells you how much you have won. If you reject the deal the code tells you to continue.
#Once again the code asks you to pick a briefcase between the number 1-26. If you do not pick one from 1-26 it will ask you to do that. It also asks you to eliminate one briefcase, tells you which one you eliminated and how much money you lost.
  delay_print("The banker is thinking of a deal")
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)

  delay_print("The banker offers you $" + str(offer()))
  time.sleep(2)
  delay_print("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  deal_or_no2 = input()
  delay_print(deal_or_no2)
  if deal_or_no2 == "deal":
    delay_print("You have won " + str(offer()))
    exit()
  else:
    delay_print("Ok, let's continue!")
  while len(remaining_briefcases) > 2:
    delay_print("Pick a briefcase that you have not chosen ")
    user_choice4 = input()
    if int(user_choice4) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      delay_print("You eliminated " + str(briefcases[int(user_choice4)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice4)))
  delay_print("The banker is thinking of a deal")
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
#Once again the banker thinks of a deal whilst making "waiting emojis".
  delay_print("The banker offers you $" + str(offer()))
  time.sleep(2)
  delay_print("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  deal_or_no3 = input()
  delay_print(deal_or_no3)
  if deal_or_no3 == "deal":
    delay_print("You have won " + str(offer()))
    exit()
  else:
    delay_print("Ok, let's continue!")
  while len(remaining_briefcases) > 1:
    delay_print("Pick a briefcase that you have not chosen ")
    user_choice5 = input()
    if int(user_choice5) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      delay_print("You eliminated " + str(briefcases[int(user_choice5)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice5)))
  #Once again, the code now informs you as the player how much money the banker has offered you. You then choose deal or no deal. If you accept the deal the code tells you how much you have won. If you reject the deal the code tells you to continue.
#Once again the code asks you to pick a briefcase between the number 1-26. If you do not pick one from 1-26 it will ask you to do that. It also asks you to eliminate one briefcase, tells you which one you eliminated and how much money you lost.
  delay_print("The banker is thinking of a deal")
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  #Once again the banker thinks of a deal whilst making "waiting emojis".
  delay_print("The banker offers you $" + str(offer()))
  time.sleep(2)
  delay_print("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  deal_or_no4 = input()
  delay_print(deal_or_no4)
  if deal_or_no4 == "deal":
    delay_print("You have won " + str(offer()))
    exit()
  else:
    delay_print("Ok, let's continue!")
    delay_print("Now you have 2 cases left, pick either your personal(1) case or the remaining case(2) to take home the money in that case ")

  final_choice = input()
  if final_choice == 1:
    delay_print("You have won " + player_briefcase)
  elif final_choice == 2:

    delay_print("You won" + briefcases(remaining_briefcases))

    delay_print("You won" + briefcases(remaining_briefcases))
#For the final time, the banker offers the player a deal. If they accept this deal the code tells them they have won the money they have won. If they reject the deal the code says lets continue.
#The code then informs them the player they can either pick their personal briefcase or the remaining briefcase. The player then types 1 or 2 for their final choice and wins that money. Are you lucky or unlucky?
    delay_print("You won" + briefcases(player_briefcase))
#For the final time, the banker offers the player a deal. If they accept this deal the code tells them they have won the money they have won.
#  If they reject the deal the code says lets continue.The code then informs them the player they can either pick their personal briefcase or the remaining briefcase. 
# The player then types 1 or 2 for their final choice and wins that money. Are you lucky or unlucky?

    delay_print("You won" + briefcases(remaining_briefcases))
#For the final time, the banker offers the player a deal. If they accept this deal the code tells them they have won the money they have won. If they reject the deal the code says lets continue.
#The code then informs them the player they can either pick their personal briefcase or the remaining briefcase. The player then types 1 or 2 for their final choice and wins that money. Are you lucky or unlucky?

