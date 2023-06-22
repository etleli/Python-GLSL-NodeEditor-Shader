import traceback

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainCode.nodes_drag_listbox import QDMDragListbox
from MainCode.shader_code_editor import ShaderCodeEditor
from MainCode.shader_code_editor_tools import CodeEditorTools
from MainCode.shader_output_view import ShaderOutputView
from nodeeditor.node_editor_widget import NodeEditorWidget
from MainCode.shader_canvas_settings import ShaderCanvasSettings


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
            self.hSplitter3 = QSplitter()

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
            self.codingTextbox = ShaderCodeEditor()

            self.codingTextboxQBox = QGroupBox("Code Editor")
            self.codingTextboxQBox.setFont(QFont(self.font, self.fontSize))
            self.codingTextboxQBox.setLayout(QVBoxLayout())
            self.codingTextboxQBox.layout().addWidget(self.codingTextbox)

            # Coding Tools
            self.codingTools = CodeEditorTools(self)

            self.codingToolsQBox = QGroupBox("Code Tools")
            self.codingToolsQBox.setFont(QFont(self.font, self.fontSize))
            self.codingToolsQBox.setLayout(QVBoxLayout())
            self.codingToolsQBox.layout().addWidget(self.codingTools)

            # Shader Output
            self.shaderOutputViewWidget = ShaderOutputView(self)

            self.shaderOutputQBox = QGroupBox("Shader Output")
            self.shaderOutputQBox.setFont(QFont(self.font, self.fontSize))
            self.shaderOutputQBox.setLayout(QVBoxLayout())
            self.shaderOutputQBox.layout().addWidget(self.shaderOutputViewWidget)

            # Shader Canvas Settings
            self.glslCanvasSettings = ShaderCanvasSettings(self.shaderOutputViewWidget)

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

            # Code Editor Splitter
            self.hSplitter3.addWidget(self.codingTextboxQBox)
            self.hSplitter3.addWidget(self.codingToolsQBox)
            self.hSplitter3.setSizes([500, 100])

            # Tab Widget
            self.tabWidget = QTabWidget()
            self.tabWidget.addTab(self.hSplitter1, "Node Editor")
            self.tabWidget.addTab(self.hSplitter3, "Coding Textbox")

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

    def runCode(self):
        self.shaderOutputViewWidget.canvas.set_fragment_shader(self.codingTextbox.getPlainCodeString())
        self.updateCanvas()


    def resetCode(self):
        print("Reset Code...")

    def updateCanvas(self):
        # trigger canvas repaint when new code is run
        self.shaderOutputViewWidget.setSize(self.shaderOutputViewWidget.canvas.width() + 1,
                                            self.shaderOutputViewWidget.canvas.height() + 1)
        self.shaderOutputViewWidget.setSize(self.shaderOutputViewWidget.canvas.width() - 1,
                                            self.shaderOutputViewWidget.canvas.height() - 1)