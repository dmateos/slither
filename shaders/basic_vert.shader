#version 330 core

in vec3 vp;
uniform mat4 translation;

void main(){
  gl_Position = translation * vec4(vp, 1.0);
}
