#The purpose of this file is to create a generic set of interactions between the player and mobs. Be it 
#negative or positive. These interactions can be used to form general interaction patterns for each specific mob
#such as "Talk","Attack","Flee"

import random
import player as playerObject
import mobs as mobs







#This interaction does nothing but indicate there was indeed an interaction
def ghost_interaction():
	return 'Interaction'




#The player takes a random amount of damage.
def damage_interaction():
	upperBound = 1
	lowerBound = 0

	playerObject.player["health"] -= random.randint(lowerBound,upperBound)




def push_interaction():
	#randomlyPushPlayer
	playerObject.player["xLocation"] += random.randint(-1,1)
	playerObject.player["yLocation"] += random.randint(-1,1)













