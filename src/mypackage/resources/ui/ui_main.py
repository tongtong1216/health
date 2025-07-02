# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainweshdp.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 631)
        MainWindow.setMinimumSize(QSize(940, 28))
        MainWindow.setMaximumSize(QSize(940, 16777215))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"")
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Bold)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_sports = QPushButton(self.topMenu)
        self.btn_sports.setObjectName(u"btn_sports")
        sizePolicy.setHeightForWidth(self.btn_sports.sizePolicy().hasHeightForWidth())
        self.btn_sports.setSizePolicy(sizePolicy)
        self.btn_sports.setMinimumSize(QSize(0, 45))
        self.btn_sports.setFont(font)
        self.btn_sports.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sports.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_sports.setStyleSheet(u"background-image: url(:/icons/images/icons/sports.png);")

        self.verticalLayout_8.addWidget(self.btn_sports)

        self.btn_diets = QPushButton(self.topMenu)
        self.btn_diets.setObjectName(u"btn_diets")
        sizePolicy.setHeightForWidth(self.btn_diets.sizePolicy().hasHeightForWidth())
        self.btn_diets.setSizePolicy(sizePolicy)
        self.btn_diets.setMinimumSize(QSize(0, 45))
        self.btn_diets.setFont(font)
        self.btn_diets.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_diets.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_diets.setStyleSheet(u"background-image: url(:/icons/images/icons/diets.png);")

        self.verticalLayout_8.addWidget(self.btn_diets)

        self.btn_social = QPushButton(self.topMenu)
        self.btn_social.setObjectName(u"btn_social")
        self.btn_social.setMinimumSize(QSize(0, 45))
        self.btn_social.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_social.setStyleSheet(u"background-image: url(:/icons/images/icons/social.png);")

        self.verticalLayout_8.addWidget(self.btn_social)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_9 = QWidget(self.leftMenuFrame)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")

        self.verticalMenuLayout.addWidget(self.widget_9)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_enter = QPushButton(self.rightButtons)
        self.btn_enter.setObjectName(u"btn_enter")
        self.btn_enter.setMinimumSize(QSize(28, 28))
        self.btn_enter.setMaximumSize(QSize(28, 28))
        self.btn_enter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/32529/.designer/images/icons/cil-user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_enter.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_enter)

        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        self.closeAppBtn.raise_()
        self.settingsTopBtn.raise_()
        self.minimizeAppBtn.raise_()
        self.maximizeRestoreAppBtn.raise_()
        self.btn_enter.raise_()

        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFont(font)
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u" background-image: none;\n"
"    background-color: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/homebackground.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.horizontalLayout_6 = QHBoxLayout(self.home)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sports_time_view = QFrame(self.home)
        self.sports_time_view.setObjectName(u"sports_time_view")
        self.sports_time_view.setFrameShape(QFrame.Shape.StyledPanel)
        self.sports_time_view.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.sports_time_view)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_11 = QWidget(self.sports_time_view)
        self.widget_11.setObjectName(u"widget_11")
        self.groupBox_3 = QGroupBox(self.widget_11)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 10, 361, 151))
        self.groupBox_4 = QGroupBox(self.widget_11)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(410, 10, 361, 151))

        self.verticalLayout_22.addWidget(self.widget_11)

        self.widget_3 = QWidget(self.sports_time_view)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_24.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_24.addWidget(self.lineEdit)


        self.verticalLayout_22.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignBottom)

        self.widget_10 = QWidget(self.sports_time_view)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.btn_creat_tips = QPushButton(self.widget_10)
        self.btn_creat_tips.setObjectName(u"btn_creat_tips")

        self.horizontalLayout_25.addWidget(self.btn_creat_tips)

        self.label_12 = QLabel(self.widget_10)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_25.addWidget(self.label_12)

        self.health_tips_line = QLineEdit(self.widget_10)
        self.health_tips_line.setObjectName(u"health_tips_line")

        self.horizontalLayout_25.addWidget(self.health_tips_line)

        self.btn_health_tips = QPushButton(self.widget_10)
        self.btn_health_tips.setObjectName(u"btn_health_tips")

        self.horizontalLayout_25.addWidget(self.btn_health_tips)


        self.verticalLayout_22.addWidget(self.widget_10)

        self.btn_goalsetting = QPushButton(self.sports_time_view)
        self.btn_goalsetting.setObjectName(u"btn_goalsetting")

        self.verticalLayout_22.addWidget(self.btn_goalsetting)


        self.horizontalLayout_6.addWidget(self.sports_time_view)

        self.stackedWidget.addWidget(self.home)
        self.week_step_numberpage = QWidget()
        self.week_step_numberpage.setObjectName(u"week_step_numberpage")
        self.stackedWidget.addWidget(self.week_step_numberpage)
        self.goalsettingpage = QWidget()
        self.goalsettingpage.setObjectName(u"goalsettingpage")
        self.verticalLayout_23 = QVBoxLayout(self.goalsettingpage)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_6 = QFrame(self.goalsettingpage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_26.addWidget(self.label_13)

        self.goalsetting_line = QLineEdit(self.frame_6)
        self.goalsetting_line.setObjectName(u"goalsetting_line")

        self.horizontalLayout_26.addWidget(self.goalsetting_line)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_26.addWidget(self.label_14)

        self.btn_goalsetting_confirm = QPushButton(self.frame_6)
        self.btn_goalsetting_confirm.setObjectName(u"btn_goalsetting_confirm")

        self.horizontalLayout_26.addWidget(self.btn_goalsetting_confirm)


        self.verticalLayout_23.addWidget(self.frame_6)

        self.widget_12 = QWidget(self.goalsettingpage)
        self.widget_12.setObjectName(u"widget_12")

        self.verticalLayout_23.addWidget(self.widget_12)

        self.stackedWidget.addWidget(self.goalsettingpage)
        self.enterpage = QWidget()
        self.enterpage.setObjectName(u"enterpage")
        self.verticalLayout_18 = QVBoxLayout(self.enterpage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_2 = QLabel(self.enterpage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_18.addWidget(self.label_2)

        self.username = QLineEdit(self.enterpage)
        self.username.setObjectName(u"username")
        self.username.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_18.addWidget(self.username)

        self.label_3 = QLabel(self.enterpage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_18.addWidget(self.label_3)

        self.password = QLineEdit(self.enterpage)
        self.password.setObjectName(u"password")
        self.password.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_18.addWidget(self.password)

        self.login_text = QLabel(self.enterpage)
        self.login_text.setObjectName(u"login_text")
        self.login_text.setMaximumSize(QSize(6666666, 50))

        self.verticalLayout_18.addWidget(self.login_text)

        self.btn_log_in = QPushButton(self.enterpage)
        self.btn_log_in.setObjectName(u"btn_log_in")
        self.btn_log_in.setCursor(QCursor(Qt.CursorShape.SizeAllCursor))

        self.verticalLayout_18.addWidget(self.btn_log_in)

        self.btn_register = QPushButton(self.enterpage)
        self.btn_register.setObjectName(u"btn_register")

        self.verticalLayout_18.addWidget(self.btn_register)

        self.stackedWidget.addWidget(self.enterpage)
        self.informationpage = QWidget()
        self.informationpage.setObjectName(u"informationpage")
        self.verticalLayout_21 = QVBoxLayout(self.informationpage)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_2 = QFrame(self.informationpage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.nickname = QLineEdit(self.widget_4)
        self.nickname.setObjectName(u"nickname")
        self.nickname.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.nickname)


        self.verticalLayout_19.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.frame_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.gender = QLineEdit(self.widget_5)
        self.gender.setObjectName(u"gender")
        self.gender.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.gender)


        self.verticalLayout_19.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.frame_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_13.addWidget(self.label_7)

        self.height = QLineEdit(self.widget_6)
        self.height.setObjectName(u"height")
        self.height.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.height)


        self.verticalLayout_19.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.frame_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_14.addWidget(self.label_8)

        self.weight = QLineEdit(self.widget_7)
        self.weight.setObjectName(u"weight")
        self.weight.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.weight)


        self.verticalLayout_19.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.frame_2)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_15.addWidget(self.label_9)

        self.birthdate = QLineEdit(self.widget_8)
        self.birthdate.setObjectName(u"birthdate")
        self.birthdate.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.birthdate)


        self.verticalLayout_19.addWidget(self.widget_8)

        self.btn_edit_information = QPushButton(self.frame_2)
        self.btn_edit_information.setObjectName(u"btn_edit_information")

        self.verticalLayout_19.addWidget(self.btn_edit_information)


        self.verticalLayout_21.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.informationpage)
        self.edit_informationpage = QWidget()
        self.edit_informationpage.setObjectName(u"edit_informationpage")
        self.verticalLayout_15 = QVBoxLayout(self.edit_informationpage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_3 = QFrame(self.edit_informationpage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.dateEdit = QDateEdit(self.frame_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(300, 220, 122, 22))
        self.dateEdit.setMaximumDateTime(QDateTime(QDate(2025, 12, 31), QTime(23, 59, 59)))
        self.dateEdit.setMaximumDate(QDate(2025, 12, 31))
        self.dateEdit.setMinimumDate(QDate(1900, 9, 14))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(160, 50, 54, 16))
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(160, 96, 54, 20))
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(160, 140, 54, 16))
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(160, 180, 54, 16))
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(160, 220, 54, 16))
        self.name_change = QLineEdit(self.frame_3)
        self.name_change.setObjectName(u"name_change")
        self.name_change.setGeometry(QRect(300, 50, 113, 20))
        self.sex_change = QLineEdit(self.frame_3)
        self.sex_change.setObjectName(u"sex_change")
        self.sex_change.setGeometry(QRect(300, 100, 113, 20))
        self.height_change = QLineEdit(self.frame_3)
        self.height_change.setObjectName(u"height_change")
        self.height_change.setGeometry(QRect(300, 140, 113, 20))
        self.weight_change = QLineEdit(self.frame_3)
        self.weight_change.setObjectName(u"weight_change")
        self.weight_change.setGeometry(QRect(300, 190, 113, 20))
        self.btn_confirm = QPushButton(self.frame_3)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setGeometry(QRect(290, 290, 75, 24))
        self.btn_return = QPushButton(self.frame_3)
        self.btn_return.setObjectName(u"btn_return")
        self.btn_return.setGeometry(QRect(690, 10, 75, 24))

        self.verticalLayout_15.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.edit_informationpage)
        self.dietspage = QWidget()
        self.dietspage.setObjectName(u"dietspage")
        self.verticalLayout_16 = QVBoxLayout(self.dietspage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame = QFrame(self.dietspage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_23.addWidget(self.label_10)

        self.food_intake = QLineEdit(self.widget_2)
        self.food_intake.setObjectName(u"food_intake")
        self.food_intake.setMaximumSize(QSize(1677721, 16777215))
        self.food_intake.setMaxLength(8)

        self.horizontalLayout_23.addWidget(self.food_intake)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_23.addWidget(self.label_11)

        self.btn_food_load = QPushButton(self.widget_2)
        self.btn_food_load.setObjectName(u"btn_food_load")

        self.horizontalLayout_23.addWidget(self.btn_food_load)


        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_22 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_cereals_and_tubers = QPushButton(self.groupBox)
        self.btn_cereals_and_tubers.setObjectName(u"btn_cereals_and_tubers")
        self.btn_cereals_and_tubers.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cereals_and_tubers.setStyleSheet(u"QWidget:pressed {\n"
"    background-color: #9D4EDD;  /* \u6d45\u7d2b\u8272\uff0cRGB\u503c\u53ef\u8c03\u6574 */\n"
"    color: white;               /* \u6587\u5b57\u767d\u8272 */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.btn_cereals_and_tubers)

        self.btn_vegetables_and_fruits = QPushButton(self.groupBox)
        self.btn_vegetables_and_fruits.setObjectName(u"btn_vegetables_and_fruits")
        self.btn_vegetables_and_fruits.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_vegetables_and_fruits.setStyleSheet(u"QWidget:pressed {\n"
"    background-color: #9D4EDD;  /* \u6d45\u7d2b\u8272\uff0cRGB\u503c\u53ef\u8c03\u6574 */\n"
"    color: white;               /* \u6587\u5b57\u767d\u8272 */\n"
"}\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.btn_vegetables_and_fruits)

        self.btn_animalderived_foods = QPushButton(self.groupBox)
        self.btn_animalderived_foods.setObjectName(u"btn_animalderived_foods")
        self.btn_animalderived_foods.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_22.addWidget(self.btn_animalderived_foods)

        self.btn_soybeans_products_nuts = QPushButton(self.groupBox)
        self.btn_soybeans_products_nuts.setObjectName(u"btn_soybeans_products_nuts")
        self.btn_soybeans_products_nuts.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_22.addWidget(self.btn_soybeans_products_nuts)

        self.btn_empty_calorie_foods = QPushButton(self.groupBox)
        self.btn_empty_calorie_foods.setObjectName(u"btn_empty_calorie_foods")
        self.btn_empty_calorie_foods.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_22.addWidget(self.btn_empty_calorie_foods)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.verticalLayout_16.addWidget(self.frame)

        self.stackedWidget.addWidget(self.dietspage)
        self.socialpage = QWidget()
        self.socialpage.setObjectName(u"socialpage")
        self.socialpage.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.socialpage)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_4 = QFrame(self.socialpage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_refresh = QPushButton(self.frame_4)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(700, 20, 75, 51))
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(40, 99, 731, 361))
        self.frame_5.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 140, 121, 81))
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.socialpage)
        self.sportspage = QWidget()
        self.sportspage.setObjectName(u"sportspage")
        self.verticalLayout_20 = QVBoxLayout(self.sportspage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_7 = QFrame(self.sportspage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_2 = QGroupBox(self.frame_7)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 999))
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_moderate_aerobic_exercise = QPushButton(self.groupBox_2)
        self.btn_moderate_aerobic_exercise.setObjectName(u"btn_moderate_aerobic_exercise")

        self.horizontalLayout_8.addWidget(self.btn_moderate_aerobic_exercise)

        self.btn_HIIT = QPushButton(self.groupBox_2)
        self.btn_HIIT.setObjectName(u"btn_HIIT")

        self.horizontalLayout_8.addWidget(self.btn_HIIT)

        self.btn_strong_training = QPushButton(self.groupBox_2)
        self.btn_strong_training.setObjectName(u"btn_strong_training")

        self.horizontalLayout_8.addWidget(self.btn_strong_training)

        self.btn_ball_sports = QPushButton(self.groupBox_2)
        self.btn_ball_sports.setObjectName(u"btn_ball_sports")

        self.horizontalLayout_8.addWidget(self.btn_ball_sports)

        self.btn_outdoor_sports = QPushButton(self.groupBox_2)
        self.btn_outdoor_sports.setObjectName(u"btn_outdoor_sports")

        self.horizontalLayout_8.addWidget(self.btn_outdoor_sports)

        self.btn_light_activities = QPushButton(self.groupBox_2)
        self.btn_light_activities.setObjectName(u"btn_light_activities")

        self.horizontalLayout_8.addWidget(self.btn_light_activities)


        self.verticalLayout_17.addWidget(self.groupBox_2)

        self.widget = QWidget(self.frame_7)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 600))
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_9.addWidget(self.label_23)

        self.sports_time = QLineEdit(self.widget)
        self.sports_time.setObjectName(u"sports_time")
        self.sports_time.setMaxLength(4)

        self.horizontalLayout_9.addWidget(self.sports_time)

        self.btn_sports_load = QPushButton(self.widget)
        self.btn_sports_load.setObjectName(u"btn_sports_load")

        self.horizontalLayout_9.addWidget(self.btn_sports_load)


        self.verticalLayout_17.addWidget(self.widget)

        self.sports_stackedWidget = QStackedWidget(self.frame_7)
        self.sports_stackedWidget.setObjectName(u"sports_stackedWidget")
        self.sports_stackedWidget.setMaximumSize(QSize(16777215, 900))
        self.moderate_aerobic_exercisepage = QWidget()
        self.moderate_aerobic_exercisepage.setObjectName(u"moderate_aerobic_exercisepage")
        self.horizontalLayout_10 = QHBoxLayout(self.moderate_aerobic_exercisepage)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_slow_rope_skipping = QPushButton(self.moderate_aerobic_exercisepage)
        self.btn_slow_rope_skipping.setObjectName(u"btn_slow_rope_skipping")

        self.horizontalLayout_10.addWidget(self.btn_slow_rope_skipping)

        self.btn_regular_cycling = QPushButton(self.moderate_aerobic_exercisepage)
        self.btn_regular_cycling.setObjectName(u"btn_regular_cycling")

        self.horizontalLayout_10.addWidget(self.btn_regular_cycling)

        self.btn_leisure_swimming = QPushButton(self.moderate_aerobic_exercisepage)
        self.btn_leisure_swimming.setObjectName(u"btn_leisure_swimming")

        self.horizontalLayout_10.addWidget(self.btn_leisure_swimming)

        self.btn_jogging = QPushButton(self.moderate_aerobic_exercisepage)
        self.btn_jogging.setObjectName(u"btn_jogging")

        self.horizontalLayout_10.addWidget(self.btn_jogging)

        self.btn_brisk_walking = QPushButton(self.moderate_aerobic_exercisepage)
        self.btn_brisk_walking.setObjectName(u"btn_brisk_walking")

        self.horizontalLayout_10.addWidget(self.btn_brisk_walking)

        self.sports_stackedWidget.addWidget(self.moderate_aerobic_exercisepage)
        self.HIITpage = QWidget()
        self.HIITpage.setObjectName(u"HIITpage")
        self.horizontalLayout_17 = QHBoxLayout(self.HIITpage)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_burpees = QPushButton(self.HIITpage)
        self.btn_burpees.setObjectName(u"btn_burpees")

        self.horizontalLayout_17.addWidget(self.btn_burpees)

        self.btn_spring_intervals = QPushButton(self.HIITpage)
        self.btn_spring_intervals.setObjectName(u"btn_spring_intervals")

        self.horizontalLayout_17.addWidget(self.btn_spring_intervals)

        self.btn_fast_jumping_jacks = QPushButton(self.HIITpage)
        self.btn_fast_jumping_jacks.setObjectName(u"btn_fast_jumping_jacks")

        self.horizontalLayout_17.addWidget(self.btn_fast_jumping_jacks)

        self.btn_explosive_high_knees = QPushButton(self.HIITpage)
        self.btn_explosive_high_knees.setObjectName(u"btn_explosive_high_knees")

        self.horizontalLayout_17.addWidget(self.btn_explosive_high_knees)

        self.btn_fast_rope_skipping = QPushButton(self.HIITpage)
        self.btn_fast_rope_skipping.setObjectName(u"btn_fast_rope_skipping")

        self.horizontalLayout_17.addWidget(self.btn_fast_rope_skipping)

        self.sports_stackedWidget.addWidget(self.HIITpage)
        self.strong_trainingpage = QWidget()
        self.strong_trainingpage.setObjectName(u"strong_trainingpage")
        self.horizontalLayout_18 = QHBoxLayout(self.strong_trainingpage)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_dumbbell_training = QPushButton(self.strong_trainingpage)
        self.btn_dumbbell_training.setObjectName(u"btn_dumbbell_training")

        self.horizontalLayout_18.addWidget(self.btn_dumbbell_training)

        self.btn_push_ups = QPushButton(self.strong_trainingpage)
        self.btn_push_ups.setObjectName(u"btn_push_ups")

        self.horizontalLayout_18.addWidget(self.btn_push_ups)

        self.btn_squats = QPushButton(self.strong_trainingpage)
        self.btn_squats.setObjectName(u"btn_squats")

        self.horizontalLayout_18.addWidget(self.btn_squats)

        self.btn_plank = QPushButton(self.strong_trainingpage)
        self.btn_plank.setObjectName(u"btn_plank")

        self.horizontalLayout_18.addWidget(self.btn_plank)

        self.btn_pull_ups = QPushButton(self.strong_trainingpage)
        self.btn_pull_ups.setObjectName(u"btn_pull_ups")

        self.horizontalLayout_18.addWidget(self.btn_pull_ups)

        self.sports_stackedWidget.addWidget(self.strong_trainingpage)
        self.ball_sportspage = QWidget()
        self.ball_sportspage.setObjectName(u"ball_sportspage")
        self.horizontalLayout_19 = QHBoxLayout(self.ball_sportspage)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btn_basketball = QPushButton(self.ball_sportspage)
        self.btn_basketball.setObjectName(u"btn_basketball")

        self.horizontalLayout_19.addWidget(self.btn_basketball)

        self.btn_footballsoccer = QPushButton(self.ball_sportspage)
        self.btn_footballsoccer.setObjectName(u"btn_footballsoccer")

        self.horizontalLayout_19.addWidget(self.btn_footballsoccer)

        self.btn_badminton = QPushButton(self.ball_sportspage)
        self.btn_badminton.setObjectName(u"btn_badminton")

        self.horizontalLayout_19.addWidget(self.btn_badminton)

        self.btn_table_tennis = QPushButton(self.ball_sportspage)
        self.btn_table_tennis.setObjectName(u"btn_table_tennis")

        self.horizontalLayout_19.addWidget(self.btn_table_tennis)

        self.btn_tennis = QPushButton(self.ball_sportspage)
        self.btn_tennis.setObjectName(u"btn_tennis")

        self.horizontalLayout_19.addWidget(self.btn_tennis)

        self.btn_volleyball = QPushButton(self.ball_sportspage)
        self.btn_volleyball.setObjectName(u"btn_volleyball")

        self.horizontalLayout_19.addWidget(self.btn_volleyball)

        self.sports_stackedWidget.addWidget(self.ball_sportspage)
        self.outdoor_sportspage = QWidget()
        self.outdoor_sportspage.setObjectName(u"outdoor_sportspage")
        self.horizontalLayout_20 = QHBoxLayout(self.outdoor_sportspage)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.btn_hiking = QPushButton(self.outdoor_sportspage)
        self.btn_hiking.setObjectName(u"btn_hiking")

        self.horizontalLayout_20.addWidget(self.btn_hiking)

        self.btn_mountain_climbing = QPushButton(self.outdoor_sportspage)
        self.btn_mountain_climbing.setObjectName(u"btn_mountain_climbing")

        self.horizontalLayout_20.addWidget(self.btn_mountain_climbing)

        self.btn_mountain_biking = QPushButton(self.outdoor_sportspage)
        self.btn_mountain_biking.setObjectName(u"btn_mountain_biking")

        self.horizontalLayout_20.addWidget(self.btn_mountain_biking)

        self.btn_skiing = QPushButton(self.outdoor_sportspage)
        self.btn_skiing.setObjectName(u"btn_skiing")

        self.horizontalLayout_20.addWidget(self.btn_skiing)

        self.btn_rock_climbing = QPushButton(self.outdoor_sportspage)
        self.btn_rock_climbing.setObjectName(u"btn_rock_climbing")

        self.horizontalLayout_20.addWidget(self.btn_rock_climbing)

        self.sports_stackedWidget.addWidget(self.outdoor_sportspage)
        self.light_activitiespage = QWidget()
        self.light_activitiespage.setObjectName(u"light_activitiespage")
        self.horizontalLayout_21 = QHBoxLayout(self.light_activitiespage)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_walking = QPushButton(self.light_activitiespage)
        self.btn_walking.setObjectName(u"btn_walking")

        self.horizontalLayout_21.addWidget(self.btn_walking)

        self.btn_dog_walking = QPushButton(self.light_activitiespage)
        self.btn_dog_walking.setObjectName(u"btn_dog_walking")

        self.horizontalLayout_21.addWidget(self.btn_dog_walking)

        self.btn_gentle_yoya = QPushButton(self.light_activitiespage)
        self.btn_gentle_yoya.setObjectName(u"btn_gentle_yoya")

        self.horizontalLayout_21.addWidget(self.btn_gentle_yoya)

        self.sports_stackedWidget.addWidget(self.light_activitiespage)

        self.verticalLayout_17.addWidget(self.sports_stackedWidget, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_20.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.sportspage)

        self.horizontalLayout_7.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_information = QPushButton(self.topMenus)
        self.btn_information.setObjectName(u"btn_information")
        sizePolicy.setHeightForWidth(self.btn_information.sizePolicy().hasHeightForWidth())
        self.btn_information.setSizePolicy(sizePolicy)
        self.btn_information.setMinimumSize(QSize(0, 45))
        self.btn_information.setFont(font)
        self.btn_information.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.btn_information.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_information.setStyleSheet(u"background-image: url(:/icons/images/icons/selfinformation.png);")

        self.verticalLayout_14.addWidget(self.btn_information)

        self.btn_change = QPushButton(self.topMenus)
        self.btn_change.setObjectName(u"btn_change")
        sizePolicy.setHeightForWidth(self.btn_change.sizePolicy().hasHeightForWidth())
        self.btn_change.setSizePolicy(sizePolicy)
        self.btn_change.setMinimumSize(QSize(0, 45))
        self.btn_change.setFont(font)
        self.btn_change.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_change.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_change.setStyleSheet(u"background-image: url(:/icons/images/icons/change_theme.png);")

        self.verticalLayout_14.addWidget(self.btn_change)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText("")
        self.titleLeftDescription.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_sports.setText(QCoreApplication.translate("MainWindow", u"sports", None))
        self.btn_diets.setText(QCoreApplication.translate("MainWindow", u"diets", None))
        self.btn_social.setText(QCoreApplication.translate("MainWindow", u"social", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
        self.btn_enter.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u8fd0\u52a8\u65f6\u95f4\u53ef\u89c6\u5316", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5468\u8fd0\u52a8\u65f6\u95f4\u53ef\u89c6\u5316", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u5361\u8def\u91cc\u6536\u652f\uff1a</span></p></body></html>", None))
        self.btn_creat_tips.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u67e5\u770b\u5065\u5eb7\u5c0f\u63d0\u793a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5065\u5eb7\u5c0f\u63d0\u793a", None))
        self.btn_health_tips.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u4e2a", None))
        self.btn_goalsetting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6bcf\u65e5\u8fd0\u52a8\u65f6\u957f\u76ee\u6807", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6bcf\u65e5\u76ee\u6807\u8fd0\u52a8\u65f6\u957f\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.btn_goalsetting_confirm.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u4e0a\u4f20", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.login_text.setText("")
        self.btn_log_in.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6635      \u79f0\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6027      \u522b\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8eab      \u9ad8\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u4f53       \u91cd\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u751f\u65e5\u671f\uff1a", None))
        self.btn_edit_information.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91\u4e2a\u4eba\u4fe1\u606f", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u6635\u79f0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u9ad8", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u4f53\u91cd", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u751f\u65e5\u671f", None))
        self.btn_confirm.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u66f4\u6539", None))
        self.btn_return.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u98df\u7269\u6444\u5165\u91cf\uff1a", None))
        self.food_intake.setInputMask("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"g\u6216ml", None))
        self.btn_food_load.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u4e0a\u4f20", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u98df\u7269\u79cd\u7c7b", None))
        self.btn_cereals_and_tubers.setText(QCoreApplication.translate("MainWindow", u"\u8c37\u85af\u7c7b", None))
        self.btn_vegetables_and_fruits.setText(QCoreApplication.translate("MainWindow", u"\u852c\u83dc\u6c34\u679c\u7c7b", None))
        self.btn_animalderived_foods.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u7269\u6027\u98df\u7269", None))
        self.btn_soybeans_products_nuts.setText(QCoreApplication.translate("MainWindow", u"\u8c46\u5236\u54c1\uff0c\u575a\u679c\u7c7b", None))
        self.btn_empty_calorie_foods.setText(QCoreApplication.translate("MainWindow", u"\u7eaf\u80fd\u91cf\u98df\u7269", None))
        self.btn_refresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5e16\u5b50\u5185\u5bb9", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u79cd\u7c7b", None))
        self.btn_moderate_aerobic_exercise.setText(QCoreApplication.translate("MainWindow", u"\u6709\u6c27\u8fd0\u52a8", None))
        self.btn_HIIT.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u5f3a\u5ea6\u95f4\u6b47\u8fd0\u52a8", None))
        self.btn_strong_training.setText(QCoreApplication.translate("MainWindow", u"\u529b\u91cf\u8bad\u7ec3", None))
        self.btn_ball_sports.setText(QCoreApplication.translate("MainWindow", u"\u7403\u7c7b\u8fd0\u52a8", None))
        self.btn_outdoor_sports.setText(QCoreApplication.translate("MainWindow", u"\u6237\u5916\u8fd0\u52a8", None))
        self.btn_light_activities.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5e38\u6d3b\u52a8", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u65f6\u957f\uff1a", None))
        self.sports_time.setInputMask("")
        self.btn_sports_load.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u4e0a\u4f20", None))
        self.btn_slow_rope_skipping.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u7ef3", None))
        self.btn_regular_cycling.setText(QCoreApplication.translate("MainWindow", u"\u9a91\u81ea\u884c\u8f66", None))
        self.btn_leisure_swimming.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u6cf3", None))
        self.btn_jogging.setText(QCoreApplication.translate("MainWindow", u"\u6162\u8dd1", None))
        self.btn_brisk_walking.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u6b65\u8d70", None))
        self.btn_burpees.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u6bd4\u8df3", None))
        self.btn_spring_intervals.setText(QCoreApplication.translate("MainWindow", u"\u77ed\u8dd1\u51b2\u523a", None))
        self.btn_fast_jumping_jacks.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u5408\u8df3", None))
        self.btn_explosive_high_knees.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u62ac\u817f", None))
        self.btn_fast_rope_skipping.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u8df3\u7ef3", None))
        self.btn_dumbbell_training.setText(QCoreApplication.translate("MainWindow", u"\u54d1\u94c3/\u6760\u94c3\u8bad\u7ec3", None))
        self.btn_push_ups.setText(QCoreApplication.translate("MainWindow", u"\u4fef\u5367\u6491", None))
        self.btn_squats.setText(QCoreApplication.translate("MainWindow", u"\u6df1\u8e72", None))
        self.btn_plank.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u677f\u652f\u6491", None))
        self.btn_pull_ups.setText(QCoreApplication.translate("MainWindow", u"\u5f15\u4f53\u5411\u4e0a", None))
        self.btn_basketball.setText(QCoreApplication.translate("MainWindow", u"\u7bee\u7403", None))
        self.btn_footballsoccer.setText(QCoreApplication.translate("MainWindow", u"\u8db3\u7403", None))
        self.btn_badminton.setText(QCoreApplication.translate("MainWindow", u"\u7fbd\u6bdb\u7403", None))
        self.btn_table_tennis.setText(QCoreApplication.translate("MainWindow", u"\u4e52\u4e53\u7403", None))
        self.btn_tennis.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7403", None))
        self.btn_volleyball.setText(QCoreApplication.translate("MainWindow", u"\u6392\u7403", None))
        self.btn_hiking.setText(QCoreApplication.translate("MainWindow", u"\u5f92\u6b65", None))
        self.btn_mountain_climbing.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5c71", None))
        self.btn_mountain_biking.setText(QCoreApplication.translate("MainWindow", u"\u5c71\u5730\u81ea\u884c\u8f66", None))
        self.btn_skiing.setText(QCoreApplication.translate("MainWindow", u"\u6ed1\u96ea", None))
        self.btn_rock_climbing.setText(QCoreApplication.translate("MainWindow", u"\u6500\u5ca9", None))
        self.btn_walking.setText(QCoreApplication.translate("MainWindow", u"\u6563\u6b65", None))
        self.btn_dog_walking.setText(QCoreApplication.translate("MainWindow", u"\u905b\u72d7", None))
        self.btn_gentle_yoya.setText(QCoreApplication.translate("MainWindow", u"\u745c\u4f3d", None))
        self.btn_information.setText(QCoreApplication.translate("MainWindow", u"information", None))
        self.btn_change.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"\u5149\u5b97\u8000\u7ec4", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

