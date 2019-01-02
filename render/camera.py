import pyrr

class Camera(object):
    def __init__(self):
        self.position = pyrr.Vector3([0.0,0.0,-100.0])
        self.rotation = pyrr.Vector3([0.0, 0.0, 0.0])
        self.direction = pyrr.Vector3([0.0, 0.0, 0.0])

        self.dirty = False
        self.permat = pyrr.Matrix44.perspective_projection(45.0, 1280/1024, 0.01, 1000.0)
        self.posmat = pyrr.Matrix44.from_translation(self.position)
        self.dirmat = pyrr.Matrix44.from_translation(self.direction)
        self.combined_mat = pyrr.Matrix44.identity() * self.dirmat * self.posmat

    def transforms(self):
        if self.dirty:
            self.posmat = pyrr.Matrix44.from_translation(self.position)
            self.dirmat = pyrr.Matrix44.from_translation(self.direction)
            self.combined_mat = pyrr.Matrix44.identity() * self.dirmat * self.posmat
            self.dirty = False
        return self.combined_mat

    def perspective(self):
        return self.permat

    def forward(self, n):
        self.direction.z += 1.0
        self.dirty = True

    def back(self, n):
        self.direction.z -= 1.0
        self.dirty = True

    def pan_left(self, n):
        self.rotation.y -= 0.001
        self.dirty = True

    def pan_right(self, n):
        self.rotation.y += 0.001
        self.dirty = True

    def strafe_left(self, n):
        self.position.x += 1.0
        self.dirty = True

    def strafe_right(self, n):
        self.position.x -= 1.0
        self.dirty = True
