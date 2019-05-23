from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

TEXTURE_PATH = ['player.png','bomb.png']
PLAYER = pyglet.image.load(TEXTURE_PATH[0])
BOMB = pyglet .image.load(TEXTURE_PATH[1])

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
        self.bomb = []

    def on_key_press(self, symbol, modifiers):
        if symbol==key.RIGHT and self.player[0].x<self.width-50:
            self.player[0].x += 50
        if symbol==key.UP and self.player[0].y<self.height-50:
            self.player[0].y += 50
        if symbol==key.LEFT and self.player[0].x>0:
            self.player[0].x -= 50
        if symbol==key.DOWN and self.player[0].y>0:
            self.player[0].y -= 50
        if symbol==key.W:
            x = self.player[0].x
            y = self.player[0].y
            b = pyglet.sprite.Sprite(img=BOMB,x=x,y=y,batch=self.batch)
            b.scale = 50/b.width
            self.bomb.append(b)


    def on_draw(self):
        self.clear()
        for quad in self.model.quads:
            quad.draw(pyglet.gl.GL_LINES)
        self.batch.draw()

def main():
    window = Window(600,600,caption='Pyglet')
    quads = []
    #pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()

if __name__=='__main__':
    main()
