import pygame








player = {"xLocation":1,"yLocation":1,"tileX":1,"tileY":1}
playerImage = ''

def playerInit(xlocation,yLocation,tileX,tileY):
	player["xLocation"] = xLocation
	player["yLocation"] = yLocation
	player["tileX"] = tileX
	player["tileY"] = tileY

	playerImage = pygame.transform.scale(pygame.image.load('tree.png'),(player["tileX"],player["tileY"]))


def renderPlayer(gameSurface):
	gameSurface.blit(playerImage,(player["xLocation"]*tileX,player["yLocation"]*tileY))
