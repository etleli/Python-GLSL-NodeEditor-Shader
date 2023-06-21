from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from nodeeditor.utils import loadStylesheets

import os

from MainCode.shader_editor_widget import ShaderEditorWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.name_company = 'AlpHive'
        self.name_product = 'GLSL Node Shader'

        self.settings = QSettings(self.name_company, self.name_product)
        self.restoreGeometry(self.settings.value("geometry", QByteArray()))
        self.restoreState(self.settings.value("windowState", QByteArray()))

        self.initUI()

    def initUI(self):
        self.shaderEditorWindow = ShaderEditorWindow()

        self.setCentralWidget(self.shaderEditorWindow)

        self.stylesheet_filename = os.path.join(os.path.dirname(__file__), "qss/nodeeditor.qss")
        loadStylesheets(
            os.path.join(os.path.dirname(__file__), "qss/nodeeditor-dark.qss"),
            self.stylesheet_filename
        )

        self.createActions()
        self.createMenus()
        # self.createToolBars()
        # self.createStatusBar()
        # self.updateMenus()
        #
        # self.readSettings()

        self.setWindowTitle("Shader Editor")

        self.empty_icon = QIcon(".")

    def closeEvent(self, event):
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        event.accept()
        import sys
        sys.exit(0)

    def createActions(self):
        # self.actNew = QAction('&New', self, shortcut='Ctrl+N', statusTip="Create new graph", triggered=self.onFileNew)
        # self.actOpen = QAction('&Open', self, shortcut='Ctrl+O', statusTip="Open file", triggered=self.onFileOpen)
        # self.actSave = QAction('&Save', self, shortcut='Ctrl+S', statusTip="Save file", triggered=self.onFileSave)
        # self.actSaveAs = QAction('Save &As...', self, shortcut='Ctrl+Shift+S', statusTip="Save file as...", triggered=self.onFileSaveAs)
        self.actExit = QAction('E&xit', self, shortcut='Ctrl+Q', statusTip="Exit application", triggered=self.close)

        # self.actUndo = QAction('&Undo', self, shortcut='Ctrl+Z', statusTip="Undo last operation", triggered=self.onEditUndo)
        # self.actRedo = QAction('&Redo', self, shortcut='Ctrl+Shift+Z', statusTip="Redo last operation", triggered=self.onEditRedo)
        # self.actCut = QAction('Cu&t', self, shortcut='Ctrl+X', statusTip="Cut to clipboard", triggered=self.onEditCut)
        # self.actCopy = QAction('&Copy', self, shortcut='Ctrl+C', statusTip="Copy to clipboard", triggered=self.onEditCopy)
        # self.actPaste = QAction('&Paste', self, shortcut='Ctrl+V', statusTip="Paste from clipboard", triggered=self.onEditPaste)
        # self.actDelete = QAction('&Delete', self, shortcut='Del', statusTip="Delete selected items", triggered=self.onEditDelete)

    def createMenus(self):
        self.createFileMenu()
        self.createEditMenu()

    def createFileMenu(self):
        menubar = self.menuBar()
        self.fileMenu = menubar.addMenu('&File')
        # self.fileMenu.addAction(self.actNew)
        # self.fileMenu.addSeparator()
        # self.fileMenu.addAction(self.actOpen)
        # self.fileMenu.addAction(self.actSave)
        # self.fileMenu.addAction(self.actSaveAs)
        # self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actExit)

    def createEditMenu(self):
        # menubar = self.menuBar()
        # self.editMenu = menubar.addMenu('&Edit')
        # self.editMenu.addAction(self.actUndo)
        # self.editMenu.addAction(self.actRedo)
        # self.editMenu.addSeparator()
        # self.editMenu.addAction(self.actCut)
        # self.editMenu.addAction(self.actCopy)
        # self.editMenu.addAction(self.actPaste)
        # self.editMenu.addSeparator()
        # self.editMenu.addAction(self.actDelete)
        pass

    def updateMenus(self):
        active = self.getCurrentNodeEditorWidget()
        hasMdiChild = (active is not None)

        # self.actSave.setEnabled(hasMdiChild)
        # self.actSaveAs.setEnabled(hasMdiChild)
        self.actClose.setEnabled(hasMdiChild)
        self.actCloseAll.setEnabled(hasMdiChild)
        self.actTile.setEnabled(hasMdiChild)
        # self.actCascade.setEnabled(hasMdiChild)
        # self.actNext.setEnabled(hasMdiChild)
        # self.actPrevious.setEnabled(hasMdiChild)
        # self.actSeparator.setVisible(hasMdiChild)

        self.updateEditMenu()

    def updateEditMenu(self):
        # try:
        #     active = self.getCurrentNodeEditorWidget()
        #     hasMdiChild = (active is not None)
        #
        #     self.actPaste.setEnabled(hasMdiChild)
        #
        #     self.actCut.setEnabled(hasMdiChild and active.hasSelectedItems())
        #     self.actCopy.setEnabled(hasMdiChild and active.hasSelectedItems())
        #     self.actDelete.setEnabled(hasMdiChild and active.hasSelectedItems())
        #
        #     self.actUndo.setEnabled(hasMdiChild and active.canUndo())
        #     self.actRedo.setEnabled(hasMdiChild and active.canRedo())
        # except Exception as e: dumpException(e)
        pass