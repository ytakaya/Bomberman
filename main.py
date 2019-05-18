from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

def main():
    window = pyglet.window.Window(800,600,caption='Pyglet')
    pyglet.app.run()

if __name__=='__main__':
    main()
