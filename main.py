import random

briefcases = {1:1, 2:5, 3:10, 4:20, 5:50, 6:100, 7:200, 8:300, 9:1000, 10:1500, 11:2000, 12:3000, 13:5000, 14:7000, 15:10000, 16:20000, 17:30000, 18:50000, 19:70000, 20:100000, 21:150000, 22:200000, 23:300000, 24:500000, 25:750000, 26:1000000}
remaining_briefcases = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
<<<<<<< HEAD
<<<<<<< HEAD
yes_or_no = input(print("Welcome new player! Would you like to play a game of deal no deal? Say yes to play, or no to not play"))
=======
yes_or_no = input("Welcome new player! Would you like to play a game of deal no deal?\n")
>>>>>>> 55aa793c06d1850da6695fe6871e590285e6671d
=======
yes_or_no = input(print("Welcome new player! Would you like to play a game of deal no deal?"))
>>>>>>> parent of d754118 (Update main.py)

if yes_or_no.lower() == "yes":
  print("Let's start!")
else:
  print("How sad!")
