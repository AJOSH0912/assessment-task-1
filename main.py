import random
import os
import time


playAgain = 1

winnerNames = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:''}
winnerValues = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:''}


while playAgain != 2:

  hiddenCase = {0:' 1 ', 1:' 2 ', 2:' 3 ', 3:' 4 ', 4:' 5 ', 5:' 6 ', 6:' 7 ', 7:' 8 ', 8:' 9 ', 9:' 10 ', 10:' 11 ', 11:' 12 ', 12:' 13 ', 13:' 14 ', 14:' 15 ', 15:' 16 ', 16:' 17 ', 17:' 18 ', 18:' 19 ', 19:' 20 ', 20:' 21 ', 21:' 22 ', 22:' 23 ', 23:' 24 ', 24:' 25 ', 25:' 26 '}

  case = {0:'0.01', 1:' 1  ', 2:' 5  ', 3:' 10 ', 4:' 25 ', 5:' 50 ', 6:' 75 ', 7:'100 ', 8:'200 ', 9:'300 ', 10:'400 ', 11:'500 ', 12:'750 ', 13:' 1K ', 14:' 5K ', 15:'10K ', 16:'25K ', 17:'50K ', 18:'75K ', 19:'100K', 20:'200K', 21:'300K', 22:'400K', 23:'500K', 24:'750K', 25:' 1M '}

  caseValues = {0:0.01, 1:1, 2:5, 3:10, 4:25, 5:50, 6:75, 7:100, 8:200, 9:300, 10:400, 11:500, 12:750, 13:1000, 14:5000, 15:10000, 16:25000, 17:50000, 18:75000, 19:100000, 20:200000, 21:300000, 22:400000, 23:500000, 24:750000, 25:1000000}

  excludedValues = []

  playerCase = {1:''}

  totalValues = 0

  offer = 1

  def checkValuesOff(pCase):

    if case[pCase] == '0.01':
      caseValues[0] = '    '

    if case[pCase] == ' 1  ':
      caseValues[1] = ' '

    if case[pCase] == ' 5  ':
      caseValues[2] = ' '

    if case[pCase] == ' 10 ':
      caseValues[3] = '  '

    if case[pCase] == ' 25 ':
      caseValues[4] = '  '

    if case[pCase] == ' 50 ':
      caseValues[5] = '  '

    if case[pCase] == ' 75 ':
      caseValues[6] = '  '

    if case[pCase] == '100 ':
      caseValues[7] = '   '

    if case[pCase] == '200 ':
      caseValues[8] = '   '

    if case[pCase] == '300 ':
      caseValues[9] = '   '

    if case[pCase] == '400 ':
      caseValues[10] = '   '

    if case[pCase] == '500 ':
      caseValues[11] = '   '

    if case[pCase] == '750 ':
      caseValues[12] = '   '

    if case[pCase] == ' 1K ':
      caseValues[13] = '    '

    if case[pCase] == ' 5K ':
      caseValues[14] = '    '

    if case[pCase] == '10K ':
      caseValues[15] = '     '

    if case[pCase] == '25K ':
      caseValues[16] = '     '

    if case[pCase] == '50K ':
      caseValues[17] = '     '

    if case[pCase] == '75K ':
      caseValues[18] = '     '

    if case[pCase] == '100K':
      caseValues[19] = '      '

    if case[pCase] == '200K':
      caseValues[20] = '      '

    if case[pCase] == '300K':
      caseValues[21] = '      '

    if case[pCase] == '400K':
      caseValues[22] = '      '

    if case[pCase] == '500K':
      caseValues[23] = '      '

    if case[pCase] == '750K':
      caseValues[24] = '      '

    if case[pCase] == ' 1M ':
      caseValues[25] = '       '



  def printCases():

    print(' -----      -----      -----      -----      -----      -----      ----- ')
    print('|', hiddenCase[0] + ' |    |', hiddenCase[1] + ' |    |', hiddenCase[2] + ' |    |', hiddenCase[3] + ' |    |', hiddenCase[4] + ' |    |', hiddenCase[5] + ' |    |', hiddenCase[6] + ' |         ', caseValues[0], '           ', caseValues[13])
    print(' -----      -----      -----      -----      -----      -----      -----             ', caseValues[1], '           ', caseValues[14])
    print('                                                                                     ', caseValues[2], '          ', caseValues[15])
    print('      -----      -----      ------     ------     ------     ------                 ', caseValues[3], '          ', caseValues[16])
    print('     |', hiddenCase[7] + ' |    |', hiddenCase[8] + ' |    |', hiddenCase[9] + ' |   |', hiddenCase[10] + ' |   |', hiddenCase[11] + ' |   |', hiddenCase[12] + ' |                ', caseValues[4], '          ', caseValues[17])
    print('      -----      -----      ------     ------     ------     ------                 ', caseValues[5], '          ', caseValues[18])
    print('                                                                                    ', caseValues[6], '         ', caseValues[19])
    print(' ------     ------     ------     ------     ------     ------     ------          ', caseValues[7], '         ', caseValues[20])
    print('|', hiddenCase[13] + ' |   |', hiddenCase[14] + ' |   |', hiddenCase[15] + ' |   |', hiddenCase[16] + ' |   |', hiddenCase[17] + ' |   |', hiddenCase[18] + ' |   |', hiddenCase[19] + ' |         ', caseValues[8], '         ', caseValues[21])
    print(' ------     ------     ------     ------     ------     ------     ------          ', caseValues[9], '         ', caseValues[22])
    print('                                                                                   ', caseValues[10], '         ', caseValues[23])
    print('      ------     ------     ------     ------     ------     ------                ', caseValues[11], '         ', caseValues[24])
    print('     |', hiddenCase[20] + ' |   |', hiddenCase[21] + ' |   |', hiddenCase[22] + ' |   |', hiddenCase[23] + ' |   |', hiddenCase[24] + ' |   |', hiddenCase[25] + ' |               ', caseValues[12], '        ', caseValues[25])
    print('      ------     ------     ------     ------     ------     ------ ')
    print('\n')


  def makingChoice(selections, roundGame):
    #making selections
    os.system('clear')
    for n in range(selections, 0, -1):
      
      #printing cases
      printCases()
      
      #choosing case // clearing text
      print('Round', roundGame)
      print('you have', str(n), 'more selections')
      
      pCase = input('which case would you like to choose : ')
      while pCase == '' or not(pCase == '26' or pCase == '25' or pCase == '24' or pCase == '23' or pCase == '22' or pCase == '21' or pCase == '20' or pCase == '19' or pCase == '18' or pCase == '17' or pCase == '16' or pCase == '15' or pCase == '14' or pCase == '13' or pCase == '12' or pCase == '11' or pCase == '10' or pCase == '9' or pCase == '8' or pCase == '7' or pCase == '6' or pCase == '5' or pCase == '4' or pCase == '3' or pCase == '2' or pCase == '1' or pCase == '27'):
        pCase = input('please pick a valid case : ')
      pCase = int(pCase)
      pCase = pCase - 1

      if  pCase in excludedValues or pCase == playerCase[1]:
        pCase = input('please pick a valid case : ')
        pCase = int(pCase)
        pCase = pCase - 1
      checkValuesOff(pCase)

      os.system('clear')
      time.sleep(0.2)

      print(' you chose case', hiddenCase[pCase])
      if len(str(hiddenCase[pCase])) == 3:
        print('      -----')
        print('     | ' + hiddenCase[pCase] + ' |')
        print('      -----')
      else:
        print('      ------')
        print('     | ' + hiddenCase[pCase] + ' |')
        print('      ------')
      time.sleep(0.15)

      for e in range(3, 0, -1):
        print('opening case in', e)

        time.sleep(0.35)

      excludedValues.append(pCase)

      os.system('clear')

      if case[pCase] == ' 10 ' or case[pCase] == ' 25 ' or case[pCase] == ' 50 ' or case[pCase] == ' 75 ' or case[pCase] == ' 1K ' or case[pCase] == ' 5K ' or case[pCase] == '100K' or case[pCase] == '200K' or case[pCase] == '300K' or case[pCase] == '400K' or case[pCase] == '500K' or case[pCase] == '750K' or case[pCase] == ' 1M ' or case[pCase] == '0.01' :
        print(' ------\n| ' + case[pCase] + ' |\n ------')
        time.sleep(1.5)
        os.system('clear')
      else:
        print(' -----\n| ' + case[pCase] + '|\n -----')
        time.sleep(1.5)
        os.system('clear')


      if len(str((hiddenCase[pCase]))) == 3:
        hiddenCase[pCase] = '   '
      else:
        hiddenCase[pCase] = '    '


  def firstSelection():
    printCases()
    print('Your first selection is for your case\nYou will have this case until the very end of the game\n')
    pCaseOriginal = (input('\nWhich case would you like to choose : '))
    while pCaseOriginal == '':
      pCaseOriginal = (input('please pick a valid case : '))
    pCaseOriginal = int(pCaseOriginal)
    pCaseOriginal = pCaseOriginal - 1
    while pCaseOriginal < 0 or pCaseOriginal > 25 or pCaseOriginal == '':
      pCaseOriginal = int(input('please pick a different case : '))
      pCaseOriginal = pCaseOriginal - 1
    print(' your case is', hiddenCase[pCaseOriginal])
    if len(str((hiddenCase[pCaseOriginal]))) == 3:
      print('      -----')
      print('     | ' + hiddenCase[pCaseOriginal] + ' |')
      print('      -----')
    else:
      print('      ------')
      print('     | ' + hiddenCase[pCaseOriginal] + ' |')
      print('      ------')
