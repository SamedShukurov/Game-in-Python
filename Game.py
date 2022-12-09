import random #pythonu başlatmaq üçün terminalda (visual studio kodunkunu deyirəm) belə yane (python game.py) yaz ki açılsın 
import time #ümumiyətlə hər hansı bir pythonu işə salmaq üçün sən terminaldan və ya exe proqramından istifadə edə bilərsən.

print("----Rock, paper , scirrors , lizard , spock") #daş,kağızkərtənkələ, qapaq
print("---------------------------------------------")
print("Welcome to the game!") # Oyuna Xoş gəldiz!
print("The game consist of 5 rounds") # Oyun 5 rauntdan ibarətdir.
print("The winner is the one who has more points.")#Çox BAL yığan qazanandır!
print("\t[r] - rock\n\t[s] - scissors\n\t[p] - paper\n\t[l] - lizard\n\t[k] - spock")
# Bu oyunu asanlıqla udmaq üçün hər rauntda code sözü yazın!



print("---------------------------------------------")
print("-----------------START GAME------------------")
def repeator(): # funksiya yaradırıq ki bu oyunu təkrarlamaq olsun
 player_score = 0
 player_select = 0
 player_win = 0
 comp_score = 0
 comp_select = 0
 comp_win = 0
 player_win_code = 0
 for i in range(5):# roundların sayı  və ya neçədənə round olacağı bir kod
     print("\t\n---------Round Number " + str(i + 1) + " --")
     comp_select = random.choice("rsplk")
     while True:
         player_select = input("\tYour select: ")
         if (player_select == "r") or (player_select == "s") or (player_select == "p") or (player_select == "l") or (player_select == "k") or player_select == ("code"):
             break
         else:
           print("\tError. print another object!")
     print("\tComputer: " + comp_select)
     if player_select == comp_select:
      print("\t\tDraw")
     elif player_select == "r" and comp_select == "s":
      player_score = player_score + 1
      print("\t\tYou win this round!")
     elif player_select == "r" and comp_select == "l":
      player_score = player_score + 1
      print("\t\tYou win this round!")
     elif player_select == "r" and comp_select == "p":
      comp_score = comp_score + 1
      print("\t\tComputer win this round!")
     elif player_select == "r" and comp_select == "k":
      comp_score = comp_score + 1
      print("\t\tComputer win this round!")
     elif player_select == "p" and comp_select == "r":
       player_score = player_score + 1
       print("\t\tYou win this round!")
     elif player_select == "p" and comp_select == "s":
       comp_score = comp_score + 1
       print("\t\tComputer win this round!")
     elif player_select == "p" and comp_select == "l":
       comp_score = comp_score + 1
       print("\t\tComputer win this round!")
     elif player_select == "p" and comp_select == "k":
       comp_score = comp_score + 1
       print("\t\tComputer win this round!")
     elif player_select == "s" and comp_select == "p":
       player_score = player_score + 1
       print("\t\tYou win this round!")
     elif player_select == "s" and comp_select == "r":
       comp_score = comp_score + 1
       print("\t\tComputer win this round!")
     elif player_select == "s" and comp_select == "l":
       player_score = player_score + 1
       print("\t\tYou win this round!")
     elif player_select == "s" and comp_select == "k":
       comp_score = comp_score + 1
       print("\t\tComputer win this round!")
     elif player_select == "l" and comp_select == "r":
       comp_score = comp_score + 1
       print("\t\tComputer win this round!") 
     elif player_select == "l" and comp_select == "s":
       comp_score = comp_score + 1
       print("\t\tComputer win this round!") 
     elif player_select == "l" and comp_select == "p":
       player_score = player_score + 1
       print("\t\tYou win this round!")
     elif player_select == "l" and comp_select == "k":
       player_score = player_score + 1
       print("\t\tYou win this round!")
     elif player_select == "k" and comp_select == "r":
       player_score = player_score + 1
       print("\t\tYou win this round!")
     elif player_select == "k" and comp_select == "s":
       player_score = player_score + 1
       print("\t\tYou win this round!")
     elif player_select == "code" and comp_select == "r":
       player_score = player_score + 100
       print("\t\tYou win with secret C0DE!!!!")
     elif player_select == "code" and comp_select == "s":
       player_score = player_score + 100010
       print("\t\tYou win with secret C0DE!!!!")
     elif player_select == "code" and comp_select == "p":
       player_score = player_score + 101010101011010
       print("\t\tYou win with secret C0DE!!!!")
     elif player_select == "code" and comp_select == "l":
       player_score = player_score + 5
       print("\t\tYou win with secret C0DE!!!!")
     elif player_select == "code" and comp_select == "k":
       player_score = player_score + 10
       print("\t\tYou win with secret C0DE!!!!")
 print("\n---------------------------------------------")
 print(f"-----------------Game Result--- You:{player_score}  Comp:{comp_score}")
 if player_score > comp_score:
    print("Congralulations! You win!")
    player_win = player_win + 1
 elif player_score < comp_score:
    print("Sorry... The computer wins!")
    comp_win = comp_win + 1
 else:
    print("Draw!")
repeator()
while True:
  yon = input(" Try again?[print y or n]: ")
  if (yon == "y") or (yon == "Y"):
     repeator()
  if (yon == "n") or (yon == "N"):
     break
  else:
    print("You have typed something wrong...")
print("Thank you for playing this game.I have no so much time to do game like this ,but nobody said that, I can't fix it.And yeah if this computer are making you angry Just type (code) to Win without fun ;)  ")
print("\n\n\n\t\t\tGame by Samed  =)")
time.sleep(15)
