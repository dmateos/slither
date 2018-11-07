#version 330 core

in vec3 vp;
uniform mat4 translation;
uniform mat4 view;

void main(){
  gl_Position = view * translation * vec4(vp, 1.0);
}
