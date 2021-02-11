import pygame








player = {"xLocation":1,"yLocation":1,"tileX":1,"tileY":1,'direction': '', 'health':1}
playerImage = ''

def playerInit(xLocation,yLocation,tileX,tileY):
	global playerImage
	player["xLocation"] = xLocation
	player["yLocation"] = yLocation
	player["tileX"] = tileX
	player["tileY"] = tileY

	playerImage = pygame.transform.scale(pygame.image.load('npc.png'),(player["tileX"],player["tileY"]))


def renderPlayer(gameSurface):
	gameSurface.blit(playerImage,(player["xLocation"]*player["tileX"],player["yLocation"]*player["tileY"]))

def playerMovement(movement,map):
	player["direction"] = movement
	if(movement == "right"):
		player["xLocation"] +=1
		if(collisionDetection(map)):
			player["xLocation"] -=1
	elif(movement == "left"):
		player["xLocation"] -=1
		if(collisionDetection(map)):
			player["xLocation"] +=1
	elif(movement == "up"):
		player["yLocation"] -=1
		if(collisionDetection(map)):
			player["yLocation"] +=1
	elif(movement == "down"):
		player["yLocation"] +=1
		if(collisionDetection(map)):
			player["yLocation"] -=1


def collisionDetection(map):
	if(player["yLocation"] < len(map) and player["xLocation"] < len(map[0])):
		if(isinstance(map[player["yLocation"]][player["xLocation"]], str):
		   return True
		else:
			if(int(map[player["yLocation"]][player["xLocation"]]) < 1 or int(map[player["yLocation"]][player["xLocation"]]) == 9):
				return False
			else:
				return False

