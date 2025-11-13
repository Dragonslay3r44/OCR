# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'latexocr.ui'
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
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_LatexOCRSettingsDialog(object):
    def setupUi(self, LatexOCRSettingsDialog):
        if not LatexOCRSettingsDialog.objectName():
            LatexOCRSettingsDialog.setObjectName(u"LatexOCRSettingsDialog")
        LatexOCRSettingsDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(LatexOCRSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_model = QLabel(LatexOCRSettingsDialog)
        self.label_model.setObjectName(u"label_model")

        self.verticalLayout.addWidget(self.label_model)

        self.combo_model = QComboBox(LatexOCRSettingsDialog)
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.setObjectName(u"combo_model")

        self.verticalLayout.addWidget(self.combo_model)

        self.button_load_image = QPushButton(LatexOCRSettingsDialog)
        self.button_load_image.setObjectName(u"button_load_image")

        self.verticalLayout.addWidget(self.button_load_image)

        self.text_result = QTextEdit(LatexOCRSettingsDialog)
        self.text_result.setObjectName(u"text_result")
        self.text_result.setReadOnly(True)

        self.verticalLayout.addWidget(self.text_result)

        self.button_close = QPushButton(LatexOCRSettingsDialog)
        self.button_close.setObjectName(u"button_close")

        self.verticalLayout.addWidget(self.button_close)


        self.retranslateUi(LatexOCRSettingsDialog)

        QMetaObject.connectSlotsByName(LatexOCRSettingsDialog)
    # setupUi

    def retranslateUi(self, LatexOCRSettingsDialog):
        LatexOCRSettingsDialog.setWindowTitle(QCoreApplication.translate("LatexOCRSettingsDialog", u"LaTeX OCR Settings", None))
        self.label_model.setText(QCoreApplication.translate("LatexOCRSettingsDialog", u"\u041c\u043e\u0434\u0435\u043b\u044c Pix2Tex:", None))
        self.combo_model.setItemText(0, QCoreApplication.translate("LatexOCRSettingsDialog", u"default", None))
        self.combo_model.setItemText(1, QCoreApplication.translate("LatexOCRSettingsDialog", u"small", None))
        self.combo_model.setItemText(2, QCoreApplication.translate("LatexOCRSettingsDialog", u"medium", None))

        self.button_load_image.setText(QCoreApplication.translate("LatexOCRSettingsDialog", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0438 \u0440\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0442\u044c", None))
        self.button_close.setText(QCoreApplication.translate("LatexOCRSettingsDialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

