import traceback

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os

from MainCode.nodes_drag_listbox import QDMDragListbox
from MainCode.shader_output_view import ShaderOutputView
from nodeeditor.node_editor_window import NodeEditorWindow
from nodeeditor.node_editor_widget import NodeEditorWidget
from GLSLShader.glsl_canvas_widget import GLSLCanvasItem
from shader_canvas_settings import ShaderCanvasSettings


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
            self.hSplitter1 = QSplitter()
            self.hSplitter2 = QSplitter()

            # Prepare Widgets

            # Shader Nodes Library
            self.nodesListWidget = QDMDragListbox()

            self.shaderNodesQBox = QGroupBox("Shader Nodes")
            self.shaderNodesQBox.setFont(QFont(self.font, self.fontSize))
            self.shaderNodesQBox.setLayout(QVBoxLayout())
            self.shaderNodesQBox.layout().addWidget(self.nodesListWidget)

            # Shader Editor
            self.nodesEditorWidget = NodeEditorWidget()

            self.shaderEditorQBox = QGroupBox("Shader Editor")
            self.shaderEditorQBox.setFont(QFont(self.font, self.fontSize))
            self.shaderEditorQBox.setLayout(QVBoxLayout())
            self.shaderEditorQBox.layout().addWidget(self.nodesEditorWidget)

            # Coding Textbox
            self.codingTextbox = QTextEdit()

            self.codingTextboxQBox = QGroupBox("Code Editor")
            self.codingTextboxQBox.setFont(QFont(self.font, self.fontSize))
            self.codingTextboxQBox.setLayout(QVBoxLayout())
            self.codingTextboxQBox.layout().addWidget(self.codingTextbox)

            # Shader Output
            self.glslCanvasViewWidget = ShaderOutputView()

            self.shaderOutputQBox = QGroupBox("Shader Output")
            self.shaderOutputQBox.setFont(QFont(self.font, self.fontSize))
            self.shaderOutputQBox.setLayout(QVBoxLayout())
            self.shaderOutputQBox.layout().addWidget(self.glslCanvasViewWidget)

            # Shader Canvas Settings
            self.glslCanvasSettings = ShaderCanvasSettings(self.glslCanvasViewWidget)

            self.shaderSettingsQBox = QGroupBox("Canvas Settings")
            self.shaderSettingsQBox.setFont(QFont(self.font, self.fontSize))
            self.shaderSettingsQBox.setLayout(QVBoxLayout())
            self.shaderSettingsQBox.layout().addWidget(self.glslCanvasSettings)

            # Shader Output Splitter
            self.hSplitter2.addWidget(self.shaderOutputQBox)
            self.hSplitter2.addWidget(self.shaderSettingsQBox)

            # Shader Editor Splitter
            self.hSplitter1.addWidget(self.shaderEditorQBox)
            self.hSplitter1.addWidget(self.shaderNodesQBox)

            # Tab Widget
            self.tabWidget = QTabWidget()
            self.tabWidget.addTab(self.hSplitter1, "Node Editor")
            self.tabWidget.addTab(self.codingTextboxQBox, "Coding Textbox")

            # Add hSplitter to vSplitter
            self.vSplitter.addWidget(self.hSplitter2)
            self.vSplitter.addWidget(self.tabWidget)

            # Set Size
            self.vSplitter.setSizes([100, 200])

            # Add the splitters to the layout
            self.layout.addWidget(self.vSplitter)

            self.setLayout(self.layout)
        except Exception as e:
            traceback.print_exc()
            print(e)