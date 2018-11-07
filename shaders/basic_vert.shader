#version 330 core

in vec3 vp;
uniform mat4 translation;
uniform mat4 view;
uniform mat4 perspective;

void main(){
  gl_Position = perspective * view * translation * vec4(vp, 1.0);
}
