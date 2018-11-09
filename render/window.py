import glfw
from OpenGL.GL import *

class Window(object):
    def __init__(self, args=None):
        self._key_press_call = []

    def setup(self):
        if not glfw.init():
            return

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)

        self.window = glfw.create_window(1280, 1024, "Window", None, None)
        glfw.set_key_callback(self.window, self._key_event)
        #glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)
        glfw.set_input_mode(self.window,glfw.STICKY_KEYS,GL_TRUE)

        if not self.window:
            glfw.terminate()
            return

        glfw.make_context_current(self.window)

        glClearColor(0.0, 1.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LESS)

        print("{0}".format(glGetString(GL_VERSION).decode("ascii")))

    def swap(self):
        glfw.swap_buffers(self.window)

    def keep_going(self):
        return not glfw.window_should_close(self.window)

    def poll(self):
        glfw.poll_events()

    def clear(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def on_key_press(self, callback):
        self._key_press_call.append(callback)

    def _key_event(self, window, key, scancode, action, mods):
        for cb in self._key_press_call:
            cb(key)
