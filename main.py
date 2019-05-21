from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

def main():
    window = pyglet.window.Window(640,640,caption='Pyglet')
    quads = []
    for i in range(7):
        quad = pyglet.graphics.vertex_list(2,
            ('v2f', [0,i*80+80,800,i*80+80]),
            ('c3B', (255,255,255,255,255,255)))
        quads.append(quad)
        quad = pyglet.graphics.vertex_list(2,
            ('v2f', [i*80+80,0,i*80+80,800]),
            ('c3B', (255,255,255,255,255,255)))
        quads.append(quad)
    @window.event
    def on_draw():
        for quad in quads:
            quad.draw(pyglet.gl.GL_LINES)
    pyglet.app.run()

if __name__=='__main__':
    main()
