#Attempting to make a mud like game
#Author: Brad Riley

import random
import time

#Player name
playName = input('What is your name? ')

#Skills
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


#Reroll skills

skillChange = input('Would you like to re roll these skills? (yes/no): ')
while skillChange == 'yes':
    health = random.randint(30,100)
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
    genSurr = 'a door: '
elif genSurr == 2:
    genSurr = 'it bends left: '
elif genSurr == 3:
    genSurr = 'it bends right: '
else:
    genSurr = 'the way goes straight: '


#Monster Logic

monChan = 1
if monChan ==1:
    monChan = '...the way is clear...'
else:
    monChan = 'Oh no theres a goblin! You cant run!'


#Goblin
staticGoblinHp = 7
goblinAtk = random.randint(5, 15)
goblinChan = random.randint(1,19)
goblinHp = 7
#Goblin Skills
#health = random.randint(5,40)
#mana = random.randint(10,50)
#strength = random.randint(1,10)
#magic = random.randint(1,10)
#marksman = random.randint(1,10)

#start

maxHealth = health
maxMana = mana
currentLevel = 1
xp = 0

#Introduction
start = input('You see a dungeion entrace... do you enter? ')
if start == 'No':
    print('You fall off a cliff.')
    health -= maxHealth

#While in dungeon
while health > 0:
    go = input('You look ahead, ' + genSurr)
    if go == 'Continue':
        monChan = random.randint(1,2)
        if monChan == 2:
            print('Oh no! there is a Goblin! You cannot run!')
            while goblinHp > 0:
                playac = input("What will you attack with? (magic, strength, or marksman? ")
                if playac == 'magic':
                    chanHit = random.randint(1,10+magic)
                    if chanHit > 11:
                            damage = random.randint(1,magic)
                            print('You hit the golin, for' + str(damage) + '!')
                            goblinHp -= damage
                    if chanHit < 11:
                            print('YOU MISSED!!!!!')
                    chanHit = random.randint(1,10+magic)
                if goblinChan > 11:
                    print('The goblin wounded you with its spear, dealing ' + str(goblinAtk) + '.')
                    health -= goblinAtk
                    print('Careful! You have ' + str(health) + ' health left')
                if goblinChan < 11:
                    print('THE GOBLIN MISSED!')
                goblinAtk = random.randint(5, 15)
                goblinChan = random.randint(1,19)
                if health < 0:
                    break
        goblinHp = staticGoblinHp
        xp += 5
        if xp == 20:
            print('Congragulations you leveled up!')
            currentLevel += 1
        if monChan == 1:
            print('The way is clear....for now...')
            ############Where I am at
        
        







#On Death

print('Oh no you died! You were level ' + str(currentLevel))
