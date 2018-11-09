import pyrr
import numpy

class Camera(object):
    def __init__(self):
        self.position = pyrr.Vector3([0.0,0.0,-100.0])
        self.rotation = pyrr.Vector3([0.0, 0.0, 0.0])

    def transforms(self):
        rotation = pyrr.Quaternion.from_eulers(self.rotation)
        translation = pyrr.Matrix44.from_translation(self.position)
        return translation * rotation

    def perspective(self):
        perspective = pyrr.Matrix44.perspective_projection(60.0, 1280/1024, 0.01, 1000.0)
        return perspective

    def forward(self, n):
        self.position.z += 1.0

    def back(self, n):
        self.position.z -= 1.0

    def pan_left(self, n):
        self.rotation.y += 0.1

    def pan_right(self, n):
        self.rotation.y -= 0.1

    def strafe_left(self, n):
        self.position.x += 1.0

    def strafe_right(self, n):
        self.position.x -= 1.0
