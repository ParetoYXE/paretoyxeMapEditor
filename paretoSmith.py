import random,pygame


pygame.init()





gameDisplay = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('The DMZ')
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('VCR_OSD_MONO', 40,)
clock = pygame.time.Clock()

w, h = pygame.display.get_surface().get_size()


quit = False


Region = 0
prevRegion = 0
OverWorldHeight = 8
OverWorldWidth = 16
regionWidth = 16
regionHeight = 11
Legend = {}
Images = {}
Screens = []
screenTransition = False
backGroundColor = [252,216,168]
for i in range(OverWorldWidth*OverWorldHeight):
	Screens.append([])



def loadLegend():
	file1 = open("Legend.txt",'r')
	Lines =  file1.readlines()
	for i in Lines: 
		if(i[0]!="#"):
			arr = i.split()
			Legend.update({arr[0]:arr[1]})
			image = pygame.image.load(arr[1])
			Images.update({arr[0]:image})

def loadScreens():
	global Screens,Region
	# Using readlines() 
	file1 = open('Screens.txt', 'r') 
	Lines = file1.readlines() 
	 

	for line in Lines: 
		if(line[0]!="#"):
			arr = line.split()
			coorX = int(arr[0])
			coorY = int(arr[1])
			mapFile = arr[2]
			with open(mapFile) as f:
				content = f.readlines()
				for i in content:
					i = i.split()
					Screens[coorY*OverWorldWidth+coorX].append(i)


def renderMap():
	global screenTransition
	tileX = round(w / regionWidth)
	tileY = round(h / regionHeight)
	xPos = 0
	yPos = 0

	map = []
	map2 = []
	if(screenTransition):
		for i in Screens[Region]:
			for j in i:
				map.append(j)
		count = 0


		for i in range(0,regionWidth):
			for j in range(0,regionHeight):
				tile = map[j*16+i]
				if(tile != '0'):
					gameDisplay.blit(pygame.transform.scale(Images[tile],(tileX,tileY)),(xPos,yPos))
				elif(tile == '0'):
					pygame.draw.rect(gameDisplay, backGroundColor, pygame.Rect(xPos,yPos, tileX, tileY)) 
				yPos+=tileY
			pygame.time.wait(10)
			pygame.display.update()	
			xPos+=tileX
			yPos = 0

		screenTransition = False
	else:
		for i in Screens[Region]:
			for j in i:
				map.append(j)

		count = 0

		for i in range(0,regionWidth):
			for j in range(0,regionHeight):
				tile = map[j*16+i]
				if(tile != '0'):
					gameDisplay.blit(pygame.transform.scale(Images[tile],(tileX,tileY)),(xPos,yPos))
				elif(tile == '0'):
					pygame.draw.rect(gameDisplay, backGroundColor, pygame.Rect(xPos,yPos, tileX, tileY)) 
				yPos+=tileY
			xPos+=tileX
			yPos = 0



loadLegend()
loadScreens()

while not quit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			playerAttack = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quit = True
			if event.key == pygame.K_d:
				screenTransition = True
				prevRegion = Region
				Region+=1
			if event.key == pygame.K_a:
				screenTransition = True
				prevRegion = Region
				Region-=1
			if event.key == pygame.K_s:
				screenTransition = True
				prevRegion = Region
				Region+=16
			if event.key == pygame.K_w:
				screenTransition = True
				prevRegion = Region
				Region-=16



	
	print(Region)
	if(not screenTransition):
		gameDisplay.fill(backGroundColor)
	renderMap()
	pygame.display.update()
	clock.tick(60)



pygame.quit()