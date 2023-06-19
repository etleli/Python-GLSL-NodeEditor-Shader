from PyQt5.QtWidgets import *


class GLSLCanvasWidget(QWidget):
    #Scene_class = Scene
    #GraphicsView_class = QDMGraphicsView

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.setMinimumHeight(200)