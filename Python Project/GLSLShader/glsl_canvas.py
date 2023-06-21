from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class GLSLCanvas(QOpenGLWidget):
    def initializeGL(self):
        VERTEX_SHADER = """
        #version 330
        in vec2 position;
        void main() {
            gl_Position = vec4(position, 0.0, 1.0);
        }
        """

        FRAGMENT_SHADER = """
        #version 330
        uniform vec2 windowSize;
        out vec4 fragColor;
        void main() {
            vec2 normalizedCoords = gl_FragCoord.xy / windowSize;
            fragColor = vec4(normalizedCoords.x, normalizedCoords.y, 0.5, 1.0);
        }
        """

        self.shader = compileProgram(
            compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
            compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
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

