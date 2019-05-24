from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse
from collections import deque

TICKS_PER_SEC = 60
TEXTURE_PATH = ['player.png','bomb.png','explosion.png']
PLAYER = pyglet.image.load(TEXTURE_PATH[0])
BOMB = pyglet.image.load(TEXTURE_PATH[1])
EXPLOSION = pyglet.image.load(TEXTURE_PATH[2])

class Model(object):

    def __init__(self):
        self.world = {}
        self.player = {}
        self.quads = []

        self._initialize()

    def _initialize(self):
        """
        Initialize the field.
        """
        for i in range(12):
            quad = pyglet.graphics.vertex_list(2,
                ('v2f', [0,i*50+50,600,i*50+50]),
                ('c3B', (255,255,255,255,255,255)))
            self.quads.append(quad)
            quad = pyglet.graphics.vertex_list(2,
                ('v2f', [i*50+50,0,i*50+50,600]),
                ('c3B', (255,255,255,255,255,255)))
            self.quads.append(quad)


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.model = Model()
        self.batch = pyglet.graphics.Batch()
        self.player = []
        self.player.append(pyglet.sprite.Sprite(img=PLAYER,batch=self.batch))
        self.player[0].scale = 50/self.player[0].width
        self.player.append(pyglet.sprite.Sprite(img=PLAYER,x=self.width-50,y=self.height-50,batch=self.batch))
        self.player[1].scale = 50/self.player[1].width
        self.bomb = deque([])
        self.explosion = deque([])

        pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)

    def hit(self,exs,player):
        """If bomb hit the player?

        Parameters
        ----------
        exs : pyglet.sprite.Sprite
            Sprite object of explosion
        player : pyglet.sprite.Sprite
            Sprite object of player

        Returns
        -------
        If hit : bool
        """
        pl_x,pl_y = player.x,player.y
        for ex in exs:
            ex_x,ex_y = ex.x,ex.y
            if ex_x==pl_x and ex_y==pl_y:
                return True
        return False

    def on_key_press(self, symbol, modifiers):
        # player0
        if symbol==key.D and self.player[0].x<self.width-50:
            self.player[0].x += 50
        if symbol==key.W and self.player[0].y<self.height-50:
            self.player[0].y += 50
        if symbol==key.A and self.player[0].x>0:
            self.player[0].x -= 50
        if symbol==key.S and self.player[0].y>0:
            self.player[0].y -= 50
        if symbol==key.V:
            x = self.player[0].x
            y = self.player[0].y
            b = pyglet.sprite.Sprite(img=BOMB,x=x,y=y,batch=self.batch)
            b.scale = 50/b.width
            self.bomb.append([b,0])

        # player1
        if symbol==key.RIGHT and self.player[1].x<self.width-50:
            self.player[1].x += 50
        if symbol==key.UP and self.player[1].y<self.height-50:
            self.player[1].y += 50
        if symbol==key.LEFT and self.player[1].x>0:
            self.player[1].x -= 50
        if symbol==key.DOWN and self.player[1].y>0:
            self.player[1].y -= 50
        if symbol==key.M:
            x = self.player[1].x
            y = self.player[1].y
            b = pyglet.sprite.Sprite(img=BOMB,x=x,y=y,batch=self.batch)
            b.scale = 50/b.width
            self.bomb.append([b,0])


    def on_draw(self):
        self.clear()
        for quad in self.model.quads:
            quad.draw(pyglet.gl.GL_LINES)
        self.batch.draw()

    def update(self,dt):
        if self.bomb:
            new_bomb = deque()
            while self.bomb:
                b = self.bomb.popleft()
                # Bomb explode on 1s after put
                if b[1]>1:
                    explosions = []
                    # Explosion occur at all sides of bomb
                    dxy = [(-50,0),(0,0),(50,0),(0,-50),(0,50)]
                    for dx,dy in dxy:
                        explosions.append(pyglet.sprite.Sprite(
                            img=EXPLOSION,x=b[0].x+dx,y=b[0].y+dy,batch=self.batch))
                        explosions[-1].scale = 50/explosions[-1].width
                    self.explosion.append([explosions,0])
                else:
                    b[1] += dt
                    new_bomb.append(b)
            self.bomb = new_bomb

        if self.explosion:
            new_ex = deque()
            while self.explosion:
                ex, t = self.explosion.popleft()
                for i,pl in enumerate(self.player):
                    if self.hit(ex,pl):
                        print('Player{} BOMB!!'.format(i+1))
                        print('Winner : Player{}'.format((i+1)%2+1))
                        print('Looser : Player{}'.format((i+1)))
                        self.on_window_close()
                if t<0.2:
                    t += dt
                    new_ex.append([ex,t])
            self.explosion = new_ex

    def on_window_close(self):
        pyglet.app.exit()

def main():
    window = Window(600,600,caption='Pyglet')
    quads = []
    #pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()

if __name__=='__main__':
    main()
