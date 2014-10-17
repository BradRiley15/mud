#This is where combat functions will be

#Author: Andrew Hecky
#Date First Started: 10/14/2014
#Date Last Edited : 10/17/2014

def combatEncounter():
  #Setting Function Variables
  empty = "--"
    #Combat Turn Variables
  outOfCombat = "noCombat"
  playerTurn = "playerTurn"
  enemyTurn = "enemy1Turn"
    #Player Turn Variables
  playerCombatTurn = "--"
  player_Suicide = "--"
  valid_CombatTurn = False
  
  #Import Global Variables
  global 
  
  #Setting Who Has First Turn
  combatTurn = outOfCombat
  if playerSpeed > enemySpeed :
    combatTurn = playerTurn
  if playerSpeed < enemySpeed :
    combatTurn = enemy1Turn

#Actual Combat

#Loop 1 : playerHealth, enemyHealth, combatTurn
  while playerHealth > 0 and enemyHealth > 0 and (combatTurn != outOfCombat) :
  
                        #While Players Turn
#Loop 2 : combatTurn 
    while combatTurn == playerTurn :
  #Setting Choice To False to Run Loop
      valid_CombatTurn = False
#Loop 3 : valid_CombatTurn
      while not valid_CombatTurn :
  
  #Player Chooses What To Do
        print("What do you want to do? ")
        print("You can (A)ttack, (R)un, (T)alk, (S)uicide, or do (N)othing. ")
        playerCombatTurn = input("Choice: ")[0].upper()
  
  #If Player Chooses To Attak
        if playerCombatTurn == "A" :
          valid_CombatTurn = True

  #If Player Chooses To Run (Complete : Needs Tested)
        elif playerCombatTurn == "R" :
          valid_CombatTurn = True
          print("You turn and attempt to run! ")
          escapeChance = random.randit(1,20)
      #If Player Escapes Successfully
          if escapeChance > 13 :
            print("You escape successfully! ")
            combatTurn = outOfCombat
            playerCombatTurn = empty
      #If Player Can't Escape
          elif escapeChange <= 13
            print("Oh no! You cannot escape! ")
            cobatTurn = enemyTurn
            playerCombatTurn = empty
  
  #If Player Chooses To Talk
        elif playerCombatTurn == "T" :
          valid_CombatTurn = True
  
  #If Player Chooses To Commit Suicide (Complete : Needs Tested)
        elif playerCombatTurn == "S" :
#Loop 4 : playerCombatTurn is "S"
          while playerCombatTurn == "S" :
            print("\nYou draw your sword, holding it with the point of it's blade pressed against your chest. ")
      #Confirming if player really wants to commit suicide
            player_Suicide = input("Are you sure? (Y/N): ")[0].upper()
          #Player Wants To Commit Suicide
            if player_Suicide == "Y" :
              print(\n"You take your readied sword and plunge it deep into your chest, killing you almost instantly. ")
              playerHealth = 0
              valid_CombatTurn = True
              playerCombatTurn = empty
              player_Suicide = empty
              combatTurn = outOfCombat
          #Player Doesn't Want To Commit Suicide
            elif player_Suicide == "N" :
              print("\nYou lower your sword, deciding not to kill yourself. ")
              valid_CombatTurn = False
              playerCombatTurn = empty
              player_Suicide = empty
          #If Player Chooses Else
            elif player_Suicide !="Y" or player_Suicide !="N" : #or player_Suicide !="--"
              print("\nThat is not a valid option. ")
              player_Suicide = input("Commit Suicide? (Y/N): ")[0].upper()
              
  #If Player Choosees To Do Nothing (Complete : Needs Testes)
        elif playerCombatTurn == "N" :
          valid_CombatTurn = True
          print("Not moving a muscle, you stand still and do nothing. ")
          combatTurn = enemyTurn
          playerCombatTurn = empty
  
  #If Player Chooses Invalid Option (Complete : Needs Tested)
        else :
          valid_CombatTurn = False
          print("\nYou cannot do that!")

""" 
***This block is currently removed, code I added earier in the loop should make this block obsolete.***
#Player Re-Selects What They Want To Do 
        if playerHealth > 0 and not valid_CombatTurn :
          print("What do you want to do? ")
          print("You can (A)ttack, (R)un, (T)alk, (S)uicide, or do (N)othing. ")
          playerCombatTurn = input("Choice: ")[0].upper()
"""


  #If Player Dies
while playerHealth <= 0 :
  print("Game Over...")
