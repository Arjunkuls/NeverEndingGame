from ursina import *
import random
app = Ursina()

from ursina.prefabs.platformer_controller_2d import PlatformerController2d
player = PlatformerController2d(y=1, z=.01, scale_y=1, max_jumps=1)
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

enemy1 = Enemy(2, 2)
ground = Entity(model='quad', scale_x=10, collider='box', color=color.black, y=0, x = 0)

blockList = []
for i in range(5):
    pos = (0, random.randint(1, 10))
    Entity(model='quad', scale_x=10, collider='box', color=color.black, x=pos[0], y=pos[1])


camera.orthographic = True
camera.position = (30/2,8)
camera.fov = 16
camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))

def update():
    if enemy1.onCollision():
        player.position = (3, 10)
app.run()

#COMMIT AND PUSH
#git commit -m "x commit"
#git push origin main
# git pull origin

# Z is vertical
# Y is horizontal
# X is 3D