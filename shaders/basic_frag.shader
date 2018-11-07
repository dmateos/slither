#version 330 core

in vec3 vn_out;
out vec3 color;

void main()
{
  // Output color = red 
  color = vn_out;
}
