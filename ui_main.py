# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 600)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_label = QLabel(Form)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMinimumSize(QSize(400, 0))
        self.image_label.setFrameShape(QFrame.Box)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.image_label)

        self.ocr_layout = QVBoxLayout()
        self.ocr_layout.setObjectName(u"ocr_layout")
        self.label_paddle = QLabel(Form)
        self.label_paddle.setObjectName(u"label_paddle")

        self.ocr_layout.addWidget(self.label_paddle)

        self.text_paddle = QTextEdit(Form)
        self.text_paddle.setObjectName(u"text_paddle")
        self.text_paddle.setReadOnly(True)

        self.ocr_layout.addWidget(self.text_paddle)

        self.label_tess = QLabel(Form)
        self.label_tess.setObjectName(u"label_tess")

        self.ocr_layout.addWidget(self.label_tess)

        self.text_tess = QTextEdit(Form)
        self.text_tess.setObjectName(u"text_tess")
        self.text_tess.setReadOnly(True)

        self.ocr_layout.addWidget(self.text_tess)


        self.horizontalLayout.addLayout(self.ocr_layout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.button_load = QPushButton(Form)
        self.button_load.setObjectName(u"button_load")

        self.verticalLayout.addWidget(self.button_load)

        self.button_theme = QPushButton(Form)
        self.button_theme.setObjectName(u"button_theme")

        self.verticalLayout.addWidget(self.button_theme)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"OCR Comparison", None))
        self.image_label.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u0437\u0434\u0435\u0441\u044c", None))
        self.label_paddle.setText(QCoreApplication.translate("Form", u"PaddleOCR:", None))
        self.label_tess.setText(QCoreApplication.translate("Form", u"Tesseract OCR:", None))
        self.button_load.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.button_theme.setText(QCoreApplication.translate("Form", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0435\u043c\u0443", None))
    # retranslateUi

