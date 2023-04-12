
briefcases = {1:1, 2:5, 3:10, 4:20, 5:50, 6:100, 7:200, 8:300, 9:1000, 10:1500, 11:2000, 12:3000, 13:5000, 14:7000, 15:10000, 16:20000, 17:30000, 18:50000, 19:70000, 20:100000, 21:150000, 22:200000, 23:300000, 24:500000, 25:750000, 26:1000000}
remaining_briefcases = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
yes_or_no = input("Welcome new player! Would you like to play a game of deal no deal?\n")



if yes_or_no.lower() == "yes":
  print("Let's start!")
else:
  print("That's sad!")

while yes_or_no.lower() == "yes":
  player_briefcase = int(input("Pick a case between 1 and 26!\n"))
  # Below line is to remove the selected item from the list
  remaining_briefcases.pop(player_briefcase)
  remaining_briefcases.insert(int(player_briefcase), "Done")

  while len(remaining_briefcases) > 1:
    user_choice1 = input("Choose a briefcase to eliminate\n")
    print("You eliminated " + str(briefcases[int(user_choice1)]))
    remaining_briefcases.pop(int(user_choice1))
    remaining_briefcases.insert(int(user_choice1), "Done")
    print("Pick a briefcase from this:" + str(remaining_briefcases))
    