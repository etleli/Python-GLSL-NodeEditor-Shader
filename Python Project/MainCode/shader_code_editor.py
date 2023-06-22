from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit

from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor
from PyQt5.QtCore import QRegExp

class ShaderCodeEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

        self.codeInput.setText("#version 330\nuniform vec2 windowSize;\nout vec4 fragColor;\nvoid main() {\n\tvec2 normalizedCoords = gl_FragCoord.xy / windowSize;\n\tfragColor = vec4(normalizedCoords.x, normalizedCoords.y, 0.5, 1.0);\n}")

    def initUI(self):
        self.layout = QVBoxLayout()

        self.initialText = QLabel("#version 330\nuniform vec2 windowSize;\nout vec4 fragColor;\nvoid main() {")
        self.codeInput = PlainTextEdit()
        self.highlighter = GLSLHighlighter(self.codeInput.document())
        self.codeInput.setStyleSheet("""
            QTextEdit {
                background-color: #333333;
                color: #FFFFFF;
                font-family: Courier;
            }
        """)
        font = self.codeInput.font()
        font.setPointSize(12)
        self.codeInput.setFont(font)
        self.closingText = QLabel("}")

        # self.layout.addWidget(self.initialText)
        self.layout.addWidget(self.codeInput)
        # self.layout.addWidget(self.closingText)

        self.setLayout(self.layout)

    def getPlainCodeString(self):
        return self.codeInput.toPlainText()

class GLSLHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(GLSLHighlighter, self).__init__(parent)
        self.highlightingRules = []

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor("#eb4034"))
        keywords = ["vec2", "vec3", "vec4", "uniform", "main"]

        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            rule = (pattern, keywordFormat)
            self.highlightingRules.append(rule)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor("#ff7300"))
        keywords = ["fragColor"]

        for word in keywords:
            pattern = QRegExp("\\b" + word + "\\b")
            rule = (pattern, keywordFormat)
            self.highlightingRules.append(rule)

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

class PlainTextEdit(QTextEdit):
    def insertFromMimeData(self, source):
        self.insertPlainText(source.text())
