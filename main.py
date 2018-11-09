import pyrr

from render import window
from render import shader
from render import program
from render import vertex_data
from render import vertex_object
from render import camera
from render import objreader

camera_obj = camera.Camera()

def main():
    display = window.Window()
    display.setup()
    display.on_key_press(key_press)

    with open("shaders/basic_frag.shader", "r") as f:
        frag_shader_data = f.read()
    with open("shaders/basic_vert.shader", "r") as f:
        vert_shader_data = f.read()

    vert_shader = shader.Shader(vert_shader_data, "vertex")
    frag_shader = shader.Shader(frag_shader_data, "fragment")

    shader_program = program.Program(vert_shader, frag_shader)

    vm = objreader.ObjReader("cube.obj", False)
    vm2 = objreader.ObjReader("monkey.obj", False)
    vm3 = objreader.ObjReader("torus.obj", False)

    vd = vertex_data.VertexData(shader_program, vm.verts, vm.vert_index, vm.normals, False)
    vd2 = vertex_data.VertexData(shader_program, vm2.verts, vm2.vert_index, vm2.normals, False)
    vd3 = vertex_data.VertexData(shader_program, vm3.verts, vm3.vert_index, vm3.normals, False)

    vo = vertex_object.VertexObject(vd, 0.0,0.0,0.0)
    vo2 = vertex_object.VertexObject(vd2, -5.0,0.0,0.0)
    vo3 = vertex_object.VertexObject(vd3, 5.0,-2.0,0.0)

    while display.keep_going():
        display.clear()

        vo.draw(shader_program, camera_obj)
        vo2.draw(shader_program, camera_obj)
        vo3.draw(shader_program, camera_obj)

        display.swap()
        display.poll()

def key_press(key):
    if key == 87: #w
        camera_obj.forward(20.0)
    elif key == 83: #s
        camera_obj.back(20.0)
    elif key == 65: #a
        camera_obj.pan_left(0.1)
    elif key == 68: #d
        camera_obj.pan_right(0.1)

if __name__ == "__main__":
    main()

