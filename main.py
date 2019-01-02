import pyrr

from render import window
from render import shader
from render import program
from render import vertex_data
from render import vertex_object
from render import camera
from render import objreader
from render import texture

from sim import sim

camera_obj = camera.Camera()

def main():
    display = window.Window()
    display.setup()
    display.on_key_press(key_press)

    sim_obj = sim.Sim()
    sim_obj.print()
    sim_obj.run()
    sim_obj.print()

    with open("shaders/basic_frag.shader", "r") as f:
        frag_shader_data = f.read()
    with open("shaders/basic_vert.shader", "r") as f:
        vert_shader_data = f.read()

    vert_shader = shader.Shader(vert_shader_data, "vertex")
    frag_shader = shader.Shader(frag_shader_data, "fragment")
    shader_program = program.Program(vert_shader, frag_shader)

    vm = objreader.ObjReader("cube.obj", False)
    vd = vertex_data.VertexData(shader_program, vm.verts, vm.vert_index, vm.normals, False)

    vo = vertex_object.VertexObject(vd, 0.0,0.0,0.0)

    tex = texture.Texture("textures/dirt.png", 400, 400)
    tex.bind()

    vo_list = []
    for x in range(sim_obj.x):
        for y in range(sim_obj.y):
            vo = vertex_object.VertexObject(vd, 2.0*x,2.0*y,0.0)
            vo_list.append({"x": x, "y" : y, "vo" : vo})

    while True and display.keep_going():
        sim_obj.run()

        display.clear()

        for vo in vo_list:
            if sim_obj.get(vo["x"], vo["y"]) == 1:
                vo["vo"].draw(shader_program, camera_obj)

        #x, y = display.get_mouse_pos()
        #handle_mouse(x, y)

        display.swap()
        display.poll()

def key_press(key):
    if key == 87: #w
        camera_obj.forward(20.0)
    elif key == 83: #s
        camera_obj.back(20.0)
    elif key == 65: #a
        camera_obj.strafe_left(0.1)
        #camera_obj.pan_left(0.001)
    elif key == 68: #d
        camera_obj.strafe_right(0.1)
        #camera_obj.pan_right(0.001)

def handle_mouse(x, y):
    #camera_obj.pan_left(x)
    #camera_obj.pan_right(x)
    pass

if __name__ == "__main__":
    main()

