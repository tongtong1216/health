import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from src.mypackage.resources.ui.ui_main import Ui_MainWindow
from .middle.Information import ProfileEditor

class InformationWindow:
    def __init__(self, main_window):
        # 引用主窗口及其UI
        self.main_window = main_window
        self.ui = main_window.ui

        self.profileeditor_w = ProfileEditor()

        self.information_dict={
            'nickname':'',
            'gender':'',
            'height':'',
            'weight':'',
            'birthday':'',
        }
        self.ui.btn_confirm.clicked.connect(self.handle_edit_information)


    def update_information(self):
        print("update1")
        print(self.information_dict)
        self.information_dict = self.profileeditor_w.get_user_profile(self.main_window.current_username)
        print("update2")
        print(self.information_dict)
        height_str=str(self.information_dict['height'])
        weight_str=str(self.information_dict['weight'])
        self.ui.nickname.setText(self.information_dict['nickname'])
        self.ui.gender.setText(self.information_dict['gender'])
        self.ui.height.setText(height_str)
        self.ui.weight.setText(weight_str)
        self.ui.birthdate.setText(self.information_dict['birthdate'])

    def handle_edit_information(self):
        selected_date = self.ui.dateEdit.date()
        birthdate = selected_date.toString("yyyy-MM-dd")
        print(self.main_window.current_username)

        self.information_dict["nickname"] = self.ui.name_change.text()
        self.information_dict["gender"] = self.ui.sex_change.text()
        self.information_dict["birthdate"] = birthdate
        self.information_dict["height"] = self.ui.height_change.text()
        self.information_dict["weight"] = self.ui.weight_change.text()
        print("edit")
        print(self.information_dict)
        print("下面为current_username")
        print(self.main_window.current_username)
        status=self.profileeditor_w.edit_profile(self.main_window.current_username,self.information_dict)
        print("edit")
        print(status)
        self.update_information()
        self.show_edit_result(status)

    def show_edit_result(self, status):
        messages = {
            1: ("操作成功", "修改个人信息成功"),
        }

        title, message = messages.get(status, ("未知状态", "发生未知错误"))

        # 创建消息框
        msg_box = QMessageBox(self.main_window)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # 根据状态设置图标
        if status == 1:
            msg_box.setIcon(QMessageBox.Information)
        else:
            msg_box.setIcon(QMessageBox.Warning)

        # 添加确定按钮
        msg_box.addButton(QMessageBox.Ok)

        # 显示消息框
        msg_box.exec()