from OpenGL.GL import *

class Program(object):
    def __init__(self, *shaders, validate=False):
        self.setup(*shaders)
        if validate == False or self.validate():
            for shader in shaders:
                shader.free()

    def setup(self, *shaders):
        self.program = glCreateProgram()
        for shader in shaders:
            glAttachShader(self.program, shader.context)

        glLinkProgram(self.program)

    def validate(self):
        glValidateProgram(self.program)
        validation = glGetProgramiv(self.program, GL_VALIDATE_STATUS)
        if validation == GL_FALSE:
            why = glGetProgramInfoLog(self.program)
            print("could not compile program: {0}".format(why))
            return False
        return True

    def use(self):
        glUseProgram(self.program)

    def unuse(self):
        glUseProgram(0)

    def get_attribute(self, name):
        attr = glGetAttribLocation(self.program, name)
        return attr

    @property
    def context(self):
        return self.program
