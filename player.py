import pygame



player = {"xLocation":1,"yLocation":1,"tileX":1,"tileY":1}
playerImage = pygame.image.transform(pygame.image.load('tree.png'),(tileX,tileY))


def renderPlayer(gameSurface):
	gameSurface.blit(playerImage,(player["xLocation"]*tileX,player["yLocation"]*tileY))
