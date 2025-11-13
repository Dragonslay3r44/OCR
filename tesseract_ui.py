# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tesseract.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_TesseractSettingsDialog(object):
    def setupUi(self, TesseractSettingsDialog):
        if not TesseractSettingsDialog.objectName():
            TesseractSettingsDialog.setObjectName(u"TesseractSettingsDialog")
        TesseractSettingsDialog.resize(452, 350)
        self.verticalLayout = QVBoxLayout(TesseractSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_language = QLabel(TesseractSettingsDialog)
        self.label_language.setObjectName(u"label_language")

        self.verticalLayout.addWidget(self.label_language)

        self.edit_language = QLineEdit(TesseractSettingsDialog)
        self.edit_language.setObjectName(u"edit_language")

        self.verticalLayout.addWidget(self.edit_language)

        self.label_psm = QLabel(TesseractSettingsDialog)
        self.label_psm.setObjectName(u"label_psm")

        self.verticalLayout.addWidget(self.label_psm)

        self.combo_psm = QComboBox(TesseractSettingsDialog)
        self.combo_psm.addItem("")
        self.combo_psm.addItem("")
        self.combo_psm.addItem("")
        self.combo_psm.addItem("")
        self.combo_psm.setObjectName(u"combo_psm")

        self.verticalLayout.addWidget(self.combo_psm)

        self.button_load_image = QPushButton(TesseractSettingsDialog)
        self.button_load_image.setObjectName(u"button_load_image")

        self.verticalLayout.addWidget(self.button_load_image)

        self.text_result = QTextEdit(TesseractSettingsDialog)
        self.text_result.setObjectName(u"text_result")
        self.text_result.setReadOnly(True)

        self.verticalLayout.addWidget(self.text_result)

        self.button_close = QPushButton(TesseractSettingsDialog)
        self.button_close.setObjectName(u"button_close")

        self.verticalLayout.addWidget(self.button_close)


        self.retranslateUi(TesseractSettingsDialog)

        QMetaObject.connectSlotsByName(TesseractSettingsDialog)
    # setupUi

    def retranslateUi(self, TesseractSettingsDialog):
        TesseractSettingsDialog.setWindowTitle(QCoreApplication.translate("TesseractSettingsDialog", u"Tesseract OCR Settings", None))
        self.label_language.setText(QCoreApplication.translate("TesseractSettingsDialog", u"\u042f\u0437\u044b\u043a:", None))
        self.edit_language.setText(QCoreApplication.translate("TesseractSettingsDialog", u"eng", None))
        self.label_psm.setText(QCoreApplication.translate("TesseractSettingsDialog", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0438 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b (PSM):", None))
        self.combo_psm.setItemText(0, QCoreApplication.translate("TesseractSettingsDialog", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u0435\u0433\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f \u0441 OSD", None))
        self.combo_psm.setItemText(1, QCoreApplication.translate("TesseractSettingsDialog", u"\u041f\u043e\u043b\u043d\u0430\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u0435\u0433\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f, \u0431\u0435\u0437 OSD", None))
        self.combo_psm.setItemText(2, QCoreApplication.translate("TesseractSettingsDialog", u"\u041f\u0440\u0435\u0434\u043f\u043e\u043b\u0430\u0433\u0430\u0435\u0442\u0441\u044f \u043e\u0434\u0438\u043d \u0431\u043b\u043e\u043a \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.combo_psm.setItemText(3, QCoreApplication.translate("TesseractSettingsDialog", u"\u0420\u0430\u0437\u0440\u0435\u0436\u0435\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442, \u0438\u0441\u043a\u0430\u0442\u044c \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0431\u043e\u043b\u044c\u0448\u0435 \u0442\u0435\u043a\u0441\u0442\u0430", None))

        self.button_load_image.setText(QCoreApplication.translate("TesseractSettingsDialog", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0438 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0442\u044c", None))
        self.button_close.setText(QCoreApplication.translate("TesseractSettingsDialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

