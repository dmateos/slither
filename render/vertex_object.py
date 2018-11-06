import numpy
import pyrr
from OpenGL.GL import *

class VertexObject(object):
    def __init__(self, vertex_data):
        self.vertex_data = vertex_data

        self.pos = pyrr.Vector3([0.10,0.0,0.0])
        self.translation = pyrr.Vector3([0.0,0.0,0.0])
        self.scale = pyrr.Vector3([0.5,0.5,0.5])

    def transforms(self):
        matrix = pyrr.Matrix44.from_scale(self.scale)
        translation = pyrr.Matrix44.from_translation(self.translation)
        matrix = matrix * translation
        return matrix

    def draw(self, program):
        program.use()
        program.set_uniform("translation", self.transforms())
        self.vertex_data.draw()
