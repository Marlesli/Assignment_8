# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asn8.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Root(object):
    def setupUi(self, Root):
        if not Root.objectName():
            Root.setObjectName(u"Root")
        Root.setEnabled(True)
        Root.resize(500, 300)
        self.centralwidget = QWidget(Root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblFrPerson = QGroupBox(self.centralwidget)
        self.lblFrPerson.setObjectName(u"lblFrPerson")
        self.lblFrPerson.setGeometry(QRect(0, 0, 501, 271))
        self.lblFirst = QLabel(self.lblFrPerson)
        self.lblFirst.setObjectName(u"lblFirst")
        self.lblFirst.setGeometry(QRect(150, 30, 71, 20))
        self.lblFirst.setStyleSheet(u"background-color: blue;\n"
"color: white;")
        self.entFirst = QLineEdit(self.lblFrPerson)
        self.entFirst.setObjectName(u"entFirst")
        self.entFirst.setGeometry(QRect(240, 30, 113, 26))
        self.lblLast = QLabel(self.lblFrPerson)
        self.lblLast.setObjectName(u"lblLast")
        self.lblLast.setGeometry(QRect(150, 70, 71, 20))
        self.lblLast.setStyleSheet(u"background-color: blue;\n"
"color: white;")
        self.entLast = QLineEdit(self.lblFrPerson)
        self.entLast.setObjectName(u"entLast")
        self.entLast.setGeometry(QRect(240, 70, 113, 26))
        self.lblEmail = QLabel(self.lblFrPerson)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setGeometry(QRect(160, 110, 49, 16))
        self.entEmail = QLineEdit(self.lblFrPerson)
        self.entEmail.setObjectName(u"entEmail")
        self.entEmail.setGeometry(QRect(240, 110, 113, 26))
        self.lblPhone = QLabel(self.lblFrPerson)
        self.lblPhone.setObjectName(u"lblPhone")
        self.lblPhone.setGeometry(QRect(160, 150, 49, 16))
        self.entPhone = QLineEdit(self.lblFrPerson)
        self.entPhone.setObjectName(u"entPhone")
        self.entPhone.setGeometry(QRect(240, 150, 113, 26))
        self.fraButtons = QFrame(self.lblFrPerson)
        self.fraButtons.setObjectName(u"fraButtons")
        self.fraButtons.setGeometry(QRect(100, 190, 271, 48))
        self.fraButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.fraButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnQ = QPushButton(self.fraButtons)
        self.btnQ.setObjectName(u"btnQ")

        self.horizontalLayout.addWidget(self.btnQ)

        self.btnR = QPushButton(self.fraButtons)
        self.btnR.setObjectName(u"btnR")

        self.horizontalLayout.addWidget(self.btnR)

        self.btnS = QPushButton(self.fraButtons)
        self.btnS.setObjectName(u"btnS")

        self.horizontalLayout.addWidget(self.btnS)

        Root.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Root)
        self.statusbar.setObjectName(u"statusbar")
        Root.setStatusBar(self.statusbar)

        self.retranslateUi(Root)

        QMetaObject.connectSlotsByName(Root)
    # setupUi

    def retranslateUi(self, Root):
        Root.setWindowTitle(QCoreApplication.translate("Root", u"Form", None))
        self.lblFrPerson.setTitle(QCoreApplication.translate("Root", u"Personal Information", None))
        self.lblFirst.setText(QCoreApplication.translate("Root", u"*First Name:", None))
        self.lblLast.setText(QCoreApplication.translate("Root", u"*Last Name:", None))
        self.lblEmail.setText(QCoreApplication.translate("Root", u"Email:", None))
        self.lblPhone.setText(QCoreApplication.translate("Root", u"Phone:", None))
        self.btnQ.setText(QCoreApplication.translate("Root", u"Quit", None))
        self.btnR.setText(QCoreApplication.translate("Root", u"Reset", None))
        self.btnS.setText(QCoreApplication.translate("Root", u"Submit", None))
    # retranslateUi

