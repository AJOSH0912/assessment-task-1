import random
from tkinter import * 
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()
from tkinter import*
briefcases = {1:1, 2:5, 3:10, 4:20, 5:50, 6:100, 7:200, 8:300, 9:1000, 10:1500, 11:2000, 12:3000, 13:5000, 14:7000, 15:10000, 16:20000, 17:30000, 18:50000, 19:70000, 20:100000, 21:150000, 22:200000, 23:300000, 24:500000, 25:750000, 26:1000000}
remaining_briefcases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
random.shuffle(briefcases)
print(briefcases)

  keys = list(briefcases.keys())
  random.shuffle(keys)
  shuffled_briefcases = dict()
  for i in keys:
    shuffled_briefcases.update({i: briefcases[keys]})
  return shuffled_briefcases

yes_or_no = input("Welcome new player! Would you like to play a game of deal no deal?\n ")

if yes_or_no.lower() == "yes":
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

else: print("That's sad!")
  

root.mainloop()
#exit()
  
print(''' Great! Now that you want to play lets lern the rules! There are 26 briefcases ranging from
  values from one dollar to one million dollars.You must now choose to keep one briefcase safe from elimination 
  this is known as your personal briefcase.It can only be opened if you make it to the end of the game.
  You will eliminate 6 briefcases of your choice.
  After this the bank will make an offer, it is your choice to accept the offer or not. If you
  take the deal then you will walk away with that amount of money and the game will end. If you do not
  take the offer then you will choose another six briefcases to eliminate. Then the banker will make
  another offer this will continue until either the contestant chooses a deal or they reach the last 
  two remaining briefcases. If the contestant reaches the last two remaining briefcases then the contestant
  must select one and the contestant will get the amount of money in the leftover briefcase.''')

print()
player_briefcase = int(input("Pick your personal case from the numbers between 1 and 26!\n "))
  #else:
  #print("That's sad!")
  #root.mainloop()
  #exit()
while yes_or_no.lower() == "yes":
  
  # Below line is to remove the selected item from the list
  remaining_briefcases.pop(remaining_briefcases.index(int(player_briefcase)))
  while len(remaining_briefcases) > 20:  
    user_choice1 = input("Choose a briefcase to eliminate\n ") 
    if int(user_choice1) not in remaining_briefcases:
      print("Sorry, you can only choose from briefcases going from 1 to 26")
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

  value1 = random.randrange(1, 1000000)
  print("The banker offers you $" + str(value1))
  time.sleep(2)
  deal_or_no = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no)
  if deal_or_no == "deal":
    print("You have won $ " + str(value1))
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

  value2 = random.randrange(1, 1000000)
  print("The banker offers you $" + str(value2))
  time.sleep(2)
  deal_or_no1 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no1)
  if deal_or_no1 == "deal":
    print("You have won $ " + str(value2))
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

  value3 = random.randrange(1, 1000000) 
  print("The banker offers you $" + str(value3))
  time.sleep(2)
  deal_or_no2 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no2)
  if deal_or_no2 == "deal":
    print("You have won $" + str(value3))
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

  value4 = random.randrange(1, 1000000)
  print("The banker offers you $" + str(value4))
  time.sleep(2)
  deal_or_no3 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no3)
  if deal_or_no3 == "deal":
    print("You have won $" + str(value4))
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
  
  value5 = random.randrange(1, 1000000)
  print("The banker offers you $" + str(value5))
  time.sleep(2)
  deal_or_no4 = input("Do you accept this offer(deal) or do you reject this offer(no deal) ")
  print(deal_or_no4)
  if deal_or_no4 == "deal":
    print("You have won $" + str(value5))
    exit()
  else:
    print("Ok, let's continue!")
  final_choice = input("Now you have 2 cases left, pick either your personal(1) case or the remaining case(2) to take home the money in that case ")
  if final_choice == 1:
    print(player_briefcase)
  elif final_choice == 2:
    print(remaining_briefcases)
  