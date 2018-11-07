class ObjReader(object):
    def __init__(self, path, debug=False):
        self.path = path
        self.verts = []
        self.normals = []
        self.vert_index = []
        self.norm_index = []
        self.debug = debug
        self.read()

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
                for vert in line.split(" ")[1:]:
                    self.vert_index.append(int(vert.split("//")[0])-1)
                    self.norm_index.append(int(vert.split("//")[1])-1)

        if self.debug:
            print("ObjReader")
            print(self.verts)
            print(self.vert_index)
            print(self.norm_index)

