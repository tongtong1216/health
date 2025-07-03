import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from .resources.ui.ui_main import Ui_MainWindow
from .middle.report import Health_report

class ReportWindow:
    def __init__(self,main_window):
        self.main_window = main_window
        self.ui = main_window.ui

        self.report_w=Health_report()

        self.data_dict={}
        self.keys=[]
        self.index=-1

        self.ui.btn_creat_tips.clicked.connect(self.creat_tips)
        self.ui.btn_health_tips.clicked.connect(self.handle_report)

    def creat_tips(self):
        self.data_dict=self.report_w.health_tips(self.main_window.current_username)
        print(self.data_dict)
        self.keys=list(self.data_dict.keys())
        self.handle_report()

    def next(self):
        """获取下一个键"""
        if not self.keys:
            return None  # 空字典返回None

        self.index = (self.index + 1) % len(self.keys)
        return self.keys[self.index]

    def handle_report(self):
        key = self.next()
        print(key)
        tip = self.data_dict[key]
        print(tip)
        self.ui.health_tips_line.setText(tip)



