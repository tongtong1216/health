import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from .resources.ui.ui_main import Ui_MainWindow
from .middle.visualization import Visualization

class VisualizationWindow:
    def __init__(self,main_window):
        self.main_window = main_window
        self.ui = main_window.ui

        self.visualization_w=Visualization()

