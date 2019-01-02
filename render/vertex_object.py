import pyrr
from OpenGL.GL import *

class VertexObject(object):
    def __init__(self, vertex_data, x, y, z):
        self.vertex_data = vertex_data

        self.position = pyrr.Vector3([x,y,z])
        self.scale = pyrr.Vector3([1.0,1.0,1.0])

        self.scalemat = pyrr.Matrix44.from_scale(self.scale)
        self.posmat = pyrr.Matrix44.from_translation(self.position)
        self.transformmat = self.scalemat * self.posmat

    def transforms(self):
        return self.transformmat

    def draw(self, program, camera):
        program.use()
        program.set_uniform("translation", self.transforms())
        program.set_uniform("view", camera.transforms())
        program.set_uniform("perspective", camera.perspective())
        self.vertex_data.draw()
