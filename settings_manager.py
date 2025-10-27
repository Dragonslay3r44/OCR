from PySide6.QtCore import QSettings, QDir

class SettingsManager:
    # Простой менеджер QSettings с группами
    def __init__(self):
        self.settings = QSettings()

    def load(self):
        # Возвращает словарь с настройками
        theme = self.settings.value("UI/theme", "light")
        last_dir = self.settings.value("Paths/last_directory", QDir.homePath())
        return {"theme": theme, "last_dir": last_dir}

    def save_theme(self, theme):
        self.settings.setValue("UI/theme", theme)

    def save_last_dir(self, path):
        self.settings.setValue("Paths/last_directory", path)
