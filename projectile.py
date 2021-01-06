#This class tracks all projectiles on a screen. Once the player exits a screen the local 
#projectiles are wiped




projectiles = []


def createProjectile(xLocation,yLocation,direction,name):
	projectiles.append({"x":xLocation,"y":yLocation,"direction":direction,"name":name})




def projectileVelocity():
	for i in range(0,len(projectiles)):
		direction = projectiles[i]["direction"]
		projectiles[i]["x"] += direction[0]
		projectiles[i]["y"] += direction[1]


def clearProjectiles():
	projectiles = []


