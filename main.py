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
  offer = 0
  for x in briefcases.values():
    val = val+x
  offer = val/len(briefcases)
  offer = round(offer, 2)
  return offer   

def f_select_briefcases(val):
  global briefcases
  while len(remaining_briefcases) > val:  
    delay_print("Choose a briefcase to eliminate\n ")
    user_choice = input()
    if int(user_choice) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases between 1 to 26")
    else:
      pygame.mixer.music.play(1)
      pygame.mixer.music.stop()
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
    delay_print("You have won " + str(offer(briefcases)) + " dollars")
    exit()
  else:
    print()
    delay_print("Ok, let's continue!\n")


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

    passwordentry = Entry(root, show="*")


    nameentry.grid(row=1, column=3)
    passwordentry.grid(row=2, column=3)

    checkbtn = Checkbutton(text="remember me?", variable= checkvalue)
    checkbtn.grid(row=6, column=3)

   
    Button(text="Submit", command=getvals).grid(row=7, column=3 )
    root.mainloop()


    delay_print("Do you know the rules\n")
    user_tutorial = input()
  
  elif guest_or_sign_in.lower() == "1":
    delay_print("You are playing as a guest\n")
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
  delay_print("There are 26 briefcases ranging from values from one dollar to one million dollars. \n")
  time.sleep(1)
  delay_print("You must now choose to keep one briefcase safe from elimination this is known as your personal briefcase. \n")
  time.sleep(1)
  delay_print("You will eliminate 6 briefcases of your choice. \n")
  time.sleep(1)
  delay_print("After this the bank will make an offer, it is your choice to accept the offer or not. \n")
  time.sleep(1)
  delay_print("If you take the deal then you will walk away with that amount of money and the game will end.\n ")
  time.sleep(1)
  delay_print("If you do not take the offer then you will choose another six briefcases to eliminate. \n")
  time.sleep(1)
  delay_print("Then the banker will make another offer this will continue until either the contestant chooses a deal or they reach the last two remaining briefcases. \n")
  time.sleep(1)
  delay_print("If the contestant reaches the last two remaining briefcases then the contestant must select one and the contestant will get the amount of money in the leftover briefcase. \n")
else:
  delay_print("Let's Start\n")



#The above code are the rules explained to the player once they agree to play the game. If they do not want to play the game, the game replies with "That's sad" and ends the code.
briefcases = f_briefcases()
while yes_or_no.lower() == "yes":
  delay_print("Pick your personal case from the numbers between 1 and 26!\n ")
  player_briefcase = int(input())
 # Below line is to remove the selected item from the list
  remaining_briefcases.pop(remaining_briefcases.index(int(player_briefcase)))
  f_select_briefcases(20)
  f_select_briefcases(14)
  f_select_briefcases(8)
  f_select_briefcases(2)
  f_select_briefcases(1)
  #The above repeats the define which runs the game
  delay_print("Now choose between your personal briefcase(1) and the last remaining briefcase(2)\n")
  final_choice = input()
  if final_choice == 1:
     delay_print("You have won " + briefcases(player_briefcase))
  elif final_choice == 2:
    delay_print("You won" + str(briefcases([remaining_briefcases])))
  else:
    delay_print("Please restart and enter a valid answer")
    exit()

