import os
import sys
from PyQt6.QtWidgets import QApplication, QFileDialog


def select_file():
    app = QApplication(sys.argv)  # noqa: F841 (Needed for window setup)
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "Select a file",
        os.path.expanduser("~"),
        # "All Allowed Files (*.pbix *.txt *.csv *.json);;Power BI files (*.pbix);;Text files (*.txt);;CSV files (*.csv);;JSON files (*.json)",
        "Power BI model files (*.bim)",
    )
    print(file_path)


if __name__ == "__main__":
    select_file()
