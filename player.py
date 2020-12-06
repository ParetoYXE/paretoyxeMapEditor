import pygame








player = {"xLocation":1,"yLocation":1,"tileX":1,"tileY":1}
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

def playerMovement(movement):
	if(movement == "right"):
		player["xLocation"] +=1
	elif(movement == "left"):
		player["xLocation"] -=1
	elif(movement == "up"):
		player["yLocation"] -=1
	elif(movement == "down"):
		player["yLocation"] +=1

