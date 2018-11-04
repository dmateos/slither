import window
import shader
import program
import vertex_data

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

vertex_data = vertex_data.VertexData(shader_program)
vertex_data.setup()

while display.keep_going():
    display.clear()

    vertex_data.draw()

    display.swap()
    display.poll()


