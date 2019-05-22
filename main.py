from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

TEXTURE_PATH = 'player.png'
PLAYER = pyglet.image.load(TEXTURE_PATH)

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

    def show_player(self, player_num):
        position = self.player[player_num]
        self._show_player(position)

    def _show_player(self, position):
        x, y = position


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.model = Model()

    def on_draw(self):
        for quad in self.model.quads:
            quad.draw(pyglet.gl.GL_LINES)
        sprite = pyglet.sprite.Sprite(img=PLAYER)
        sprite.scale = 50/sprite.width
        sprite.draw()

def main():
    window = Window(600,600,caption='Pyglet')
    quads = []
    pyglet.app.run()

if __name__=='__main__':
    main()
