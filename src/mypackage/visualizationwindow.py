import sys
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMessageBox, QVBoxLayout, QProgressBar, QLabel, QHBoxLayout
from .middle.visualization import Visualization
from datetime import date
import numpy as np
import matplotlib.pyplot as plt


class VisualizationWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = main_window.ui

        self.visual_w=Visualization()

        # 创建更小的单一画布 (8x5英寸)
        self.figure = Figure(figsize=(8, 5), dpi=80)  # 缩小尺寸和提高DPI
        self.canvas = FigureCanvas(self.figure)

        # 设置week_visual容器
        self.ui.week_visual.setLayout(QVBoxLayout())
        self.ui.week_visual.layout().setContentsMargins(0, 0, 0, 0)
        self.ui.week_visual.layout().addWidget(self.canvas)

        # 确保容器有布局
        if self.ui.day_visual.layout() is None:
            self.ui.day_visual.setLayout(QVBoxLayout())
            self.ui.day_visual.layout().setContentsMargins(10, 10, 10, 10)

        # 创建进度条和相关控件
        self.create_progress_bar()

        # 初始化坐标轴
        self.ax = None
        self.diets_index=0
        self.sports_index=0
        self.diets_keys=[]
        self.sports_keys=[]
        self.sports_dict={}
        self.diets_dict={}

        self.ui.btn_visual.clicked.connect(self.handle_visual)
        self.ui.btn_visual.clicked.connect(self.update_progress)

        self.ui.btn_diets_visual.clicked.connect(self.diets_show)
        self.ui.btn_sports_visual.clicked.connect(self.sports_show)

        self.ui.pushButton_2.clicked.connect(self.next_diets)
        self.ui.pushButton.clicked.connect(self.next_sports)



    def diets_next(self):
        self.diets_index = (self.diets_index + 1) % len(self.diets_list)
        return self.diets_index

    def sports_next(self):
        self.sports_index = (self.sports_index + 1) % len(self.sports_list)
        return self.sports_index

    def diets_show(self):
        self.diets_list = self.visual_w.get_today_food_records(self.main_window.current_username)
        self.diets_dict = self.diets_list[0]
        self.diets_index = 0
        print(self.diets_dict)
        tip=f"食物名称：{self.diets_dict['食物名称']}，摄入数量：{self.diets_dict['摄入数量']}，摄入卡路里：{self.diets_dict['卡路里摄入']}，"
        self.ui.lineEdit_2.setText(tip)

    def sports_show(self):
        self.sports_list=self.visual_w.get_today_exercise_records(self.main_window.current_username)
        self.sports_dict = self.sports_list[0]
        self.spors_index = 0
        print(self.sports_dict)
        print(self.sports_list)
        tip=f"运动日期：{self.sports_dict['运动日期']}，运动类型：{self.sports_dict['运动类型']}，运动时间：{self.sports_dict['运动时间']}，卡路里消耗{self.sports_dict['卡路里消耗']}，"
        self.ui.lineEdit.setText(tip)


    def next_sports(self):
        key = self.sports_next()
        print(key)
        self.sports_dict = self.sports_list[key]
        tip = f"运动日期：{self.sports_dict['运动日期']}，运动类型：{self.sports_dict['运动类型']}，运动时间：{self.sports_dict['运动时间']}，卡路里消耗{self.sports_dict['卡路里消耗']}，"
        self.ui.lineEdit.setText(tip)


    def next_diets(self):
        key = self.diets_next()
        print(key)
        self.diets_dict = self.diets_list[key]
        tip = f"食物名称：{self.diets_dict['食物名称']}，摄入数量：{self.diets_dict['摄入数量']}，摄入卡路里：{self.diets_dict['卡路里摄入']}，"
        self.ui.lineEdit_2.setText(tip)


    def handle_visual(self):
        """完全去除图例的简洁组合图"""
        # 获取数据
        week_sports = self.visual_w.weekly_changes(self.main_window.current_username)
        print(week_sports)
        # 清除现有图表
        self.figure.clear()

        # 创建单一坐标轴 - 使用更紧凑的布局
        self.ax = self.figure.add_axes([0.1, 0.1, 0.85, 0.8])  # 手动设置位置和大小

        try:
            # 提取数据
            dates = [item["date"] for item in week_sports]
            sports = [item["total_duration"] for item in week_sports]

            # 创建数值型位置用于X轴
            positions = list(range(len(dates)))

            # 绘制细线折线图
            self.ax.plot(positions, sports, 'b-', linewidth=1.2, alpha=0.8, zorder=1)

            # 添加小尺寸散点
            self.ax.scatter(positions, sports, s=40, color='r', alpha=0.8, zorder=2)

            # 设置更小的标题和标签
            self.ax.set_title("运动时长分析", fontsize=12, pad=8)  # pad减少间距
            self.ax.set_xlabel("日期", fontsize=10)
            self.ax.set_ylabel("时长(分钟)", fontsize=10)

            # 设置X轴刻度为日期标签 - 使用紧凑布局
            self.ax.set_xticks(positions)
            self.ax.set_xticklabels([d[5:] for d in dates], rotation=45, ha='right', fontsize=9)  # 简写日期

            # 设置Y轴刻度标签更小
            self.ax.tick_params(axis='y', labelsize=8)

            # 添加更淡的网格
            self.ax.grid(True, linestyle='-', alpha=0.1)  # 非常淡的网格

            # 调整坐标轴范围，增加一些顶部空间
            self.ax.set_ylim(min(sports) - 1, max(sports) + 5)

            # 添加简洁的边界
            for spine in self.ax.spines.values():
                spine.set_linewidth(0.5)

            # 紧凑布局 - 不再使用tight_layout
            self.canvas.draw_idle()

            # 减少背景白色区域
            self.figure.set_facecolor('#f9f9f9')
            self.ax.set_facecolor('#ffffff')

        except Exception as e:
            # 简约的错误处理
            self.ax.clear()
            self.ax.text(0.5, 0.5, "图表错误", ha='center', va='center', fontsize=10)
            self.ax.set_axis_off()
            self.canvas.draw()

    def create_progress_bar(self):
        """创建进度条组件"""
        # 清除容器内容
        while self.ui.day_visual.layout().count():
            child = self.ui.day_visual.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # 创建主布局
        layout = QVBoxLayout()
        layout.setSpacing(8)

        # 创建标题
        title = QLabel("今日运动进度")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont("Arial", 18, QFont.Bold)
        title.setFont(title_font)
        title.setStyleSheet("color: #333333;")
        layout.addWidget(title)

        # 创建进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)  # 固定范围 0-100
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setFixedHeight(25)  # 较小的高度
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #cccccc;
                border-radius: 8px;
                background-color: #f0f0f0;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 8px;
            }
        """)
        layout.addWidget(self.progress_bar)

        # 创建数值显示区域
        stats_layout = QHBoxLayout()
        stats_layout.setContentsMargins(5, 0, 5, 0)

        # 当前进度标签
        self.day_sports_label = QLabel("今日: 0")
        self.day_sports_label.setAlignment(Qt.AlignLeft)
        self.day_sports_label.setFont(QFont("Arial", 9))
        stats_layout.addWidget(self.day_sports_label)

        # 目标标签
        self.goal_label = QLabel("目标: 0")
        self.goal_label.setAlignment(Qt.AlignRight)
        self.goal_label.setFont(QFont("Arial", 9))
        stats_layout.addWidget(self.goal_label)

        layout.addLayout(stats_layout)

        # 添加布局到容器
        self.ui.day_visual.layout().addLayout(layout)

    def update_progress_bar(self, day_sports, goal):
        """更新进度条数据"""
        if goal == 0:  # 避免除以零
            percentage = 0
        else:
            # 计算百分比，但不超过100%
            percentage = min(100, int(day_sports / goal * 100))

        # 更新进度条值
        self.progress_bar.setValue(percentage)

        # 格式化显示值
        day_sports_text = f"今日: {day_sports}min"  # 可以添加单位如分钟
        goal_text = f"目标: {goal}min"  # 可以添加单位

        # 超过目标时添加特殊样式
        if day_sports >= goal:
            # 改变进度条颜色
            self.progress_bar.setStyleSheet("""
                QProgressBar {
                    border: 1px solid #cccccc;
                    border-radius: 8px;
                    background-color: #f0f0f0;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #2196F3;
                    border-radius: 8px;
                }
            """)
            goal_text = f"目标达成! {goal_text}"
        else:
            # 恢复普通样式
            self.progress_bar.setStyleSheet("""
                QProgressBar {
                    border: 1px solid #cccccc;
                    border-radius: 8px;
                    background-color: #f0f0f0;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #4CAF50;
                    border-radius: 8px;
                }
            """)

        # 更新文本显示
        self.day_sports_label.setText(day_sports_text)
        self.goal_label.setText(goal_text)

        # 更新进度条文本
        percent_text = f"{percentage}%"
        if day_sports > goal:
            percent_text += " (超额完成)"
        self.progress_bar.setFormat(percent_text)


    def update_progress(self):
        today = date.today()
        print(today)
        day_dict = self.visual_w.daily_data(self.main_window.current_username,today)
        calories_consumption = day_dict['total_calories_consumption']
        calories_intake = day_dict['total_calories_intake']
        day_sports = day_dict['total_duration']
        goal = day_dict['total_goal']
        calories_consumption_str=str(calories_consumption)
        calories_intake_str=str(calories_intake)
        self.ui.calories_consumption_line.setText(calories_consumption_str)
        self.ui.calories_intake_line.setText(calories_intake_str)
        print(day_sports)
        self.update_progress_bar(day_sports, goal)
