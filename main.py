import random
import time
import sys

briefcases = {1:1, 2:5, 3:10, 4:20, 5:50, 6:100, 7:200, 8:300, 9:1000, 10:1500, 11:2000, 12:3000, 13:5000, 14:7000, 15:10000, 16:20000, 17:30000, 18:50000, 19:70000, 20:100000, 21:150000, 22:200000, 23:300000, 24:500000, 25:750000, 26:1000000}
remaining_briefcases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

def offer():
  val = 0
  for x in briefcases:
    if x in remaining_briefcases:
      val = val+briefcases[x]
  return val/len(briefcases)  

def shuffle():
  print("I am here")
  keys = list(briefcases.keys())
  random.shuffle(keys)
  shuffled_briefcases = dict()
  for i in keys:
    shuffled_briefcases.update({i: briefcases[keys]})
  return shuffled_briefcases


shuffle

yes_or_no = input("Welcome new player! Would you like to play a game of deal no deal?\n")

if yes_or_no.lower() == "yes":
  print(''' Great! Now that you want to play lets lern the rules! There are 26 briefcases ranging from
  values from one dollar to one million dollars.You must now choose to keep one briefcase safe from elimination, 
  this is known as your personal briefcase.You will eliminate 6 briefcases of your choice.
  After this the bank will make an offer, it is your choice to accept the offer or not. If you
  take the deal then you will walk away with that amount of money and the game will end. If you do not
  take the offer then you will choose another six briefcases to eliminate. Then the banker will make
  another offer this will continue until either the contestant chooses a deal or they reach the last 
  two remaining briefcases. If the contestant reaches the last two remaining briefcases then the contestant
  must select one and the contestant will get the amount of money in the leftover briefcase.''')
else:
  print("That's sad!")
  exit()

while yes_or_no.lower() == "yes":
  player_briefcase = int(input("Pick your personal case from the numbers between 1 and 26!\n"))
  # Below line is to remove the selected item from the list
  remaining_briefcases.pop(remaining_briefcases.index(int(player_briefcase)))
  while len(remaining_briefcases) > 19:  
    user_choice1 = input("Choose a briefcase to eliminate\n") 
    if int(user_choice1) not in remaining_briefcases:
      print("You have allready chosen this")
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

  deal_or_no = input("Do you accept this offer(1) or do you reject this offer(2)")
  print(deal_or_no)
  if deal_or_no == "1":
    print("You have won " + str(offer()))
    exit()
  else:
    print("Ok, let's continue!")
  while len(remaining_briefcases) > 13:
    user_choice2 = input("Pick a briefcase that you have not chosen")
    if int(user_choice2) not in remaining_briefcases:
      print("You have allready chosen this")
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

  deal_or_no = input("Do you accept this offer(1) or do you reject this offer(2)")
  print(deal_or_no)
  if deal_or_no == "1":
    print("You have won " + str(offer()))
    exit()
  else:
    print("Ok, let's continue!")
  while len(remaining_briefcases) > 6:
    user_choice2 = input("Pick a briefcase that you have not chosen")
    if int(user_choice1) not in remaining_briefcases:
      print("You have allready chosen this")
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

  deal_or_no = input("Do you accept this offer(1) or do you reject this offer(2)")
  print(deal_or_no)
  if deal_or_no == "1":
    print("You have won " + str(offer()))
    exit()
  else:
    print("Ok, let's continue!")
  while len(remaining_briefcases) > 3:
    user_choice2 = input("Pick a briefcase that you have not chosen")
    if int(user_choice1) not in remaining_briefcases:
      print("You have allready chosen this")
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

  deal_or_no = input("Do you accept this offer(1) or do you reject this offer(2)")
  print(deal_or_no)
  if deal_or_no == "1":
    print("You have won " + str(offer()))
    exit()
  else:
    print("Ok, let's continue!")