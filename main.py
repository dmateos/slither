import pywavefront

from render import window
from render import shader
from render import program
from render import vertex_data
from render import vertex_object

from render import objreader

def main():
    display = window.Window()
    display.setup()

    with open("shaders/basic_frag.shader", "r") as f:
        frag_shader_data = f.read()
    with open("shaders/basic_vert.shader", "r") as f:
        vert_shader_data = f.read()

    vert_shader = shader.Shader(vert_shader_data, "vertex")
    frag_shader = shader.Shader(frag_shader_data, "fragment")

    shader_program = program.Program(vert_shader, frag_shader)
    shader_program.use()

    vm = objreader.ObjReader("cube.obj")
    vm.read()

    vd = vertex_data.VertexData(shader_program, vm.verts, vm.vert_index)
    vd.setup()

    vo = vertex_object.VertexObject(vd)

    while display.keep_going():
        display.clear()

        vo.draw(shader_program)

        display.swap()
        display.poll()


if __name__ == "__main__":
    main()
    #vm = pywavefront.Wavefront("cube.obj")
    #print(vm.materials["Material"].vertex_format)

