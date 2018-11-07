import numpy
from OpenGL.GL import *

class VertexData(object):
    def __init__(self, program, data, index_data, debug=False):
        self.vertex_array_id = 0
        self.vertex_buffer_id = 0
        self.vertex_index_id = 0
        self.program = program
        self.debug = debug

        self.buffer_data = numpy.array(data, dtype="float32")
        self.index_data = numpy.array(index_data, dtype="uint32")

        if self.debug:
            print(self.buffer_data)
            print(self.index_data)

        self.setup()

    def setup(self):
        self.vertex_array_id = glGenVertexArrays(1)
        self.bind()

        self.vertex_buffer_id = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertex_buffer_id)
        glBufferData(GL_ARRAY_BUFFER,
                     len(self.buffer_data) * 4,
                     self.buffer_data,
                     GL_STATIC_DRAW
        )

        glEnableVertexAttribArray(self.program.get_attribute("vp"))
        glVertexAttribPointer(self.program.get_attribute("vp"), 3, GL_FLOAT, GL_FALSE, 0, None)

        self.vertex_index_id = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vertex_index_id)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                     len(self.index_data) * 4,
                     self.index_data,
                     GL_STATIC_DRAW
        )

        self.unbind()
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def bind(self):
        glBindVertexArray(self.vertex_array_id)

    def unbind(self):
        glBindVertexArray(0)

    def draw(self):
        self.program.use()
        self.bind()
        glDrawElements(GL_TRIANGLES, len(self.index_data), GL_UNSIGNED_INT, None)

        err = glGetError()
        if err:
            print(err)

        self.unbind()
