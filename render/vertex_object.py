import numpy
import pyrr
from OpenGL.GL import *

class VertexObject(object):
    def __init__(self, vertex_data):
        self.vertex_data = vertex_data
        self.pos = pyrr.Vector3([0.1, 0.0, 0.0])

    def translation_matrix(self):
        matrix = pyrr.Matrix44.from_translation(self.pos)
        return matrix

    def draw(self, program):
        program.use()
        program.set_uniform("translation", self.translation_matrix())
        self.vertex_data.draw()
