#Attempting to make a mud like game
#Author: Brad Riley

import random
import time

#player name
playName = input('What is your name? ')

#skills
health = random.randint(10,100)
mana = random.randint(10,50)
strength = random.randint(1,10)
magic = random.randint(1,10)
marksman = random.randint(1,10)

print('Your skills are: ')
print('Your Health is: ' + str(health))
print('Your Mana is: ' + str(mana))
print('Your Strength skill level is: ' + str(strength))
print('Your Magic skill level is: ' + str(magic))
print('Your Marksman skill level is: ' + str(marksman))


#reroll skills

skillChange = input('Would you like to re roll these skills? (yes/no): ')
while skillChange == 'yes':
    health = random.randint(10,100)
    mana = random.randint(10,50)
    strength = random.randint(1,10)
    magic = random.randint(1,10)
    marksman = random.randint(1,10)
    print('Your skills are: ')
    print('Your Health is: ' + str(health))
    print('Your Mana is: ' + str(mana))
    print('Your Strength skill level is: ' + str(strength))
    print('Your Magic skill level is: ' + str(magic))
    print('Your Marksman skill level is: ' + str(marksman))
    skillChange = input('Would you like to re roll these skills? (yes/no): ')

#Map Logic

genSurr = random.randint(1,4)
if genSurr == 1:
    genSurr = 'a door'
elif genSurr == 2:
    genSurr = 'it bends left.'
elif genSurr == 3:
    genSurr = 'it bends right.'
elif genSurr == 4:
    genSurr = 'the way goes straight'

#start

maxHealth = health
maxMana = mana
currentLevel = 1

while health > 0:
    location = input('You see a dungeion entrace... do you enter? ')
    if location == 'No':
        print('You fall off a cliff.')
        health -= maxHealth
    go = input('You look ahead, ' + genSurr)








#On Death

print('Oh no you died! You were level ' + str(currentLevel))
