import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from .resources.ui.ui_main import Ui_MainWindow
from .middle.register import Register

class RegisterWindow:
    def __init__(self,main_window):
        self.main_window = main_window
        self.ui = main_window.ui

        self.ui.btn_register.clicked.connect(self.handle_register)

        self.register_w = Register()

    def handle_register(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        self.main_window.current_username = username
        print("register")
        print(self.main_window.current_username)
        status = self.register_w.register(username, password)
        self.show_login_result(status,username)


    # def register_information(self,username,password,status):
    #     selected_date = self.ui.dateEdit.date()
    #     birthdate = selected_date.toString("yyyy-MM-dd")
    #     print("regiser",birthdate)
    #     information_dict = {
    #         'nickname': self.ui.name_change.text(),
    #         'gender': self.ui.sex_change.text(),
    #         'birthdate': birthdate,
    #         'height': self.ui.height_change.text(),
    #         'weight': self.ui.weight_change.text(),
    #     }
    #     print("register",information_dict)
    #     self.profileeditor_w.edit_profile(self.main_window.current_username, information_dict)
    #     self.main_window.update_information()
    #     self.show_login_result(status, username)

    def show_login_result(self, status, username):
        messages = {
            1: ("注册失败", "账户或密码不能为空"),
            2: ("注册失败", f"用户 '{username}' 已存在"),
            3: ("注册失败", "系统错误"),
            4: ("注册成功", "请牢记密码"),
        }

        title, message = messages.get(status, ("未知状态", "发生未知错误"))

        # 创建消息框
        msg_box = QMessageBox(self.main_window)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # 根据状态设置图标
        if status == 4:
            msg_box.setIcon(QMessageBox.Information)
        else:
            msg_box.setIcon(QMessageBox.Warning)

        # 添加确定按钮
        msg_box.addButton(QMessageBox.Ok)

        # 显示消息框
        msg_box.exec()

        # 在UI中显示文本
        self.ui.login_text.setText(message)

