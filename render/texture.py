from OpenGL.GL import *
import imageio

class Texture(object):
    def __init__(self, texture_data, width, height):
        self.texture_data = imageio.imread(texture_data)
        self.width = width
        self.height = height
        self.texture_id = 0

        print(self.texture_data)
        self._opengl_setup_texture()

    def bind(self):
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

    def unbind(self):
        glBindTexture(GL_TEXTURE_2D, 0)

    def get_gl_coord(self):
        pass

    def _opengl_setup_texture(self):
        self.texture_id = glGenTextures(1)
        self.bind()

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                     self.width, self.height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, self.texture_data
        )

        self.unbind()
