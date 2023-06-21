from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from GLSLShader.glsl_canvas import GLSLCanvas


# class GLSLCanvasWidget(QWidget):
#
#     def __init__(self, width, height, parent: QWidget = None):
#         super().__init__(parent)
#
#         self.width = width
#         self.height = height
#
#         self.layout = QVBoxLayout(self)
#
#         self.initContent()
#
#         self.setLayout(self.layout)
#
#     def initContent(self):
#         self.canvasWidget = GLSLCanvas()
#         self.layout.addWidget(self.canvasWidget)
#
#     def boundingRect(self) -> QRectF:
#         return QRectF(
#             0,
#             0,
#             self.width,
#             self.height
#         ).normalized()
#
#     def paint(self, painter, option, widget):
#         painter.setBrush(QBrush(QColor("#E3212121")))
#         painter.drawRect(self.boundingRect())
#
#     def setSize(self, width, height):
#         self.width = width
#         self.height = height
#         self.canvasWidget.resize(self.width, self.height)

# class GLSLCanvasWidget(QGraphicsWidget):
#
#     def __init__(self, width, height, parent: QWidget = None):
#         super().__init__(parent)
#
#         self.width = width
#         self.height = height
#
#         self.initContent()
#
#     def initContent(self):
#         self.canvasWidget = GLSLCanvas()
#
#         # Create a layout and add the GLSLCanvas to it
#         layout = QVBoxLayout()
#         layout.addWidget(self.canvasWidget)
#
#         # Set the layout on the GLSLCanvasWidget
#         self.setLayout(layout)
#
#     def boundingRect(self) -> QRectF:
#         return QRectF(
#             0,
#             0,
#             self.width,
#             self.height
#         ).normalized()
#
#     def paint(self, painter, option, widget):
#         painter.setBrush(QBrush(QColor("#E3212121")))
#         painter.drawRect(self.boundingRect())
#
#     def setSize(self, width, height):
#         self.width = width
#         self.height = height
#         self.canvasWidget.resize(self.width, self.height)

class GLSLCanvasItem(QGraphicsItem):
    def __init__(self, width, height, canvas, parent=None):
        super().__init__(parent)
        self.canvas = canvas
        self.width = width
        self.height = height

    def boundingRect(self) -> QRectF:
        return QRectF(
            0,
            0,
            self.width,
            self.height
        ).normalized()

    def paint(self, painter, option, widget):
        if self.canvas is not None and self.canvas.image is not None:
            painter.drawImage(0, 0, self.canvas.image)

    def setSize(self, width, height):
        self.width = width
        self.height = height
