#This file will be used to store monster stats and if they appear etc.

#Setting Armor Ranges
noArmor = random.randint(3,5)
leatherArmor = random.randint(6,8)
chainArmor = random.randint(9,11)
plateArmor = random.randint(12,14)
PossibleArmor = [noArmor,leatherArmor,chainArmor,plateArmor]

#Goblin | Level 1
import random
#import "mud/ArmorStats.py"

#Setting Goblins Health, Speed, Stamina, Dexterity, Strength
goblinHealth = random.randint(7,14)
goblinSpeed = random.randint(3,7)
goblinStamina = 20
goblinDexterity = random.randint(3,18)
goblinStrength = random.randint(3,19)

#Setting Goblins Armor
goblinArmor = random.choice(PossibleArmor)
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
  
print("Goblin Stats: \n------------\nHealth: " + str(goblinHealth) + "\nSpeed: " + str(goblinSpeed) + "\nStamina: " + str(goblinStamina) + "\nDexterity: " + str(goblinDexterity) + "\nStrength: " + str(goblinStrength) + "\nArmor: " + str(goblinArmor))
