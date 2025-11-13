# latexocr_window.py
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import Slot
from latexocr_ui import Ui_LatexOCRSettingsDialog
from pix2tex.cli import LatexOCR
from PIL import Image
import time

class LatexOCRSettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LatexOCRSettingsDialog()
        self.ui.setupUi(self)

        # Привязка кнопок
        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_load_image.clicked.connect(self.load_and_run_ocr)

    def _measure_ocr(self, func, *args, **kwargs):
        """Замер времени OCR с обработкой исключений"""
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            return f"[Ошибка OCR: {e}]", 0.0
        elapsed = time.perf_counter() - start
        return result, elapsed

    @Slot()
    def load_and_run_ocr(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выбрать изображение",
            "",
            "Изображение (*.png *.jpg *.jpeg)"
        )
        if not file_name:
            return

        try:
            # Создаем объект LatexOCR без аргументов
            ocr = LatexOCR()
            img = Image.open(file_name)
            result, elapsed = self._measure_ocr(ocr, img)

            if not result.strip():
                result = "[Нет распознанного текста]"

            self.ui.text_result.setPlainText(result.strip())
            print(f"LaTeX OCR: {elapsed:.2f}s")

        except Exception as e:
            self.ui.text_result.setPlainText(f"[Ошибка: {e}]")
