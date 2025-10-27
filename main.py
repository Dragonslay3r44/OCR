# main.py
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCoreApplication
from MainWindow import MainWindow

if __name__ == "__main__":
    # Метаданные
    QCoreApplication.setOrganizationName("Drawi Labs")
    QCoreApplication.setOrganizationDomain("Drawi.com")
    QCoreApplication.setApplicationName("OCR App")
    QCoreApplication.setApplicationVersion("1.0")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
