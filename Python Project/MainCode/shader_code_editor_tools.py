from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit

class CodeEditorTools(QWidget):
    def __init__(self, shaderEditorWindow, parent=None):
        super().__init__(parent)

        self.shaderEditorWindow = shaderEditorWindow

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.runButton = QPushButton("Run code")
        self.runButton.clicked.connect(self.run_code)

        self.outputWindow = QTextEdit()
        self.outputWindow.setReadOnly(True)

        self.resetButton = QPushButton("Reset")
        self.resetButton.clicked.connect(self.reset_output)

        self.layout.addWidget(self.runButton)
        self.layout.addWidget(self.outputWindow)
        self.layout.addWidget(self.resetButton)

        self.setLayout(self.layout)

    def run_code(self):
        # Add your code execution logic here
        # For now, it just adds a message to the output window
        # self.outputWindow.append("Running code...")
        self.shaderEditorWindow.runCode()

    def reset_output(self):
        # self.outputWindow.clear()
        self.shaderEditorWindow.resetCode()

    def outputText(self, code):
        self.outputWindow.clear()
        formatted_string = code.replace("\\n", "\n")
        self.outputWindow.setText(formatted_string)
