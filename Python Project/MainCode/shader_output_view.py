from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from MainCode.shader_graphics_scene import QSDGraphicsScene
from MainCode.shader_graphics_view import QSMGraphicsView
from GLSLShader.glsl_canvas_widget import GLSLCanvasWidget


class ShaderOutputView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.grScene = QSDGraphicsScene()

        self.view = QSMGraphicsView(self.grScene, self)
        self.view.setScene(self.grScene)
        self.layout.addWidget(self.view)

        self.addDebugContent()

    def addDebugContent(self):
        canvasWidget = GLSLCanvasWidget()
        proxyWidget = self.grScene.addWidget(canvasWidget)
        proxyWidget.resize(1080, 1090)
        proxyWidget.setPos(0, 30)

        widget1 = QPushButton("Hello World")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.ItemIsMovable)
        proxy1.setPos(0, 40)




