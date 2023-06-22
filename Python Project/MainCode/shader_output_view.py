from PyQt5.QtWidgets import *

from GLSLShader.glsl_canvas import GLSLCanvas
from MainCode.graphics.shader_graphics_view import QSMGraphicsView
from MainCode.graphics.shader_graphics_scene import QSDGraphicsScene


class ShaderOutputView(QWidget):
    def __init__(self, shaderEditorWindow, parent=None):
        super().__init__(parent)

        self.shaderEditorWindow = shaderEditorWindow

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.canvas = GLSLCanvas(self.shaderEditorWindow)

        self.scene = QSDGraphicsScene()
        self.scene.addWidget(self.canvas)

        self.view = QSMGraphicsView(self.scene)

        self.layout.addWidget(self.view)

    def setSize(self, width, height):
        self.canvas.setFixedSize(width, height)

    def updateFragmentShader(self, code):
        self.canvas.set_fragment_shader(code)





