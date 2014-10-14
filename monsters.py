#This file will be used to store monster stats and if they appear etc.

import random
#import "mud/ArmorStats.py"

#Setting Armor Ranges
noArmor = random.randint(3,5)
leatherArmor = random.randint(6,8)
chainArmor = random.randint(9,11)
plateArmor = random.randint(12,14)
PossibleArmor = [noArmor,leatherArmor,chainArmor,plateArmor]

#Goblin | Level 1

#Setting Goblins Health, Speed, Stamina, Dexterity, Strength
goblinHealth = random.randint(7,14)
goblinSpeed = random.randint(3,7)
goblinStamina = 20
goblinDexterity = random.randint(3,18)
goblinStrength = random.randint(3,19)

#Setting Goblins Armor
goblinArmor = random.choice(PossibleArmor)
#Setting Goblin Armor Type
if goblinArmor < 6 :
  goblinArmortype = "None"
elif 6 <= goblinArmor <= 8 :
  goblinArmortype = "Leather"
elif 9 <= goblinArmor <= 11 :
  goblinArmortype = "Chain Mail"
elif 12 <= goblinArmor <= 14 :
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
print("Goblin Stats: \n------------\nHealth: " + str(goblinHealth) + "\nSpeed: " + str(goblinSpeed) + "\nStamina: " + str(goblinStamina) + "\nDexterity: " + str(goblinDexterity) + "\nStrength: " + str(goblinStrength) + "\nArmor: " + str(goblinArmor) + " : " + str(goblinArmortype))
