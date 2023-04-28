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
  print("Great! Now that you want to play lets learn the rules")
  time.sleep(3)
  print("There are 26 briefcases ranging from values from one dollar to one million dollars.")
  time.sleep(3)
  print("You must now choose to keep one briefcase safe from elimination this is known as your personal briefcase.")
  time.sleep(3)
  print("You will eliminate 6 briefcases of your choice.")
  time.sleep(3)
  print("After this the bank will make an offer, it is your choice to accept the offer or not.")
  time.sleep(3)
  print("If you take the deal then you will walk away with that amount of money and the game will end.")
  time.sleep(3)
  print("If you do not take the offer then you will choose another six briefcases to eliminate.")
  time.sleep(3)
  print("Then the banker will make another offer this will continue until either the contestant chooses a deal or they reach the last two remaining briefcases.")
  time.sleep(4)
  print("If the contestant reaches the last two remaining briefcases then the contestant must select one and the contestant will get the amount of money in the leftover briefcase.")
else:
  print("That's sad!")
  exit()

while yes_or_no.lower() == "yes":
  player_briefcase = int(input("Pick your personal case from the numbers between 1 and 26!\n "))
  # Below line is to remove the selected item from the list
  remaining_briefcases.pop(remaining_briefcases.index(int(player_briefcase)))
  while len(remaining_briefcases) > 20:  
    user_choice1 = input("Choose a briefcase to eliminate\n ") 
    if int(user_choice1) not in remaining_briefcases:
      print("Sorry, you can only choose from briefcases between 1 to 26")
    else:
      print("You eliminated " + str(briefcases[int(user_choice1)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice1)))

  print("The banker is thinking of a deal")
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)

  print("The banker offers you $" + str(offer())) 
  time.sleep(2)
  deal_or_no = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no)
  if deal_or_no == "deal":
    print("You have won " + str(offer()))
    exit()
  else:
    print("Ok, let's continue!")
  while len(remaining_briefcases) > 14:
    user_choice2 = input("Pick a briefcase that you have not chosen ")
    if int(user_choice2) not in remaining_briefcases:
      print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      print("You eliminated " + str(briefcases[int(user_choice2)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice2)))
 
  print("The banker is thinking of a deal")
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)

  print("The banker offers you $" + str(offer()))
  time.sleep(2)
  deal_or_no1 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no1)
  if deal_or_no1 == "deal":
    print("You have won " + str(offer()))
    exit()
  else:
    print("Ok, let's continue!")
  while len(remaining_briefcases) > 8:
    user_choice3 = input("Pick a briefcase that you have not chosen ")
    if int(user_choice3) not in remaining_briefcases:
      print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      print("You eliminated " + str(briefcases[int(user_choice3)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice3)))
  print("The banker is thinking of a deal")
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)

  print("The banker offers you $" + str(offer()))
  time.sleep(2)
  deal_or_no2 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no2)
  if deal_or_no2 == "deal":
    print("You have won " + str(offer()))
    exit()
  else:
    print("Ok, let's continue!")
  while len(remaining_briefcases) > 2:
    user_choice4 = input("Pick a briefcase that you have not chosen ")
    if int(user_choice4) not in remaining_briefcases:
      print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      print("You eliminated " + str(briefcases[int(user_choice4)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice4)))
  print("The banker is thinking of a deal")
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)

  print("The banker offers you $" + str(offer()))
  time.sleep(2)
  deal_or_no3 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no3)
  if deal_or_no3 == "deal":
    print("You have won " + str(offer()))
    exit()
  else:
    print("Ok, let's continue!")
  while len(remaining_briefcases) > 1:
    user_choice5 = input("Pick a briefcase that you have not chosen ")
    if int(user_choice5) not in remaining_briefcases:
      print("Sorry, you can only choose from briefcases going from 1 to 26")
    else:
      print("You eliminated " + str(briefcases[int(user_choice5)]) + " Dollar/s")
      remaining_briefcases.pop(remaining_briefcases.index(int(user_choice5)))
  print("The banker is thinking of a deal")
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)
  print(".")
  time.sleep(1.2)
  
  print("The banker offers you $" + str(offer()))
  time.sleep(2)
  deal_or_no4 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no4)
  if deal_or_no4 == "deal":
    print("You have won " + str(offer()))
    exit()
  else:
    print("Ok, let's continue!")
  final_choice = input("Now you have 2 cases left, pick either your personal(1) case or the remaining case(2) to take home the money in that case ")
  if final_choice == 1:
    print(player_briefcase)
  elif final_choice == 2:
    print(remaining_briefcases)
  