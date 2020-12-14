import random,pygame,json
import player as playerObject
import mobs as mobsController

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
OverWorldHeight = 8
OverWorldWidth = 16
regionWidth = 16
regionHeight = 11
tileX = round(w / regionWidth)
tileY = round(h / regionHeight)
Legend = {}
Images = {}
Screens = []
mobs = {}
localMobs = [] 
overWorldMode = False



for i in range(OverWorldWidth*OverWorldHeight):
	Screens.append([])
	localMobs.append([])


def loadMobs():
	file1 = open("mobs.txt",'r')
	Lines =  file1.readlines()
	for i in Lines: 
		if(i[0]!='#'):
			arr = i.split()
			mobs[arr[0]] = eval(arr[1])
	print(mobs)

def loadLocalMobs():
	global OverWorldWidth
	file1 = open('masterMobs.txt', 'r') 
	Lines = file1.readlines() 
	for line in Lines: 
		if(line[0]!="#"):
			arr = line.split()
			name = str(arr[0])
			coorX = int(arr[1])
			coorY = int(arr[2])
			tileX = int(arr[3])
			tileY = int(arr[4])
			region = coorY*OverWorldWidth+coorX
			temp = localMobs[region]
			temp.append({'name':name,'coorX':coorX,'coorY':coorY,'tileX':tileX,'tileY':tileY})
			image = pygame.image.load(mobs[name]['image'])
			Images.update({name:image})
			localMobs[region] = temp

	print(localMobs)
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

def renderMobs():
	for i in localMobs[Region]:
		mob = mobs[i['name']]
		gameDisplay.blit(pygame.transform.scale(Images[i["name"]],(round(mob['tileX']*tileX),round(mob['tileY']*tileY))),(i["tileX"]*tileX,i["tileY"]*tileY))



def mobAI():
	for i in localMobs[Region]:
		if(len(i)>0):
			i = mobsController.mobsAI(i,mobs)

		

def renderMap():
	xPos = 0
	yPos = 0

	for i in Screens[Region]:
		for j in i:
			if(j != '0'):
				gameDisplay.blit(pygame.transform.scale(Images[j],(tileX,tileY)),(xPos,yPos))
			xPos+=tileX	
		yPos+=tileY
		xPos = 0

loadMobs()
loadLegend()
loadScreens()
loadLocalMobs()
playerObject.playerInit(0,0,tileX,tileY)

aiTimer = 0

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
				if(not overWorldMode):
					playerObject.playerMovement("right")
				else:
					Region+=1
			if event.key == pygame.K_a:
				if(not overWorldMode):
					playerObject.playerMovement("left")
				else:
					Region-=1
			if event.key == pygame.K_s:
				if(not overWorldMode):
					playerObject.playerMovement("down")
				else:
					Region+=16
			if event.key == pygame.K_w:
				if(not overWorldMode):
					playerObject.playerMovement("up")
				else:
					Region-=16
			if event.key == pygame.K_LSHIFT:
				overWorldMode = not overWorldMode


	gameDisplay.fill([252,216,168])
	#pygame.time.wait(200) #Used to control time process time for AI and player actions. This should be tweaked to use a counter rather then a interupt.
	if(aiTimer > 60):
		aiTimer = 0
		mobAI()
	else:
		aiTimer+=1

	print(aiTimer)
	renderMap()
	renderMobs()
	playerObject.renderPlayer(gameDisplay)
	pygame.display.update()
	clock.tick(60)



pygame.quit()