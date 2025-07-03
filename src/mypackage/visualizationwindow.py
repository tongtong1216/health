# import sys
# from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import pandas as pd
# import numpy as np
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
# from .resources.ui.ui_main import Ui_MainWindow
# from .middle.visualization import Visualization
#
# class VisualizationWindow:
#     def __init__(self,main_window):
#         self.main_window = main_window
#         self.ui = main_window.ui
#
#         self.visualization_w=Visualization()
#
#
#
#         self.line_figure = Figure(figsize=(5, 4), dpi=100)
#         self.scatter_figure = Figure(figsize=(5, 4), dpi=100)
#
#         # 2. 创建可嵌入的Qt画布
#         self.line_canvas = FigureCanvas(self.line_figure)
#         self.scatter_canvas = FigureCanvas(self.scatter_figure)
#
#         # 3. 设置图表容器区域的布局边距
#         self.ui.day_visual.layout().setContentsMargins(0, 0, 0, 0)
#         self.ui.week_visual.layout().setContentsMargins(0, 0, 0, 0)
#
#         # 4. 将画布添加到指定的容器布局中
#         self.ui.day_visual.layout().addWidget(self.line_canvas)
#         self.ui.week_visual.layout().addWidget(self.scatter_canvas)
#
#         # self.today_dict={
#         #     'total_duration': '',
#         #     'total_goal': '',
#         #     'total_calories_consumption': '',
#         #     'total_calories_intake': ''
#         # }
#
#         self.ui.btn_visual.clicked.connect(self.handle_visual)
#
#
#     def handle_visual(self):
#
#         self.line_figure.clear()
#         self.scatter_figure.clear()
#
#         day_dict=self.visualization_w.today_data(self.main_window.current_username)
#         week_sports=self.visualization_w.weekly_changes(self.main_window.current_username)
#
#         try:
#             # 提取键名（假设数据格式为字典列表）
#             keys = list(week_sports[0].keys())  # 获取所有字段名称
#
#             # 提取数据列
#             x_data = [item['date'] for item in week_sports]
#             y_data = [item['total_duration'] for item in week_sports]
#
#             # 绘制折线图
#             self.draw_line_chart(x_data, y_data)
#
#             # 绘制散点图
#             self.draw_scatter_chart(x_data, y_data)
#
#             # # 刷新画布
#             # self.line_canvas.draw_idle()
#             # self.scatter_canvas.draw_idle()
#
#         except:
#             print("错误")
#
#     def draw_line_chart(self, x_data, y_data):
#         """绘制专用折线图"""
#         ax = self.line_figure.add_subplot(111)
#
#         # 尝试数值转换
#         try:
#             x_num = [float(x) for x in x_data]
#             y_num = [float(y) for y in y_data]
#             ax.plot(x_num, y_num, 'b-', linewidth=2, marker='o')
#         except ValueError:
#             # 处理非数值数据（如日期或类别）
#             ax.plot(x_data, y_data, 'b-', linewidth=2)
#
#         # 设置标签和标题
#         ax.set_title("数据与运动关系折线图", fontsize=12)
#         ax.set_xlabel("数据", fontsize=10)
#         ax.set_ylabel("运动", fontsize=10)
#
#
#         # 网格和样式
#         ax.grid(True, linestyle='--', alpha=0.7)
#         self.line_figure.tight_layout()
#
#     def draw_scatter_chart(self, x_data, y_data):
#         """绘制专用散点图"""
#         ax = self.scatter_figure.add_subplot(111)
#
#         # 尝试数值转换
#         try:
#             x_num = [float(x) for x in x_data]
#             y_num = [float(y) for y in y_data]
#             scatter = ax.scatter(x_num, y_num, c='r', s=50, alpha=0.7)
#         except ValueError:
#             # 处理非数值数据 - 使用位置映射
#             unique_x = list(set(x_data))
#             unique_y = list(set(y_data))
#             x_map = {val: i for i, val in enumerate(unique_x)}
#             y_map = {val: i for i, val in enumerate(unique_y)}
#
#             x_num = [x_map[x] for x in x_data]
#             y_num = [y_map[y] for y in y_data]
#             scatter = ax.scatter(x_num, y_num, c='g', s=50, alpha=0.7)
#
#             # 设置刻度标签
#             ax.set_xticks(range(len(unique_x)))
#             ax.set_xticklabels(unique_x, rotation=45)
#             ax.set_yticks(range(len(unique_y)))
#             ax.set_yticklabels(unique_y)
#
#         # 设置标签和标题
#         ax.set_title("数据与运动关系散点图", fontsize=12)
#         ax.set_xlabel("数据", fontsize=10)
#         ax.set_ylabel("运动", fontsize=10)
#
#         # # 添加回归线（数值数据）
#         # if isinstance(x_num[0], (int, float)) and isinstance(y_num[0], (int, float)):
#         #     try:
#         #         # 计算线性回归
#         #         slope, intercept = np.polyfit(x_num, y_num, 1)
#         #         ax.plot(x_num, [slope * x + intercept for x in x_num], 'r--')
#         #     except:
#         #         pass
#
#         # 网格和样式
#         ax.grid(True, linestyle=':', alpha=0.5)
#         self.scatter_figure.tight_layout()


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

        self.ui.btn_visual.clicked.connect(self.handle_visual)
        self.ui.btn_visual.clicked.connect(self.update_progress)

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
        day_sports_text = f"今日: {day_sports}"  # 可以添加单位如分钟
        goal_text = f"目标: {goal}"  # 可以添加单位

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
        day_sports = day_dict['total_duration']
        goal = day_dict['total_goal']
        print(day_sports)
        self.update_progress_bar(day_sports, goal)
