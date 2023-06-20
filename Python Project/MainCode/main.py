import os, sys
import traceback

from PyQt5.QtWidgets import QApplication, QStyleFactory

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from MainCode.main_window import MainWindow

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)

        print(QStyleFactory.keys())
        app.setStyle('Fusion')

        window = MainWindow()
        window.show()

        sys.exit(app.exec_())
    except Exception as e:
        print("Exception: ", e)
        traceback.print_exc()