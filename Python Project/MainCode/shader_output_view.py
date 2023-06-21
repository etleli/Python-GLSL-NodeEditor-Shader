from PyQt5.QtWidgets import *

from GLSLShader.glsl_canvas import GLSLCanvas
from MainCode.graphics.shader_graphics_view import QSMGraphicsView
from MainCode.graphics.shader_graphics_scene import QSDGraphicsScene


class ShaderOutputView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.canvas = GLSLCanvas()
        self.canvas.setFixedSize(1920, 1080)

        self.scene = QSDGraphicsScene()
        self.scene.addWidget(self.canvas)

        self.view = QSMGraphicsView(self.scene)

        self.layout.addWidget(self.view)






