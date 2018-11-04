from OpenGL.GL import *

class Shader(object):
    def __init__(self, shader_code, shader_type):
        self.setup(shader_code, shader_type)

    def setup(self, shader_code, shader_type):
        if shader_type == "vertex":
            self.shader = glCreateShader(GL_VERTEX_SHADER)
        else:
            self.shader = glCreateShader(GL_FRAGMENT_SHADER)

        glShaderSource(self.shader, shader_code)
        glCompileShader(self.shader)

        result = glGetShaderiv(self.shader, GL_COMPILE_STATUS)

        if not result:
            print("could not compile shader")

    def free(self):
        glDeleteShader(self.shader)

    @property
    def context(self):
        return self.shader
