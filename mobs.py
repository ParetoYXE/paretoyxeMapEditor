import random
import player as playerObject



map = []
width = 0
def mobsAI(mob,mobs,localmap,regionWidth):

	global map, width 
	map = localmap
	width = regionWidth

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
	xLocationOld = xLocation
	yLocationOld = yLocation
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

	if(not collisionDetection(mob,map)):
		pass
	else:
		mob["tileX"] = xLocationOld
		mob["tileY"] = yLocationOld 

	return mob


def collisionDetection(mob,map):

	print(map[mob["tileY"]][mob["tileX"]])
	if(int(map[mob["tileY"]][mob["tileX"]]) < 1):
		return False
	else:
		return True
