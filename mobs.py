import random
import player as playerObject

def mobsAI(mob):
	xLocation = mob['tileX']
	yLocation = mob['tileY']


	if(mob["name"]=="oldMan"):
		xLocation += random.randint(-1,1)
		yLocation += random.randint(-1,1)

	mob['tileX'] = xLocation
	mob['tileY'] = yLocation
	
	return mob