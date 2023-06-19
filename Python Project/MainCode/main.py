import os, sys
from PyQt5.QtWidgets import QApplication

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from MainCode.mdi_window import ShaderEditorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # print(QStyleFactory.keys())
    app.setStyle('Fusion')

    window = ShaderEditorWindow()
    window.show()

    sys.exit(app.exec_())