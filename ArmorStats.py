#Armor
"""
- No Armor
  - Armor Range 3-5
- Leather Armor
  - Armor Range 6-8
- Chain Mail Armor
  - Armor Range 9-11
- Plate Armor
  - Armor Range 12-14
  
if Dexterity > 13 then Armor = + 1
if Dexterity > 15 then Armor = + 2
if Dexterity > 17 then Armer = + 3
"""
import random

#No Armor
noArmor = random.randint(3,5)

#Leather
leatherArmor = random.randint(6,8)

#Chain Mail Armor
chainmailArmor = random.randint(9,11)

#Plate Armor
plateArmor = random.randint(12,14)

#Function to run armor
"""
playArmor = 0
def Armor():
  if playDex > 13:
    playArmor += 1
  if playDex > 15:
    playArmor +=2
  if playDex > 17:
    playArmor +=3

"""
