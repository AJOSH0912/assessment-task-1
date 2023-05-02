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
remaining_briefcases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

def offer():
  val = 0
  for x in briefcases:
    val = val+briefcases[x]
  return val/len(briefcases)  

def shuffle():
  keys = list(briefcases.keys())
  random.shuffle(keys)
  shuffled_briefcases = dict()
  for i in keys:
    shuffled_briefcases.update({i: briefcases[keys]})
  return shuffled_briefcases


shuffled_briefcases = shuffle


yes_or_no = input("Welcome new player! Would you like to play a game of deal no deal?\n ") 

if yes_or_no.lower() == "yes":
  user_tutorial = input("Do you know the rules?")
else:
  delay_print("That's sad!")
  exit()
  
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
  print("Let's Start")

while yes_or_no.lower() == "yes":
  player_briefcase = int(input("Pick your personal case from the numbers between 1 and 26!\n "))
  # Below line is to remove the selected item from the list
  remaining_briefcases.pop(remaining_briefcases.index(int(player_briefcase)))
  while len(remaining_briefcases) > 20:  
    user_choice1 = input("Choose a briefcase to eliminate\n ") 
    if int(user_choice1) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases between 1 to 26")
    else:
      delay_print("You eliminated " + str(briefcases[int(user_choice1)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice1)))
    print()

  delay_print("The banker is thinking of a deal")
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)

  delay_print("The banker offers you $" + str(offer())) 
  print()
  time.sleep(2)
  deal_or_no = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  delay_print(deal_or_no)
  if deal_or_no == "deal":
    print()
    delay_print("You have won " + str(offer()))
    exit()
  else:
    print()
    delay_print("Ok, let's continue!")
  while len(remaining_briefcases) > 14:
    user_choice2 = input("Pick a briefcase that you have not chosen ")
    if int(user_choice2) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      delay_print("You eliminated " + str(briefcases[int(user_choice2)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice2)))
 
  delay_print("The banker is thinking of a deal")
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)

  delay_print("The banker offers you $" + str(offer()))
  time.sleep(2)
  deal_or_no1 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  delay_print(deal_or_no1)
  if deal_or_no1 == "deal":
    delay_print("You have won " + str(offer()))
    exit()
  else:
    delay_print("Ok, let's continue!")
  while len(remaining_briefcases) > 8:
    user_choice3 = input("Pick a briefcase that you have not chosen ")
    if int(user_choice3) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      delay_print("You eliminated " + str(briefcases[int(user_choice3)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice3)))
  delay_print("The banker is thinking of a deal")
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)

  delay_print("The banker offers you $" + str(offer()))
  time.sleep(2)
  deal_or_no2 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  delay_print(deal_or_no2)
  if deal_or_no2 == "deal":
    delay_print("You have won " + str(offer()))
    exit()
  else:
    delay_print("Ok, let's continue!")
  while len(remaining_briefcases) > 2:
    user_choice4 = input("Pick a briefcase that you have not chosen ")
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

  delay_print("The banker offers you $" + str(offer()))
  time.sleep(2)
  deal_or_no3 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  delay_print(deal_or_no3)
  if deal_or_no3 == "deal":
    delay_print("You have won " + str(offer()))
    exit()
  else:
    delay_print("Ok, let's continue!")
  while len(remaining_briefcases) > 1:
    user_choice5 = input("Pick a briefcase that you have not chosen ")
    if int(user_choice5) not in remaining_briefcases:
      delay_print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      delay_print("You eliminated " + str(briefcases[int(user_choice5)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice5)))
  delay_print("The banker is thinking of a deal")
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  delay_print(".")
  time.sleep(1.2)
  
  delay_print("The banker offers you $" + str(offer()))
  time.sleep(2)
  deal_or_no4 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  delay_print(deal_or_no4)
  if deal_or_no4 == "deal":
    delay_print("You have won " + str(offer()))
    exit()
  else:
    delay_print("Ok, let's continue!")
  final_choice = input("Now you have 2 cases left, pick either your personal(1) case or the remaining case(2) to take home the money in that case ")
  if final_choice == 1:
    delay_print("You have won " + player_briefcase)
  elif final_choice == 2:
    delay_print(briefcases(player_briefcase))