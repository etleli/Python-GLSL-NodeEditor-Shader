from PyQt5 import QtWidgets, QtOpenGL
from OpenGL.GL import shaders
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
import traceback

class OpenGLWidget(QtOpenGL.QGLWidget):
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
            out vec4 fragColor;
            void main() {
                fragColor = vec4(gl_FragCoord.x/640.0, gl_FragCoord.y/480.0, 0.5, 1.0);
            }
            """, GL_FRAGMENT_SHADER)

            self.shader = shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)
        except Exception:
            traceback.print_exc()

    def paintGL(self):
        try:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glUseProgram(self.shader)
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
        except Exception:
            traceback.print_exc()

try:
    app = QtWidgets.QApplication(sys.argv)
    window = OpenGLWidget()
    window.show()
    app.exec_()
except Exception:
    traceback.print_exc()
