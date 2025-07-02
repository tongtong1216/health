import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from .resources.ui.ui_main import Ui_MainWindow
from .middle.goalsetting import GoalManager

class GoalSettingWindow:
    def __init__(self,main_window):
        self.main_window = main_window
        self.ui = main_window.ui

        self.goalsetting_w=GoalManager()

        self.ui.btn_goalsetting_confirm.clicked.connect(self.handle_goalsetting)

    def handle_goalsetting(self):
        duration=self.ui.goalsetting_line.text()
        duration_int=int(duration)
        print("执行")
        print(duration_int)
        print(self.main_window.current_username)
        self.goalsetting_w.update_goal(self.main_window.current_username,duration_int)
