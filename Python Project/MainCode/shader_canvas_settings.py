from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from MainCode.shader_output_view import ShaderOutputView

class ShaderCanvasSettings(QWidget):
    def __init__(self, shaderOutputView, parent=None):
        super().__init__(parent)
        self.shaderOutputView = shaderOutputView

        self.initUI()

        self.widthLineEdit.setText("1920")
        self.heightLineEdit.setText("1080")

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.widthLabel = QLabel("Width:")
        self.widthLineEdit = QLineEdit()

        self.heightLabel = QLabel("Height:")
        self.heightLineEdit = QLineEdit()

        self.layout.addWidget(self.widthLabel)
        self.layout.addWidget(self.widthLineEdit)

        self.layout.addWidget(self.heightLabel)
        self.layout.addWidget(self.heightLineEdit)

        self.setLayout(self.layout)

        # Connect signals and slots
        self.widthLineEdit.textChanged.connect(self.updateWidth)
        self.heightLineEdit.textChanged.connect(self.updateHeight)

    def updateWidth(self, text):
        value = int(text) if text.isdigit() else 0
        self.shaderOutputView.setSize(value, self.shaderOutputView.canvas.height())

    def updateHeight(self, text):
        value = int(text) if text.isdigit() else 0
        self.shaderOutputView.setSize(self.shaderOutputView.canvas.width(), value)