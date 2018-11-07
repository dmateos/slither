import numpy
import pyrr

class Camera(object):
    def __init__(self):
        self.translation = pyrr.Vector3([0.0,0.0,0.0])
        self.orientation = "something"

    def transforms(self):
        perspective = pyrr.Matrix44.perspective_projection(60.0, 1280/1024, 0.01, 1000.0)

        lookat = pyrr.Matrix44.look_at(
            (self.translation.x, self.translation.y, self.translation.z),
            (0.0, 0.0, 0.0),
            (0.0, 1.0, 0.0),
        )
        return perspective * lookat
