import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from .resources.ui.ui_main import Ui_MainWindow
from .middle.posts import PostService
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QFrame,
    QPushButton, QFileDialog
)
from PySide6.QtGui import QPixmap, QImage


class SocialWindow():
    def __init__(self, main_window):
        self.main_window = main_window
        self.ui = main_window.ui

        self.social_w =PostService()

        self.nowid=-1
        self.image_path=None

        self.ui.btn_refresh.clicked.connect(self.refresh)
        self.ui.btn_next_page.clicked.connect(self.next_page)
        self.ui.btn_like.clicked.connect(self.like)
        self.ui.btn_confirmpost.clicked.connect(self.myposts)
        self.ui.btn_image_load.clicked.connect(self.select_image)
        self.ui.btn_post.clicked.connect(self.setimage)
        self.ui.btn_pre_page.clicked.connect(self.pre_page)


    def setimage(self):
        self.image_path = None

    def like(self):
        self.social_w.increment_like_count(self.nowid)
        posts = self.social_w.get_post_by_id(self.nowid, include_image=True)
        self.ui.like_line.setText(str(posts['like_count']))


    def refresh(self):
        self.nowid=self.social_w.get_max_post_id()
        posts=self.social_w.get_post_by_id(self.nowid,include_image=True)
        self.ui.textEdit_2.setText(str(posts['content']))
        self.ui.like_line.setText(str(posts['like_count']))
        self.ui.lable_username.setText(str(posts['nickname']))
        image = QImage()
        if not image.loadFromData(posts['image_data']):
            self.ui.label_25.setText("无法加载图片数据")

        pixmap = QPixmap.fromImage(image)
        self.ui.label_25.setPixmap(pixmap)


    def pre_page(self):
        self.ui.label_25.clear()
        self.nowid = self.nowid + 1
        id=self.social_w.get_max_post_id()
        if(self.nowid>=id):
            self.nowid=id
        else:
            posts = self.social_w.get_post_by_id(self.nowid, include_image=True)
            self.ui.textEdit_2.setText(str(posts['content']))
            self.ui.like_line.setText(str(posts['like_count']))
            image_date=posts['image_data']
            image = QImage()
            if not image.loadFromData(image_date):
                self.ui.label_24.setText("无法加载图片数据")
                return False

            pixmap = QPixmap.fromImage(image)
            self.ui.label_25.setPixmap(pixmap)

    def next_page(self):
        self.ui.label_25.clear()
        self.nowid=self.nowid-1
        if(self.nowid<=0):
            self.nowid=0
        else:
            posts = self.social_w.get_post_by_id(self.nowid, include_image=True)
            self.ui.textEdit_2.setText(str(posts['content']))
            self.ui.like_line.setText(str(posts['like_count']))
            image_date = posts['image_data']
            image = QImage()
            if not image.loadFromData(image_date):
                self.ui.label_24.setText("无法加载图片数据")
                return False

            pixmap = QPixmap.fromImage(image)
            self.ui.label_25.setPixmap(pixmap)


    def myposts(self):
        content=self.ui.textEdit_4.toPlainText()
        image_date=self.image_path
        if image_date is None:
            self.social_w.create_post(self.main_window.current_usernmae,content)
        else:
            self.social_w.create_post(self.main_window.current_username,content,image_date)


    def select_image(self):
        """打开文件对话框选择图片"""
        # 设置文件过滤器，只显示图片文件
        print("选择图片")
        file_filter = "图片文件 (*.png *.jpg *.jpeg *.bmp *.gif);;所有文件 (*)"

        # 打开文件对话框
        file_path, _ = QFileDialog.getOpenFileName(
            parent=self.main_window,
            caption="选择图片",
            dir=os.path.expanduser("~"),  # 从用户主目录开始
            filter = file_filter
        )
        self.image_path= file_path