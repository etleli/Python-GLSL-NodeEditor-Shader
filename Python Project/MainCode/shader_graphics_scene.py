import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QSDGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setItemIndexMethod(QGraphicsScene.NoIndex)

        self._color_background = QColor("#57504b")
        self._color_light = QColor("#706862")
        self.gridSize = 100

        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self.scene_width, self.scene_height = 2000, 2000

        self.setSceneRect(-self.scene_width//2, -self.scene_height//2, self.scene_width, self.scene_height)

        self.setBackgroundBrush(self._color_background)

    def dragMoveEvent(self, event):
        """Overriden Qt's dragMoveEvent to enable Qt's Drag Events"""
        pass

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.gridSize)
        first_top = top - (top % self.gridSize)

        lines = []
        for x in range(first_left, right, self.gridSize):
            lines.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.gridSize):
            lines.append(QLine(left, y, right, y))

        painter.setPen(self._pen_light)
        painter.drawLines(*lines)