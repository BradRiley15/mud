 #Attempt at making a MUD Game. By: Bradly Riley and Andrew Hecky
 """
 So first things first, we should set variable names, so everyone knows what the variables are, and so they stay
 the same throughout the enitre code.
 """
 """
 Global Variables:
 ------------------
 - 
 """
 """
 Player Variables:
 -----------------
 - playerName
	- "playerName" is the variable that sets the name of the person/user playing the game. It is set at the beginning
			game's instance. Once saves are incorperated, it will stay the same throughout the game save, and will
			change with every new game started.
 - playerMaxhealth
 	- "playerMaxHealth" is the maximum amount of health the player can have at a certain time. Max Health will 
 			incrase when the player levels up. It is set to a certain integer (either random or static, that 
 			is unknown yet) at the beginning of the game.
 - playerHealth
 	- "playerHealth' is the variable that tells the game how much health the player has at a certain point in time 
 			throughout the game. It is set to a "playerMaxhealth" at the beginning of the game. Health will be 
 			deducted from "playerHealth" due to combat, traps, falling, etc. Once "playerHealth" reaches 0, the	
 			player is dead, and the game will end. (Checkpoints may be added)
 - playerMaxmana
 	- "playerMaxmana" is the maximum amount of mana the player can have at a certain time. Max Mana will 
 			incrase when the player levels up. It is set to a certain integer (either random or static, that 
 			is unknown yet) at the beginning of the game.
 - playerMana
 	- "playerMana" is the amount of mana your character has at any given time. Mana determines if you can cast 
 			certain spells. Casting spells uses a predetermined amount of mana based on how powerful the spells are.
 - playerSpeed
 	- "playerSpeed" is the speed of the player. Speed determines who attacks first in combat. Speed is set at the
 			beginning of the game, it will be a random integer between a certain range. Speed may be increased when
 			the player levels up (when levels are added).
 - playerStrength
 	- "playerStrength" is the strength of the player. The more strength you have, the more damage you do with melee
 			weapons in combat. Strength may increase when the player levels up (When levels are added)
 - playerDexterity
 	- "playerDexterity" is the dexterity of the player. The higher your dexterity, the more damage you deal with 
 			ranged weapons. The player will also gain Armor bounuses if there dexterity is high enough. Dexterity
 			may increase when the player levels up (When levels are added)
 - playerMagic
 	- "playerMagic" tells the game what kind of spells you can cast, and how much damage they do. When you level up,
 			You will unlock more spells, and the spells you have will do more damage
 - playerArmor
 	- "playerArmor" is the amount of armor the player has. The more armor you have, the harder it is for an enemy 
 			hit you. The player has the option to buy armor in towns, for a price. The armor choices are
 			"Cloth" (Least Protection), "Leather" (Decent Protection), "Chain Mail" (Good Protection), and
 			"Plate" (Most Protection).
 - playerExperience
 	- "playerExperience" is the amount of experince (a.k.a "XP") the player has. Killing enemies and making smart 
 			decisions will gain the player experience (XP). Once the player reaches a certain amount of experience
 			the player will level up.
 - playerWeapon
 	- "playerWeapon" tells the combat system what kind of weapon the player is using. Different weapons can do
 			different amounts of damage. Weapons can be purchased in towns, but only certain races/classes can use
 			certain weapons.
 """

 """			
Monster/Enemy Variables: (For these variables, replace "(enemy)" with the name of the monster.
(Ex. "(enemy)Health" would be "goblinHealth" if the enemy was a Goblin.)
------------------------
 - (enemy)Maxhealth
 	- "(enemy)MaxHealth" is the maximum amount of health the enemy can have at a certain time. Max Health will 
 			incrase based on the level of the enemy.
 - (enemy)Health
 	- "(enemy)Health' is the variable that tells the game how much health the enemy has at a certain point in time 
 			throughout the game.  Health will be deducted from "(enemy)Health" due to combat and traps. Once 
 			"(enemy)Health" reaches 0, the enemy is dead. Once an enemy is dead, he will no longer attack, and
 			the player will gain experience
 - (enemy)Maxmana
 	- "(enemy)Maxmana" is the maximum amount of mana the enemy can have at a certain time. Max Mana will 
 			incrase based on the level of the monster. It is set to a certain integer (either random or static, 
 			that is unknown yet) at the beginning of the game.
 - (enemy)Mana
 	- "(enemy)Mana" is the amount of mana the enemy has at any given time. Mana determines if the enemy can cast 
 			certain spells. Casting spells uses a predetermined amount of mana based on how powerful the spells are.
 - (enemy)Speed
 	- "(enemy)Speed" is the speed of the enemy. Speed determines who attacks first in combat. Speed is set at the
 			beginning of the game, it will be a random integer between a certain range. Speed may be increased
 			based on the level of the monster.
 - (enemy)Strength
 	- "(enemy)Strength" is the strength of the enemy. The more strength the enemy has, the more damage the enemy will
 			do with melle attacks in combat. Strength may increase based on the level of the enemy.
 - (enemy)Dexterity
 	- "(enemy)Dexterity" is the dexterity of the enemy. The higher the dexterity, the more damage the enemy will deal 
 			with ranged weapons. The enemy will also gain Armor bounuses if there dexterity is high enough. Dexterity 
 			may increase based on the level of the enemy.
 - (enemy)Magic
 	- "(enemy)Magic" tells the game what kind of spells the enemy can cast, and how much damage they do. The enemy
 			will have different more powerful spells based on their level.
 - (enemy)Armor
 	- "(enemy)Armor" is the amount of armor the enemy has. The more armor the enemy has, the harder it is for the
 			the player to hit the enemy. The enemy spawns with a random set of armor equiped.
 - (enemy)Weapon
 	- "(enemy)Weapon" tells the combat system what kind of weapon the enemy is using. Different weapons will do
 			different amounts of damage. Enemies spawn with a randomly selected weapon. Certain enemies can't spawn
 			with certain weapons.
"""
