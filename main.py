import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from asn8_ui import Ui_Root


class MainWindow(QMainWindow, Ui_Root):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnS.clicked.connect(self.submit_info)
        self.btnR.clicked.connect(self.reset_fields)
        self.btnQ.clicked.connect(self.close)

    def submit_info(self):
        first_name = self.entFirst.text().strip()
        last_name = self.entLast.text().strip()
        email = self.entEmail.text().strip()
        phone = self.entPhone.text().strip()

        if first_name == "" or last_name == "":
            QMessageBox.warning(
                self,
                "Missing Required Fields",
                "First Name and Last Name are required."
            )
            return

        print("Personal Information")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")

        QMessageBox.information(
            self,
            "Submitted",
            f"First Name: {first_name}\n"
            f"Last Name: {last_name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}"
        )

    def reset_fields(self):
        self.entFirst.clear()
        self.entLast.clear()
        self.entEmail.clear()
        self.entPhone.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())