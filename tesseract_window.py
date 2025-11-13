from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import Slot
from tesseract_ui import Ui_TesseractSettingsDialog
from PIL import Image
import pytesseract
import time

class TesseractSettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TesseractSettingsDialog()
        self.ui.setupUi(self)

        # Привязка кнопок
        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_load_image.clicked.connect(self.load_and_run_ocr)

        # Путь к tesseract.exe
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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

        lang = self.ui.edit_language.text()

        # Определяем PSM из ComboBox
        try:
            psm_text = self.ui.combo_psm.currentText()
            psm = int(psm_text.split(" ")[0])
        except Exception:
            psm = 3  # по умолчанию

        try:
            img = Image.open(file_name)

            # Используем legacy engine для PSM 0, иначе LSTM
            oem = 0 if psm == 0 else 3

            text, elapsed = self._measure_ocr(
                pytesseract.image_to_string,
                img,
                lang=lang,
                config=f'--psm {psm} --oem {oem}'
            )

            if not text.strip():
                text = "[Нет распознанного текста]"

            self.ui.text_result.setPlainText(text.strip())
            print(f"Tesseract OCR (PSM {psm}): {elapsed:.2f}s")

        except Exception as e:
            self.ui.text_result.setPlainText(f"[Ошибка: {e}]")
