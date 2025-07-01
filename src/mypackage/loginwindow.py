import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from .resources.ui.ui_main import Ui_MainWindow
from .middle.login import Login

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
#
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from .resources.ui.ui_main import Ui_MainWindow
from .middle.login import Login


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 确保登录页面可见
        self.ensure_login_page_visible()

        # 初始化登录处理器
        self.login_w = Login()

        # 连接登录按钮
        self.ui.btn_log_in.clicked.connect(self.handle_login)

    def ensure_login_page_visible(self):
        """确保登录页面是当前显示的页面"""
        if hasattr(self.ui, 'stackedWidget') and hasattr(self.ui, 'enterpage'):
            index = self.ui.stackedWidget.indexOf(self.ui.enterpage)
            if index >= 0:
                self.ui.stackedWidget.setCurrentIndex(index)

    def handle_login(self):
        """处理登录请求"""
        # 方法1：直接访问（如果UI结构正确）
        try:
            # 访问直接放在enterpage中的username
            username = self.ui.username.text().strip()

            # 访问log_inpage中的password
            password = self.ui.log_inpage.widget_2.password.text().strip()
        except AttributeError:
            # 方法2：使用对象名称查找
            username_input = self.findChild(QLineEdit, "username")
            password_input = self.findChild(QLineEdit, "password")

            if username_input and password_input:
                username = username_input.text().strip()
                password = password_input.text().strip()
            else:
                QMessageBox.critical(self, "系统错误", "无法找到输入框")
                return

        # 检查输入是否为空
        if not username or not password:
            QMessageBox.warning(self, "输入错误", "用户名和密码不能为空")
            return

        # 执行登录
        status = self.login_w.login(username, password)

        # 根据状态显示消息
        if status == 6:  # 登录成功
            QMessageBox.information(self, "登录成功", "登录成功！")
        else:
            error_messages = {
                1: "登录失败，账户或密码不能为空",
                2: "登录失败，用户不存在",
                3: "用户已被锁定，请稍后再试",
                4: "登录失败，密码错误",
                5: "登录失败，系统错误"
            }
            message = error_messages.get(status, "未知错误，请重试")
            QMessageBox.critical(self, "登录失败", message)