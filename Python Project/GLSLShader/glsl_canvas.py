from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class GLSLCanvas(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vertex_shader_source = """
        #version 330
        in vec2 position;
        void main() {
            gl_Position = vec4(position, 0.0, 1.0);
        }
        """

        self.fragment_shader_source = """
        #version 330
        uniform vec2 windowSize;
        out vec4 fragColor;
        void main() {
            vec2 normalizedCoords = gl_FragCoord.xy / windowSize;
            fragColor = vec4(normalizedCoords.x, normalizedCoords.y, 0.5, 1.0);
        }
        """

    def initializeGL(self):
        self.compile_shaders()

    def compile_shaders(self):
        self.shader = compileProgram(
            compileShader(self.vertex_shader_source, GL_VERTEX_SHADER),
            compileShader(self.fragment_shader_source, GL_FRAGMENT_SHADER)
        )
        self.windowSizeLocation = glGetUniformLocation(self.shader, "windowSize")

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.shader)

        width, height = self.width(), self.height()
        glUniform2f(self.windowSizeLocation, width, height)

        glBegin(GL_QUADS)
        glVertex2f(-1, -1)
        glVertex2f(1, -1)
        glVertex2f(1, 1)
        glVertex2f(-1, 1)
        glEnd()

        glUseProgram(0)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def set_vertex_shader(self, code):
        self.vertex_shader_source = code
        self.compile_shaders()
        self.update()

    def set_fragment_shader(self, code):
        self.fragment_shader_source = code
        self.compile_shaders()
        self.update()


