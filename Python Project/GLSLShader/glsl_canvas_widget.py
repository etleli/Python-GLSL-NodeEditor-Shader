from PyQt5 import QtWidgets, QtOpenGL, QtCore
from OpenGL.GL import shaders
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette


class GLSLCanvasWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        super(GLSLCanvasWidget, self).__init__(parent)
        # self.width = 180
        # self.height = 240

        # self.width = 180
        # self.height = 240
    # def __init__(self, parent=None):
    #     super(GLSLCanvasWidget, self).__init__(parent)
    #     self.aspect_ratio = 1.0
    #
    #
    #
    # def setCanvasSize(self, width, height):
    #     self.aspect_ratio = width / height
    #     self.updateGeometry()
    #
    # def sizeHint(self):
    #     # Override sizeHint to return a size that maintains the aspect ratio
    #     width = super(GLSLCanvasWidget, self).sizeHint().width()
    #     height = int(width / self.aspect_ratio)
    #     return QtCore.QSize(width, height)
    #
    # def resizeEvent(self, event):
    #     size = event.size()
    #     if size.height() != 0:
    #         if size.width() / size.height() > self.aspect_ratio:
    #             size.setWidth(int(size.height() * self.aspect_ratio))
    #         else:
    #             size.setHeight(int(size.width() / self.aspect_ratio))
    #     self.resize(size)
    #     super().resizeEvent(event)

    def initializeGL(self):
        try:
            VERTEX_SHADER = shaders.compileShader("""
            #version 330
            in vec2 position;
            void main() {
                gl_Position = vec4(position, 0.0, 1.0);
            }
            """, GL_VERTEX_SHADER)

            FRAGMENT_SHADER = shaders.compileShader("""
            #version 330
            uniform vec2 windowSize;
            out vec4 fragColor;
            void main() {
                vec2 normalizedCoords = gl_FragCoord.xy / windowSize;
                fragColor = vec4(normalizedCoords.x, normalizedCoords.y, 0.5, 1.0);
            }

            """, GL_FRAGMENT_SHADER)

            self.shader = shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)

            # Get the location of the windowSize uniform variable
            self.windowSizeLocation = glGetUniformLocation(self.shader, "windowSize")
        except Exception:
            traceback.print_exc()

    def paintGL(self):
        try:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glUseProgram(self.shader)

            # Set the windowSize uniform variable
            width, height = self.width(), self.height()  # get the current width and height
            glUniform2f(self.windowSizeLocation, width, height)

            glBegin(GL_QUADS)
            glVertex2f(-1, -1)
            glVertex2f(1, -1)
            glVertex2f(1, 1)
            glVertex2f(-1, 1)
            glEnd()
            glUseProgram(0)
        except Exception:
            traceback.print_exc()

    def resizeGL(self, w, h):
        try:
            glViewport(0, 0, w, h)
            self.update()
        except Exception:
            traceback.print_exc()

