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
        # 检查stackedWidget是否存在
        if not hasattr(self.ui, 'stackedWidget'):
            print("警告：无法找到stackedWidget")
            return

        # 查找enterpage的索引
        found = False
        for i in range(self.ui.stackedWidget.count()):
            widget = self.ui.stackedWidget.widget(i)
            if widget.objectName() == "enterpage":
                self.ui.stackedWidget.setCurrentIndex(i)
                found = True
                break

        if not found:
            print("警告：无法找到登录页面")

    def find_inputs(self):
        """查找用户名和密码输入框"""
        # 先尝试直接访问
        try:
            # 访问log_inpage中的username输入框
            username_input = self.ui.log_inpage.username
            password_input = self.ui.log_inpage.password
            return username_input, password_input
        except AttributeError:
            pass

        # 如果直接访问失败，尝试查找对象
        username_input = self.findChild(QLineEdit, "username")
        password_input = self.findChild(QLineEdit, "password")

        return username_input, password_input

    def handle_login(self):
        """处理登录请求"""
        # 查找输入框
        username_input, password_input = self.find_inputs()

        # 验证输入框是否找到
        if not username_input or not password_input:
            QMessageBox.critical(self, "系统错误", "无法找到用户名或密码输入框")
            return

        # 获取输入内容
        username = username_input.text().strip()
        password = password_input.text().strip()

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