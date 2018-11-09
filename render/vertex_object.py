import pyrr
from OpenGL.GL import *

class VertexObject(object):
    def __init__(self, vertex_data, x, y, z):
        self.vertex_data = vertex_data

        self.translation = pyrr.Vector3([x,y,z])
        self.scale = pyrr.Vector3([10.0,10.0,10.0])

    def transforms(self):
        matrix = pyrr.Matrix44.from_scale(self.scale)
        translation = pyrr.Matrix44.from_translation(self.translation)
        matrix = matrix * translation
        return matrix

    def draw(self, program, camera):
        program.use()
        program.set_uniform("translation", self.transforms())
        program.set_uniform("view", camera.transforms())
        program.set_uniform("perspective", camera.perspective())
        self.vertex_data.draw()
