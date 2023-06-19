import os, sys
import traceback

from PyQt5.QtWidgets import QApplication

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from MainCode.shader_editor__window import ShaderEditorWindow

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)

        # print(QStyleFactory.keys())
        app.setStyle('Fusion')

        window = ShaderEditorWindow()
        window.show()

        sys.exit(app.exec_())
    except Exception as e:
        print("Exception: ", e)
        traceback.print_exc()