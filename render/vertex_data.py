import numpy
from OpenGL.GL import *

class VertexData(object):
    def __init__(self, program, data, index_data, normal_data, debug=False):
        self.vertex_array_id = 0
        self.vertex_buffer_id = 0
        self.normal_buffer_id = 0
        self.vertex_index_id = 0
        self.program = program
        self.debug = debug

        self.buffer_data = numpy.array(data, dtype="float32")
        self.index_data = numpy.array(index_data, dtype="uint32")
        self.normal_data = numpy.array(normal_data, dtype="float32")

        self.index_len = len(self.index_data)

        if self.debug:
            print("VertexData")
            print(self.buffer_data)
            print(self.index_data)

        self.setup()

    def setup(self):
        self.vertex_array_id = glGenVertexArrays(1)
        self.program.use()
        self.bind()

        self.vertex_buffer_id = self._opengl_buffer(GL_ARRAY_BUFFER, self.buffer_data, "vp")
        self.normal_buffer_id = self._opengl_buffer(GL_ARRAY_BUFFER, self.normal_data, "vn")
        self.vertex_index_id = self._opengl_buffer(GL_ELEMENT_ARRAY_BUFFER, self.index_data)

        self.unbind()

    def bind(self):
        glBindVertexArray(self.vertex_array_id)

    def unbind(self):
        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def draw(self):
        #self.program.use()
        self.bind()
        glDrawElements(GL_TRIANGLES, self.index_len, GL_UNSIGNED_INT, None)

        if self.debug:
            err = glGetError()
            if err:
                print(err)

        self.unbind()

    def _opengl_buffer(self, buffer_type, data, attribute=None):
        buffer_id = glGenBuffers(1)
        glBindBuffer(buffer_type, buffer_id)
        glBufferData(buffer_type,
                     len(data) * 4,
                     data,
                     GL_STATIC_DRAW,
        )

        if buffer_type == GL_ARRAY_BUFFER:
            glEnableVertexAttribArray(self.program.get_attribute(attribute))
            glVertexAttribPointer(self.program.get_attribute(attribute),
                                  3, GL_FLOAT, GL_FLOAT, 0, None
            )

        return buffer_id

