#This is where combat functions will be


def combatEncounter():
  #Setting Function Variables
  outOfCombat = "noCombat"
  playerTurn = "playerTurn"
  enemyTurn = "enemy1Turn"
  playerCombatTurn = "-"
  player_Suicide = "-"
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
    while combatTurn == playerTurn :
      #Player Chooses What To Do
      print("What do you want to do? ")
      print("You can (A)ttack, (R)un, (T)alk, (S)uicide, or do (N)othing. ")
      playerCombatTurn = input("Choice: ")[0].upper()
      #Deciding if Player Choice Is Valid
      while not valid_CombatTurn :
        if playerCombatTurn == "A" :
          valid_CombatTurn = True
        elif playerCombatTurn == "R" :
          valid_CombatTurn = True
        elif playerCombatTurn == "T" :
          valid_CombatTurn = True
        elif playerCombatTurn == "S" :
          valid_CombatTurn = True
        elif playerCombatTurn == "N" :
          valid_CombatTurn = True
        else :
          valid_CombatTurn = False
          print("\nYou cannot do that!")
          print("You can only (A)ttack, (R)un, (T)alk, (S)uicide, or do (N)othing. ")
          playerCombatTurn = input("Choice: ")[0].upper()
      #If Player Chooses To Commit Suicide
      if playerCombatTurn == "S" :
        print("\nYou draw your sword, holding it with the point of it's blade pressed against your chest. ")
        player_Suicide = input("Are you sure? (Y/N): ")[0].upper()
        #Confirming if player really wants to commit suicide
        if player_Suicide == "Y" :
          print("You take your readied sword and plunge it deep into your chest, killing you almost instantly. ")
          playerHealth = 0
          valid_CombatTurn = False
          playerCombatTurn = "-"
          break
        elif player_Suicide == "N" :
          print("You lower your sword, deciding not to kill yourself. ")
          valid_CombatTurn = False
          playerCombatTurn = "-"
        elif player_Suicide !="Y"

#If Player Dies
while playerHealth <= 0 :
  print("Game Over...")
