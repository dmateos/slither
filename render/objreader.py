class ObjReader(object):
    def __init__(self, path):
        self.path = path
        self.verts = []
        self.normals = []
        self.vert_index = []

    def read(self):
        data = ""
        with open(self.path, "r") as f:
            data = f.read()

        for line in data.split("\n"):
            if line.startswith("vn"):
                for vert in line.split(" ")[1:]:
                    self.normals.append(float(vert))
            elif line.startswith("v"):
                for vert in line.split(" ")[1:]:
                    self.verts.append(float(vert))
            elif line.startswith("f"):
                for vert in line.split(" ")[1:3]:
                    for e in vert.split("//"):
                        self.vert_index.append(e[0])

        print(self.verts)
        print(self.vert_index)

