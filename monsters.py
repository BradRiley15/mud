#This file will be used to store monster stats and if they appear etc.

import random
#import "mud/ArmorStats.py"

#Setting Armor Stats
noArmor = 6
clothArmor = 8
leatherArmor = 10
chainArmor = 12
plateArmor = 14
PossibleArmor = [noArmor,clothArmor,leatherArmor,chainArmor,plateArmor]

#Goblin | Level 1

#Setting Goblins Health, Speed, Stamina, Dexterity, Strength
goblinHealth = random.randint(7,14)
goblinSpeed = random.randint(3,7)
goblinDexterity = random.randint(3,18)
goblinStrength = random.randint(3,19)

#Setting Goblins Armor
goblinArmor = random.choice(PossibleArmor)
#Setting Goblin Armor Type
if goblinArmor = 6 :
  goblinArmortype = "None"
elif goblinArmor = 8 :
  goblinArmortype = "Cloth"
elif goblinArmor = 10 :
  goblinArmortype = "Leather"
elif goblinArmor = 12 :
  goblinArmortype = "Chain"
elif goblinArmor = 14 : 
  goblinArmortype = "Plate" 

#Possible Armor Buffs
if goblinDexterity > 13 :
  goblinArmor = goblinArmor + 1
if goblinDexterity > 15 :
  goblinArmor = goblinArmor + 2
if goblinDexterity > 17 :
  goblinArmor = goblinArmor + 3
  
#Possible Hit Buff
if goblinDexterity > 13 :
  goblinHitbuff = 3

#Print Goblin Stats (For Testing)

print("|=============|")
print("| For Testing |")
print("|=============|")
print("Goblin Stats: \n------------\n Health: " + str(goblinHealth) + "\n Speed: " + str(goblinSpeed) + "\n Stamina: " + str(goblinStamina) + "\n Dexterity: " + str(goblinDexterity) + "\n Strength: " + str(goblinStrength) + "\n Armor: " + str(goblinArmor) + " (" + str(goblinArmortype) + ") ")
