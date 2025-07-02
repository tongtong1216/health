import sys
import os
import platform
import PySide6

from src.mypackage.resources.ui import *
from src.mypackage.loginwindow import LoginWindow
from src.mypackage.registerwindow import RegisterWindow
from src.mypackage.uploadwindow import UploadWindow
from src.mypackage.informationwindow import InformationWindow
from src.mypackage.goalsettingwindow import GoalSettingWindow
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_username = None

        self.login_window = LoginWindow(self)
        self.register_window = RegisterWindow(self)
        self.upload_window = UploadWindow(self)
        self.information_window = InformationWindow(self)
        self.goalsetting_window = GoalSettingWindow(self)
        # self.information_window = InformationWindow(self)

        global widgets
        widgets = self.ui


        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - Modern GUI"
        description = "健康管理也能很有趣！打卡、挑战、数据可视化，让自律变轻松"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)



        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        #运动界面
        widgets.btn_sports.clicked.connect(self.buttonClick)
        #饮食界面
        widgets.btn_diets.clicked.connect(self.buttonClick)
        #社交页面
        widgets.btn_social.clicked.connect(self.buttonClick)
        #注册登录功能
        widgets.btn_enter.clicked.connect(self.buttonClick)
        widgets.btn_log_in.clicked.connect(self.buttonClick)
        widgets.btn_register.clicked.connect(self.buttonClick)
        #个人信息编辑页面
        widgets.btn_information.clicked.connect(self.buttonClick)
        #主题更改功能
        widgets.btn_change.clicked.connect(self.buttonClick)
        #个人信息编辑功能
        widgets.btn_edit_information.clicked.connect(self.buttonClick)
        #运动界面切换
        widgets.btn_moderate_aerobic_exercise.clicked.connect(self.buttonClick)
        widgets.btn_HIIT.clicked.connect(self.buttonClick)
        widgets.btn_strong_training.clicked.connect(self.buttonClick)
        widgets.btn_ball_sports.clicked.connect(self.buttonClick)
        widgets.btn_outdoor_sports.clicked.connect(self.buttonClick)
        widgets.btn_light_activities.clicked.connect(self.buttonClick)
        #切换到目标设定页面
        widgets.btn_goalsetting.clicked.connect(self.buttonClick)


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        # main.py
        self.current_theme = "dark"

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # def update_information(self):
    #     self.information_window.information_dict = self.information_window.profileeditor_w.get_user_profile(self.current_username)
    #     self.ui.nickname.setText(self.information_window.information_dict['nickname'])
    #     self.ui.gender.setText(self.information_window.information_dict['gender'])
    #     self.ui.birthdate.setText(self.information_window.information_dict['birthdate'])
    #     self.ui.height.setText(self.information_window.information_dict['height'])
    #     self.ui.weight.setText(self.information_window.information_dict['weight'])
    #     print("update")
    #     print(self.information_window.information_dict)

    def toggleTheme(self):
        """切换黑白主题并更新按钮颜色"""
        themes_dir = os.path.join(os.path.dirname(__file__), "resources", "themes")
        if self.current_theme == "light":
            # 切换到黑色主题
            theme_file = os.path.join(themes_dir, "py_dracula_dark.qss")
            self.current_theme = "dark"
            widgets.btn_change.setText("change 🌞")
            text_color = "#ffffff"  # 黑色主题下的白色文字
        else:
            # 切换到白色主题
            theme_file = os.path.join(themes_dir, "py_dracula_light.qss")
            self.current_theme = "light"
            widgets.btn_change.setText("change 🌙 ")
            text_color = "#000000"  # 白色主题下的黑色文字

        if os.path.exists(theme_file):
            # 应用主题
            UIFunctions.theme(self, theme_file, True)
            AppFunctions.setThemeHack(self)
            print(f"已切换到 {self.current_theme} 主题")

            # 更新所有按钮的文字颜色
            self._update_button_colors(text_color)
        else:
            print(f"错误：主题文件不存在 - {theme_file}")

    def _update_button_colors(self, color):
        """更新所有按钮的文字颜色"""
        # 更新主题切换按钮本身
        widgets.btn_change.setStyleSheet(f"color: {color};")

        # 遍历并更新其他需要随主题变色的按钮
        for btn_name in ["btn_edit_information","btn_week_step_number_view","btn_week_exercise_time_view","btn_cereals_and_tubers","btn_vegetables_and_fruits","btn_condiments","btn_animalderived_foods","btn_soybeans_products_nuts"]:  # 添加你的按钮名称
            if hasattr(widgets, btn_name):
                getattr(widgets, btn_name).setStyleSheet(f"color: {color};")
        # 应用主题...
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        #切换到主页面
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        #切换到运动界面
        if btnName == "btn_sports":
            widgets.stackedWidget.setCurrentWidget(widgets.sportspage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        #切换到饮食界面
        if btnName == "btn_diets":
            widgets.stackedWidget.setCurrentWidget(widgets.dietspage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        #切换到社交页面
        if btnName == "btn_social":
            widgets.stackedWidget.setCurrentWidget(widgets.socialpage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        #切换到信息编辑页面
        if btnName == "btn_information":
            widgets.stackedWidget.setCurrentWidget(widgets.informationpage)
            self.information_window.update_information()
            print("informationpage")
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        #切换到登录页面
        if btnName == "btn_enter":
            widgets.stackedWidget.setCurrentWidget(widgets.enterpage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        #切换主题
        if btnName == "btn_change":
           self.toggleTheme()

        #切换个人信息编辑页面
        if btnName == "btn_edit_information":
            widgets.stackedWidget.setCurrentWidget(widgets.edit_informationpage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        #周步数，运动时间切换
        if btnName == "btn_week_step_number_view":
            widgets.stackedWidget.setCurrentWidget(widgets.week_step_numberpage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_week_exercise_time_view":
            widgets.stackedWidget.setCurrentWidget(widgets.week_exercise_timepage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        #饮食录入功能
        if btnName == "btn_moderate_aerobic_exercise":
            widgets.sports_stackedWidget.setCurrentWidget(widgets.moderate_aerobic_exercisepage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_HIIT":
            widgets.sports_stackedWidget.setCurrentWidget(widgets.HIITpage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_strong_training":
            widgets.sports_stackedWidget.setCurrentWidget(widgets.strong_trainingpage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_ball_sports":
            widgets.sports_stackedWidget.setCurrentWidget(widgets.ball_sportspage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_outdoor_sports":
            widgets.sports_stackedWidget.setCurrentWidget(widgets.outdoor_sportspage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_light_activities":
            widgets.sports_stackedWidget.setCurrentWidget(widgets.light_activitiespage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_goalsetting":
            widgets.stackedWidget.setCurrentWidget(widgets.goalsettingpage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))



    # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
