# paddleocr_window.py
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import Slot
from paddleocr_ui import Ui_PaddleOCRSettingsDialog
from paddleocr import PaddleOCR
import cv2
import time

class PaddleOCRSettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PaddleOCRSettingsDialog()
        self.ui.setupUi(self)

        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_load_image.clicked.connect(self.load_and_run_ocr)

    def _measure_ocr(self, func, *args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            return f"[Ошибка OCR: {e}]", 0.0
        elapsed = time.perf_counter() - start
        return result, elapsed

    @Slot()
    def load_and_run_ocr(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выбрать изображение", "", "Изображение (*.png *.jpg *.jpeg)")
        if not file_name:
            return

        lang = self.ui.edit_lang.text()
        use_angle = self.ui.check_angle.isChecked()
        try:
            ocr = PaddleOCR(lang=lang, use_angle_cls=use_angle)
            img_cv = cv2.imread(file_name)
            img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
            result, _ = self._measure_ocr(ocr.ocr, img_rgb)
            text_lines = []
            for line in result:
                text_lines.append(" ".join(word_info[1][0] for word_info in line))
            self.ui.text_result.setPlainText("\n".join(text_lines))
        except Exception as e:
            self.ui.text_result.setPlainText(f"[Ошибка: {e}]")
