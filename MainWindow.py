from PySide6.QtWidgets import QMainWindow, QPushButton, QTextEdit, QLabel, QFileDialog, QWidget, QMessageBox
from PySide6.QtGui import QPixmap, Qt, QIcon
from PySide6.QtCore import Slot, QDir, QSettings, QCoreApplication
import resources_rc
from ui_main import Ui_Form
from paddleocr import PaddleOCR
import cv2
import pytesseract
from pathlib import Path
from PIL import Image
import time
import sys

from themes import LIGHT_THEME, DARK_THEME # Импорт тем

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_Ui()
        self.init_OCR()

        self.settings = QSettings() # Менеджер настроек

        self.current_theme = self.settings.value("UI/theme", "light")  # По умолчанию
        self.apply_theme(self.current_theme)

    def init_Ui(self):
        # Настройка свойств главного окна
        app_name = QCoreApplication.applicationName()
        app_version = QCoreApplication.applicationVersion()
        self.setWindowTitle(f"{app_name} v{app_version}")

        self.resize(1000, 600)
        self.setWindowIcon(QIcon(":/icons/appicon.png")) # Иконка

        # Создаём центральный виджет и настраиваем UI через сгенерированный класс
        self.ui = Ui_Form()
        self.central_widget = QWidget()
        self.ui.setupUi(self.central_widget)
        self.setCentralWidget(self.central_widget)

         # Получаем виджеты (предполагаем, что они есть)
        self.button_load = self.ui.button_load
        self.button_theme = self.ui.button_theme
        self.image_label = self.ui.image_label
        self.text_paddle = self.ui.text_paddle # Paddle
        self.text_tess = self.ui.text_tess # Tesseract

        # Делаем текстовые поля только для чтения
        self.text_paddle.setReadOnly(True)
        self.text_tess.setReadOnly(True)

        # Привязываем кнопку
        self.button_load.clicked.connect(self.load_image)
        self.button_theme.clicked.connect(self.toggle_theme)

        # Настройка QLabel для изображения
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setText("Изображение появится здесь")

    def init_OCR(self):
        # Инициализация PaddleOCR и Tesseract
        self.ocr = PaddleOCR(lang='en', use_angle_cls=True)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def apply_theme(self, theme: str):
        self.setStyleSheet(DARK_THEME if theme == "dark" else LIGHT_THEME)
        # ПОСМОТРЕТЬ (DARK_THEME, LIGHT_THEME)[theme == "dark"]

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme(self.current_theme)
        self.settings.setValue("UI/theme", self.current_theme) # Сохраняем тему

    @Slot()
    def load_image(self):
        # Объект настроек (использует OrganizationName и ApplicationName)
        settings = QSettings()

        # Последняя используемая папка или домашняя
        last_dir = settings.value("last_directory", QDir.homePath())

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выбрать изображение",
            last_dir,
            "Изображение (*.png *.jpeg *.jpg)"
        )
        if not file_name:
            QMessageBox.information(self, "Отмена", "Файл не выбран.")
            return

        # Сохраняем папку файла как последнюю
        current_dir = str(Path(file_name).parent)
        settings.setValue("last_directory", current_dir)

        # Загружаем изображение через OpenCV
        img_cv = cv2.imread(file_name)
        if img_cv is None or img_cv.size == 0:
            self.text_paddle.setPlainText("[PaddleOCR: не смог отработать - файл не загружен]")
            self.text_tess.setPlainText("[Tesseract: не смог отработать - файл не загружен]")
            self.image_label.setText("Неверный файл изображения")
            return

        try:
            img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        except Exception:
            self.text_paddle.setPlainText("[Ошибка: неизвестный формат изображения]")
            self.text_tess.setPlainText("[Ошибка: неизвестный формат изображения]")
            self.image_label.setText("Ошибка формата")
            return

        # PaddleOCR
        # Начало измерения времени
        start_paddle = time.perf_counter()
        result = self.ocr.ocr(img_rgb)
        # Конец замера времени
        paddle_time = time.perf_counter() - start_paddle

        paddle_text = ""
        if result and result[0]:
            for line in result:
                for word_info in line:
                    paddle_text += word_info[1][0] + " "
                paddle_text += "\n"
        self.text_paddle.setPlainText(paddle_text.strip())
        # Вывод времени в консоль
        print(f"PaddleOCR: {paddle_time:.3f} sec")
        sys.stdout.flush()

        # Tesseract OCR
        pil_img = Image.fromarray(img_rgb)
        # Начало замера времени
        start_tess = time.perf_counter()
        try:
            tess_text = pytesseract.image_to_string(pil_img, lang='eng')
        except Exception as e:
            tess_text = f"[Tesseract error: {e}]"
        # Конец замера времени
        tess_time = time.perf_counter() - start_tess

        self.text_tess.setPlainText(tess_text.strip())
        # Вывод времени в консоль
        print(f"Tesseract: {tess_time:.3f} sec")
        sys.stdout.flush()

        # Отображаем изображение
        pixmap = QPixmap(file_name)
        if pixmap.isNull():
            self.image_label.setText("Не удалось отобразить изображение") # Обработка ошибок
        else:
            self.image_label.setPixmap(
                pixmap.scaled(
                    self.image_label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )
