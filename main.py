from ursina import *
import random
app = Ursina()

from ursina.prefabs.platformer_controller_2d import PlatformerController2d
player = PlatformerController2d(y=1, z=.01, scale_y=1, max_jumps=2, texture="Assets/player", color=color.white)
player.start_position = (1, 0.1)

class Enemy(Entity):
    def __init__(self,x,y):
        super().__init__()
        self.model = 'cube'
        self.color = color.green
        self.x = x
        self.y = y
        self.collider = 'box'
        
    def onCollision(self):
        if self.intersects(player).hit:
            return True

class Trap(Entity):
    def __init__(self, x, y, player):
        super.__init__()
        self.model='quad',
        self.scale_x = 10,
        self.collider='box', 
        self.color = color.purple
        self.x = x
        self.y = y
        self.player = player
    
    def onCollision(self):
        if self.intersects(player.hit):
            return True

enemy1 = Enemy(4, 5)

x=0

#Starting Platform
for i in range(6):
    ground = Entity(model='quad', scale_x=1, collider='box', texture='Assets/grass', x=x, y=0)
    x+=0.95

def makePlatform(num):
    for x in range(num):
        pos = (random.randint(5, 15), random.randint(1, 10))
        x = pos[0]
        for i in range(6):
            Entity(model='quad', scale_x=1, collider='box', texture='Assets/grass', x=x, y=pos[1])
            x+=0.9

makePlatform(10)

bg = Entity(model="quad", scale=(100, 100), texture="Assets/sky_cloud", z=1)

poslist = []
for i in range(5):
    pos = (random.randint(5, 15), random.randint(1, 10))

    x = pos[0]
    for i in range(6):
        
        x+=0.9

camera.orthographic = True
camera.position = (30/2,8)
camera.fov = 16
camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))

def update():
    if enemy1.onCollision():
        player.position = (0, 0)

app.run()

#COMMIT AND PUSH
#git commit -m "x commit"
#git push origin main
# git pull origin

# Z is vertical
# Y is horizontal
# X is 3D