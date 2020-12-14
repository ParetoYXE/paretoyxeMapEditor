import random
import player as playerObject

def mobsAI(mob,mobs):

	print(mob)
	if(mobs[mob["name"]]["type"]=="random"):
		mob = randomAI(mob)
	elif(mobs[mob["name"]]["type"]=="approach"):
		mob = approachAI(mob)

	return mob





def randomAI(mob):
	xLocation = mob["tileX"]
	yLocation = mob["tileY"]

	xLocation += random.randint(-1,1)
	yLocation += random.randint(-1,1)

	mob["tileX"] = xLocation
	mob["tileY"] = yLocation

	return mob


def approachAI(mob):
	xLocation = mob["tileX"]
	yLocation = mob["tileY"]
	playerX = playerObject.player['xLocation']
	playerY = playerObject.player['yLocation']

	if(xLocation < playerX):
		xLocation+=1
	elif(xLocation > playerX):
		xLocation-=1

	if(yLocation < playerY):
		yLocation +=1
	elif(yLocation > playerY):
		yLocation -=1



	mob["tileX"] = xLocation
	mob["tileY"] = yLocation
	return mob
