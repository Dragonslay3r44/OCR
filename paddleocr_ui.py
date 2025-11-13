# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paddleOCR.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_PaddleOCRSettingsDialog(object):
    def setupUi(self, PaddleOCRSettingsDialog):
        if not PaddleOCRSettingsDialog.objectName():
            PaddleOCRSettingsDialog.setObjectName(u"PaddleOCRSettingsDialog")
        PaddleOCRSettingsDialog.resize(400, 350)
        self.verticalLayout = QVBoxLayout(PaddleOCRSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_lang = QLabel(PaddleOCRSettingsDialog)
        self.label_lang.setObjectName(u"label_lang")

        self.verticalLayout.addWidget(self.label_lang)

        self.edit_lang = QLineEdit(PaddleOCRSettingsDialog)
        self.edit_lang.setObjectName(u"edit_lang")

        self.verticalLayout.addWidget(self.edit_lang)

        self.label_angle = QLabel(PaddleOCRSettingsDialog)
        self.label_angle.setObjectName(u"label_angle")

        self.verticalLayout.addWidget(self.label_angle)

        self.check_angle = QCheckBox(PaddleOCRSettingsDialog)
        self.check_angle.setObjectName(u"check_angle")
        self.check_angle.setChecked(True)

        self.verticalLayout.addWidget(self.check_angle)

        self.button_load_image = QPushButton(PaddleOCRSettingsDialog)
        self.button_load_image.setObjectName(u"button_load_image")

        self.verticalLayout.addWidget(self.button_load_image)

        self.text_result = QTextEdit(PaddleOCRSettingsDialog)
        self.text_result.setObjectName(u"text_result")
        self.text_result.setReadOnly(True)

        self.verticalLayout.addWidget(self.text_result)

        self.button_close = QPushButton(PaddleOCRSettingsDialog)
        self.button_close.setObjectName(u"button_close")

        self.verticalLayout.addWidget(self.button_close)


        self.retranslateUi(PaddleOCRSettingsDialog)

        QMetaObject.connectSlotsByName(PaddleOCRSettingsDialog)
    # setupUi

    def retranslateUi(self, PaddleOCRSettingsDialog):
        PaddleOCRSettingsDialog.setWindowTitle(QCoreApplication.translate("PaddleOCRSettingsDialog", u"PaddleOCR Settings", None))
        self.label_lang.setText(QCoreApplication.translate("PaddleOCRSettingsDialog", u"\u042f\u0437\u044b\u043a \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u044f:", None))
        self.edit_lang.setText(QCoreApplication.translate("PaddleOCRSettingsDialog", u"en", None))
        self.label_angle.setText(QCoreApplication.translate("PaddleOCRSettingsDialog", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u0430 \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0430:", None))
        self.button_load_image.setText(QCoreApplication.translate("PaddleOCRSettingsDialog", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0438 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0442\u044c", None))
        self.button_close.setText(QCoreApplication.translate("PaddleOCRSettingsDialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

