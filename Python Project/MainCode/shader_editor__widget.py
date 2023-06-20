import traceback

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os

from MainCode.nodes_drag_listbox import QDMDragListbox
from MainCode.shader_output_view import ShaderOutputView
from nodeeditor.node_editor_window import NodeEditorWindow
from nodeeditor.node_editor_widget import NodeEditorWidget
from GLSLShader.glsl_canvas_widget import GLSLCanvasWidget

class ShaderEditorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.name_company = 'AlpHive'
        self.name_product = 'GLSL Node Shader'

        self.font = "Arial"
        self.fontSize = 12

        self.initUI()

    def initUI(self):
        try:
            self.layout = QVBoxLayout(self)

            # Create a vSplitter
            self.vSplitter = QSplitter(Qt.Vertical)

            # Create a hSplitter
            self.hSplitter = QSplitter()

            # Prepare Widgets
            self.nodesListWidget = QDMDragListbox()

            self.shaderNodesQBox = QGroupBox("Shader Nodes")
            self.shaderNodesQBox.setFont(QFont(self.font, self.fontSize))
            self.shaderNodesQBox.setLayout(QVBoxLayout())
            self.shaderNodesQBox.layout().addWidget(self.nodesListWidget)

            self.nodesEditorWidget = NodeEditorWidget()

            self.shaderEditorQBox = QGroupBox("Shader Editor")
            self.shaderEditorQBox.setFont(QFont(self.font, self.fontSize))
            self.shaderEditorQBox.setLayout(QVBoxLayout())
            self.shaderEditorQBox.layout().addWidget(self.nodesEditorWidget)

            self.glslCanvasWidget = GLSLCanvasWidget()

            self.glslCanvasWidget.setMaximumSize(100, 200)

            self.glslCanvasViewWidget = ShaderOutputView()

            self.shaderOutputQBox = QGroupBox("Shader Output")
            self.shaderOutputQBox.setFont(QFont(self.font, self.fontSize))
            shaderOutputLayout = QVBoxLayout()

            # shaderOutputLayout.addWidget(self.glslCanvasWidget)
            shaderOutputLayout.addWidget(self.glslCanvasViewWidget)

            self.shaderOutputQBox.setLayout(shaderOutputLayout)
            #self.shaderOutputQBox.layout().setAlignment(Qt.AlignCenter)

            print(self.shaderOutputQBox.height())

            # Add Widgets to Splitter
            self.vSplitter.addWidget(self.shaderOutputQBox)
            self.hSplitter.addWidget(self.shaderEditorQBox)
            self.hSplitter.addWidget(self.shaderNodesQBox)

            # Add hSplitter to vSplitter
            self.vSplitter.addWidget(self.hSplitter)

            # Set Size
            self.vSplitter.setSizes([100, 200])

            # Add the splitters to the layout
            self.layout.addWidget(self.vSplitter)

            self.setLayout(self.layout)
        except Exception as e:
            traceback.print_exc()
            print(e)