import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from .resources.ui.ui_main import Ui_MainWindow
from .middle.upload import Upload

class UploadWindow:
    def __init__(self,main_window):
        self.main_window = main_window
        self.ui = main_window.ui

        self.Upload_w = Upload()

        self.current_food_name=None
        self.current_sport_name=None
        self.sport_buttons = {
            self.ui.btn_basketball: "篮球",
            self.ui.btn_footballsoccer: "足球",
            self.ui.btn_slow_rope_skipping: "跳绳",
            self.ui.btn_regular_cycling: "骑自行车",
            self.ui.btn_leisure_swimming: "游泳",
            self.ui.btn_jogging: "慢跑",
            self.ui.btn_brisk_walking: "快步走",
            self.ui.btn_burpees: "波比跳",
            self.ui.btn_spring_intervals: "短跑冲刺",
            self.ui.btn_fast_jumping_jacks: "开合跳",
            self.ui.btn_explosive_high_knees: "高抬腿",
            self.ui.btn_fast_rope_skipping: "快速跳绳",
            self.ui.btn_badminton: "羽毛球",
            self.ui.btn_table_tennis: "乒乓球",
            self.ui.btn_volleyball: "排球",
            self.ui.btn_walking: "散步",
            self.ui.btn_dog_walking: "遛狗",
            self.ui.btn_gentle_yoya: "瑜伽",
            self.ui.btn_hiking: "徒步",
            self.ui.btn_mountain_climbing: "登山",
            self.ui.btn_mountain_biking: "山地自行车",
            self.ui.btn_skiing: "滑雪",
            self.ui.btn_rock_climbing: "攀岩",
            self.ui.btn_dumbbell_training: "哑铃/杠铃训练",
            self.ui.btn_push_ups: "俯卧撑",
            self.ui.btn_squats: "深蹲",
            self.ui.btn_plank: "平板支撑",
            self.ui.btn_pull_ups: "引体向上",
        }

        for button, sport_name in self.sport_buttons.items():
            button.clicked.connect(lambda checked, name=sport_name: self.set_current_sport(name))

        self.food_buttons = {
            self.ui.btn_cereals_and_tubers:"谷薯类",
            self.ui.btn_vegetables_and_fruits: "蔬菜水果类",
            self.ui.btn_animalderived_foods: "动物性食物",
            self.ui.btn_soybeans_products_nuts: "豆制品，坚果类",
            self.ui.btn_empty_calorie_foods: "纯能量食物",
        }

        for button, food_name in self.food_buttons.items():
            button.clicked.connect(lambda checked, name=food_name: self.set_current_food(name))

        self.ui.btn_food_load.clicked.connect(self.handle_food)
        self.ui.btn_sports_load.clicked.connect(self.handle_sports)

    def handle_food(self):
        intake = self.ui.food_intake.text()
        intake_int=int(intake)
        if self.current_food_name is None:
            status=0
        else:
            status=self.Upload_w.upload_food_data(self.main_window.current_username, self.current_food_name, intake_int)
        self.current_food_name =None
        self.show_food_result(status)

    def handle_sports(self):
        duration = self.ui.sports_time.text()
        duration_int = int(duration)
        if self.current_sport_name is None:
            status=0
        else:
            print(self.main_window.current_username)
            print(self.current_sport_name)
            status=self.Upload_w.upload_exercise_data(self.main_window.current_username, self.current_sport_name, duration_int)
        self.current_sport_name = None
        self.show_sport_result(status)

    def show_sport_result(self, status):
        messages = {
            0: ("操作失败", "请确认选择了运动类型"),
            1: ("操作成功", "成功加入了新的运动类型记录"),
            2: ("操作成功", "成功更新了原有的运动类型记录"),
            3: ("操作失败", "请填写0~1440内的整数"),
        }

        title, message = messages.get(status, ("未知状态", "发生未知错误"))

        # 创建消息框
        msg_box = QMessageBox(self.main_window)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # 根据状态设置图标
        if status == 1 or status == 2:
            msg_box.setIcon(QMessageBox.Information)
        else:
            msg_box.setIcon(QMessageBox.Warning)

        # 添加确定按钮
        msg_box.addButton(QMessageBox.Ok)

        # 显示消息框
        msg_box.exec()

    def show_food_result(self, status):
        messages = {
            0: ("操作失败", "请确认选择了食物种类"),
            1: ("操作成功", "成功加入了新的饮食类型记录"),
            2: ("操作成功", "成功更新了原有的饮食类型记录"),
        }

        title, message = messages.get(status, ("未知状态", "发生未知错误"))

        # 创建消息框
        msg_box = QMessageBox(self.main_window)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # 根据状态设置图标
        if status == 1 or status == 2:
            msg_box.setIcon(QMessageBox.Information)
        else:
            msg_box.setIcon(QMessageBox.Warning)

        # 添加确定按钮
        msg_box.addButton(QMessageBox.Ok)

        # 显示消息框
        msg_box.exec()

    def set_current_sport(self, sport_name):
        self.current_sport_name = sport_name

    def set_current_food(self, food_name):
        self.current_food_name = food_name