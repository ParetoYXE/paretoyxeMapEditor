import random
import player as playerObject
import playerMobInteractions as interactions


map = []
width = 0
height = 0

def mobsAI(mob,mobs,localmap,regionWidth,regionHeight):

	global map, width, height 
	map = localmap
	width = regionWidth
	height = regionHeight

	print(mob)
	if(mobs[mob["name"]]["type"]=="random"):
		mob = randomAI(mob)
	elif(mobs[mob["name"]]["type"]=="approach"):
		mob = approachAI(mob)
	elif(mobs[mob["name"]]["type"]=="stationary"):
		mob = stationaryAI(mob)

	return mob




def randomAI(mob):
	xLocation = mob["tileX"]
	yLocation = mob["tileY"]

	wonder = True
	while(wonder):
		oldxLocation = mob["tileX"]
		oldyLocation = mob["tileY"]
		xLocation += random.randint(-1,1)
		yLocation += random.randint(-1,1)

		if(xLocation > width or yLocation > height):
			print("test"+str(height))
			mob["tileX"] = oldxLocation
			mob["tileY"] = oldyLocation
		else:
			mob["tileX"] = xLocation
			mob["tileY"] = yLocation

		if(not collisionDetection(mob,map)):
			wonder = False
		else:
			mob["tileX"] = oldxLocation
			mob["tileY"] = oldyLocation



	playerCollision(mob)
	return mob


def stationaryAI(mob):
	if(playerCollision(mob)):
		interactions.damage_interaction()
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

	
	if playerCollision(mob):
		pass #put interaction here
	return mob


def playerCollision(mob):
	if(playerObject.player["xLocation"] == mob["tileX"] and playerObject.player["yLocation"] == mob["tileY"]):
		return True

def collisionDetection(mob,map):

	print(map[mob["tileY"]][mob["tileX"]])
	if((map[mob["tileY"]][mob["tileX"]]) in ['a','b','c','d','e','f']):
		return True
	else:
		if(int(map[mob["tileY"]][mob["tileX"]]) < 1):
			return False
		else:
			return True

