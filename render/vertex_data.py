import numpy
from OpenGL.GL import *

class VertexData(object):
    def __init__(self, program):
        self.vertex_array_id = 0
        self.vertex_buffer_id = 0
        self.program = program

        self.buffer_data = numpy.array(
            [
                -1.0, -1.0, 0.0,
                1.0, -1.0, 0.0,
                0.0, 1.0, 0.0,
             ],
            dtype="float32"
        )

    def setup(self):
        self.vertex_array_id = glGenVertexArrays(1)
        glBindVertexArray(self.vertex_array_id)

        self.vertex_buffer_id = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertex_buffer_id)
        glBufferData(GL_ARRAY_BUFFER,
                     len(self.buffer_data) * 4,
                     self.buffer_data,
                     GL_STATIC_DRAW
        )

        glEnableVertexAttribArray(self.program.get_attribute("vp"))
        glVertexAttribPointer(self.program.get_attribute("vp"), 3, GL_FLOAT, GL_FALSE, 0, None)

    def draw(self):
        self.program.use()
        glDrawArrays(GL_TRIANGLES, 0, 3)
        #glDrawElements(GL_TRIANGLES, 9, GL_FLOAT, 0)

        err = glGetError()
        if err:
            print(err)
