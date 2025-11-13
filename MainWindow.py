from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, QSettings, QCoreApplication, QDir, Slot
from ui_main import Ui_Form
from paddleocr import PaddleOCR
import pytesseract
from pix2tex.cli import LatexOCR
from PIL import Image
from pathlib import Path
import cv2
import time
import os
from themes import LIGHT_THEME, DARK_THEME

# Импорт окон настроек OCR (исправлено)
from tesseract_window import TesseractSettingsWindow
from paddleocr_window import PaddleOCRSettingsWindow
from latexocr_window import LatexOCRSettingsWindow

# Чтобы избежать конфликта OpenMP
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.central_widget = QWidget()
        self.ui.setupUi(self.central_widget)
        self.setCentralWidget(self.central_widget)

        self.init_Theme()
        self.init_Ocr()
        self.init_Ui()

        self.tess_window = TesseractSettingsWindow()  # Окно Tesseract
        self.paddle_window = PaddleOCRSettingsWindow()  # Окно PaddleOCR
        self.latex_window = LatexOCRSettingsWindow()  # Окно LaTeX OCR

    def init_Theme(self):
        self.settings = QSettings()
        self.current_theme = self.settings.value("UI/theme", "light")
        self.apply_theme(self.current_theme)

    def apply_theme(self, theme: str):
        self.setStyleSheet(DARK_THEME if theme == "dark" else LIGHT_THEME)

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme(self.current_theme)
        self.settings.setValue("UI/theme", self.current_theme)

    def init_Ui(self):
        # Только чтение текстовых полей
        self.ui.text_paddle.setReadOnly(True)
        self.ui.text_tess.setReadOnly(True)
        self.ui.text_latex.setReadOnly(True)

        # Привязка кнопок
        self.ui.button_load.clicked.connect(self.load_image)
        self.ui.button_theme.clicked.connect(self.toggle_theme)

        # Привязка кнопок к окнам настроек OCR
        self.ui.button_tess_settings.clicked.connect(self.show_tesseract_window)
        self.ui.button_paddle_settings.clicked.connect(self.show_paddle_window)
        self.ui.button_latex_settings.clicked.connect(self.show_latex_window)

        # QLabel для изображения
        self.ui.image_label.setAlignment(Qt.AlignCenter)
        self.ui.image_label.setText("Изображение появится здесь")

        # Настройка окна
        app_name = QCoreApplication.applicationName()
        app_version = QCoreApplication.applicationVersion()
        self.setWindowTitle(f"{app_name} v{app_version}")
        self.resize(1000, 600)
        self.setWindowIcon(QIcon(":/icons/appicon.png"))

    def init_Ocr(self):
        self.paddle_ocr = PaddleOCR(lang='en', use_angle_cls=True)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.latex_ocr_model = LatexOCR()

    def _parse_paddle_result(self, result) -> str:
        if not result:
            return "[Нет распознанного текста]"
        lines = []
        for line in result:
            lines.append(" ".join(word_info[1][0] for word_info in line))
        return "\n".join(lines)

    def _measure_ocr(self, func, *args, **kwargs):
        """Унифицированный замер времени OCR с обработкой исключений"""
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            return f"[Ошибка OCR: {e}]", 0.0
        elapsed = time.perf_counter() - start
        return result, elapsed

    @Slot()
    def load_image(self):
        settings = QSettings()
        last_dir = settings.value("last_directory", str(Path.home() / "Pictures"))

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выбрать изображение",
            last_dir,
            "Изображение (*.png *.jpeg *.jpg)"
        )
        if not file_name:
            QMessageBox.information(self, "Отмена", "Файл не выбран.")
            return

        settings.setValue("last_directory", str(Path(file_name).parent))

        img_cv = cv2.imread(file_name)
        if img_cv is None or img_cv.size == 0:
            self.ui.text_paddle.setPlainText("[PaddleOCR: файл не загружен]")
            self.ui.text_tess.setPlainText("[Tesseract: файл не загружен]")
            self.ui.text_latex.setPlainText("[LaTeX OCR: файл не загружен]")
            self.ui.image_label.setText("Неверный файл изображения")
            return

        try:
            img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        except Exception:
            self.ui.text_paddle.setPlainText("[Ошибка формата изображения]")
            self.ui.text_tess.setPlainText("[Ошибка формата изображения]")
            self.ui.text_latex.setPlainText("[Ошибка формата изображения]")
            self.ui.image_label.setText("Ошибка формата")
            return

        # PaddleOCR
        paddle_result, paddle_time = self._measure_ocr(self.paddle_ocr.ocr, img_rgb)
        self.ui.text_paddle.setPlainText(self._parse_paddle_result(paddle_result))
        print(f"PaddleOCR: {paddle_time:.3f} sec")

        # Tesseract OCR
        pil_img = Image.fromarray(img_rgb)
        tess_text, tess_time = self._measure_ocr(pytesseract.image_to_string, pil_img, lang='eng')
        self.ui.text_tess.setPlainText(tess_text.strip())
        print(f"Tesseract: {tess_time:.3f} sec")

        # LaTeX OCR
        try:
            img_pil = Image.open(file_name)
            latex_code, latex_time = self._measure_ocr(self.latex_ocr_model, img_pil)
            self.ui.text_latex.setPlainText(latex_code.strip())
            print(f"LaTeX OCR: {latex_time:.3f} sec")
        except Exception as e:
            self.ui.text_latex.setPlainText(f"[LaTeX OCR error: {e}]")

        # Отображаем изображение
        pixmap = QPixmap(file_name)
        if pixmap.isNull():
            self.ui.image_label.setText("Не удалось отобразить изображение")
        else:
            self.ui.image_label.setPixmap(
                pixmap.scaled(
                    self.ui.image_label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

    def show_tesseract_window(self):
        self.tess_window.show()  # Показываем окно Tesseract

    def show_paddle_window(self):
        self.paddle_window.show()  # Показываем окно PaddleOCR

    def show_latex_window(self):
        self.latex_window.show()  # Показываем окно LaTeX OCR



