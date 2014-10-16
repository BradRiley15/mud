#This is where combat functions will be


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
  global outOfCombat
  global playerTurn
  global enemy1Turn
  
  #Setting Who Has First Turn
  combatTurn = outOfCombat
  if playerSpeed > enemySpeed :
    combatTurn = playerTurn
  if playerSpeed < enemySpeed :
    combatTurn = enemy1Turn

  #Actual Combat
  while playerHealth > 0 and enemyHealth > 0 :
  valid_CombatTurn = empty
    while combatTurn == playerTurn :
      #Player Chooses What To Do
      print("What do you want to do? ")
      print("You can (A)ttack, (R)un, (T)alk, (S)uicide, or do (N)othing. ")
      playerCombatTurn = input("Choice: ")[0].upper()
      #Deciding if Player Choice Is Valid
      while not valid_CombatTurn :
    #If Player Chooses To Attak
        if playerCombatTurn == "A" :
          valid_CombatTurn = True

    #If Player Chhoses To Run
        elif playerCombatTurn == "R" :
          valid_CombatTurn = True
          print("You turn and attempt to run! ")
          escapeChance = random.randit(1,20)
          if escapeChance > 13 :
            print("You escape successfully! ")
          
  
    #If Player Chooses To Talk
        elif playerCombatTurn == "T" :
          valid_CombatTurn = True
  
    #If Player Chooses To Commit Suicide
        elif playerCombatTurn == "S" :
          valid_CombatTurn = True
          while playerCombatTurn == "S" :
            print("\nYou draw your sword, holding it with the point of it's blade pressed against your chest. ")
            player_Suicide = input("Are you sure? (Y/N): ")[0].upper()
        #Confirming if player really wants to commit suicide
            if player_Suicide == "Y" :
              print(\n"You take your readied sword and plunge it deep into your chest, killing you almost instantly. ")
              playerHealth = 0
              valid_CombatTurn = False
              playerCombatTurn = empty
              player_Suicide = empty
            elif player_Suicide == "N" :
              print("\nYou lower your sword, deciding not to kill yourself. ")
              valid_CombatTurn = False
              playerCombatTurn = empty
              player_Suicide = empty
            elif player_Suicide !="Y" or player_Suicide !="N" : #or player_Suicide !="--"
              print("\nThat is not a valid option. ")
              player_Suicide = input("Commit Suicide? (Y/N): ")[0].upper()
            print(" ")
    #If Player Choosees To Do Nothing      
        elif playerCombatTurn == "N" :
          valid_CombatTurn = True
          while playerCombatTurn == "N" :
            print("Not moving a muscle, you stand still and do nothing. ")
            combatTurn = enemyTurn
            playerCombatTurn = empty
     #If Player Chooses Invalid Option
        else :
          valid_CombatTurn = False
          print("\nYou cannot do that!")
    #Plater Re-Selects What They Want To Do 
        if playerHealth > 0 :
          print("What do you want to do? ")
          print("You can (A)ttack, (R)un, (T)alk, (S)uicide, or do (N)othing. ")
          playerCombatTurn = input("Choice: ")[0].upper()



#If Player Dies
while playerHealth <= 0 :
  print("Game Over...")
