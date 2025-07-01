# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow
# from .resources.ui.ui_main import Ui_MainWindow
# from .middle.login import Login
#
# class LoginWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.login_w=Login()
#         self.ui.btn_log_in.clicked.connect(self.handle_login)
#
#
#     #返回登录结果
#     def handle_login(self):
#         Username = self.ui.username.text()
#         Password = self.ui.password.text()
#         status=self.login_w.login(Username,Password)
#         if status==1:
#             self.ui.login_text.setText("登录失败，账户或密码不能为空")
#         if status==2:
#             self.ui.login_text.setText("登录失败，用户不存在")
#         if status==3:
#             self.ui.login_text.setText("用户已被锁定，请稍后再试")
#         if status==4:
#             self.ui.login_text.setText("登录失败，密码错误")
#         if status==5:
#             self.ui.login_text.setText("登录失败，系统错误")
#         if status==6:
#             self.ui.login_text.setText("登录成功")
#
#
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from .resources.ui.ui_main import Ui_MainWindow
from .middle.login import Login


class LoginWindow:
    def __init__(self, main_window):
        # 引用主窗口及其UI
        self.main_window = main_window
        self.ui = main_window.ui

        # 设置密码框为密码模式
        self.ui.password.setEchoMode(QLineEdit.Password)

        # 连接登录按钮
        self.ui.btn_log_in.clicked.connect(self.handle_login)

        # 初始化登录逻辑
        self.login_w = Login()

    def handle_login(self):
        # 直接从主窗口的UI元素获取输入值
        username = self.ui.username.text()
        password = self.ui.password.text()

        # 调用登录逻辑
        status = self.login_w.login(username, password)

        # 根据状态码显示结果
        self.show_login_result(status, username)

    def show_login_result(self, status, username):
        """根据登录状态显示结果消息"""
        messages = {
            1: ("登录失败", "账户或密码不能为空"),
            2: ("登录失败", f"用户 '{username}' 不存在"),
            3: ("账户锁定", "用户已被锁定，请稍后再试"),
            4: ("登录失败", "密码错误"),
            5: ("系统错误", "登录失败，系统错误"),
            6: ("登录成功", f"欢迎回来，{username}!")
        }

        title, message = messages.get(status, ("未知状态", "发生未知错误"))

        # 创建消息框
        msg_box = QMessageBox(self.main_window)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # 根据状态设置图标
        if status == 6:
            msg_box.setIcon(QMessageBox.Information)
        else:
            msg_box.setIcon(QMessageBox.Warning)

        # 添加确定按钮
        msg_box.addButton(QMessageBox.Ok)

        # 显示消息框
        msg_box.exec()

        # 在UI中显示文本
        self.ui.login_text.setText(message)

        # 调试输出
        print(f"登录状态: {status} - {message}")