import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QOpenGLWidget, QApplication
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class GLSLCanvas(QOpenGLWidget):
    def __init__(self, shaderEditorWindow, parent=None):
        super().__init__(parent)

        self.shaderEditorWindow = shaderEditorWindow
        self.start_time = time.time()

        self.vertex_shader_source = """
        #version 330
        in vec2 position;
        void main() {
            gl_Position = vec4(position, 0.0, 1.0);
        }
        """

        self.DEFAULT_FRAGMENT_SHADER = """
        #version 330
        uniform vec2 windowSize;
        out vec4 fragColor;
        void main() {
            vec2 normalizedCoords = gl_FragCoord.xy / windowSize;
            fragColor = vec4(normalizedCoords.x, normalizedCoords.y, 0.5, 1.0);
        }
        """

        self.fragment_shader = """
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
        self.start_time = time.time()
        self.timer = QTimer()
        self.timer.timeout.connect(self.shaderEditorWindow.updateCanvas)
        self.timer.start(16)  # 60 FPS (1000 ms / 60 = 16.67 ms)

    def compile_shaders(self):
        try:
            # Assuming 'code' is the shader code retrieved from the text box
            self.shader = compileProgram(
                compileShader(self.vertex_shader_source, GL_VERTEX_SHADER),
                compileShader(self.fragment_shader, GL_FRAGMENT_SHADER)
            )
            self.outputError("")
        except Exception as e:
            # Display the error message to the user
            self.outputError(str(e))
            # Fall back to a default or previously working shader
            self.shader = compileProgram(
                compileShader(self.vertex_shader_source, GL_VERTEX_SHADER),
                compileShader(self.DEFAULT_FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
            )

        self.windowSizeLocation = glGetUniformLocation(self.shader, "windowSize")

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.shader)

        width, height = self.width(), self.height()
        glUniform2f(self.windowSizeLocation, width, height)

        # Get the current time
        current_time = time.time() - self.start_time

        # Set the time uniform in the shader
        time_location = glGetUniformLocation(self.shader, "time")
        glUniform1f(time_location, current_time)

        glBegin(GL_QUADS)
        glVertex2f(-1, -1)
        glVertex2f(1, -1)
        glVertex2f(1, 1)
        glVertex2f(-1, 1)
        glEnd()

        glUseProgram(0)
        glFlush()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def set_vertex_shader(self, code):
        self.vertex_shader_source = code
        self.compile_shaders()
        self.update()

    def set_fragment_shader(self, code):
        # finalcode = "#version 330\nuniform vec2 windowSize;\nout vec4 fragColor;\nvoid main() {\n" + code + "}"
        self.fragment_shader = code
        self.compile_shaders()
        self.update()

    def outputError(self, error):
        self.shaderEditorWindow.codingTools.outputText(error)

