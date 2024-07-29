import sys
import os
import threading
import shutil
import time
from PyQt5 import QtWidgets, QtCore


class CopyFileApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Copy Application')
        self.setGeometry(100, 100, 400, 200)

        layout = QtWidgets.QVBoxLayout()

        self.source_button = QtWidgets.QPushButton('Select Source File', self)
        self.source_button.clicked.connect(self.select_source)
        layout.addWidget(self.source_button)

        self.source_text = QtWidgets.QLineEdit(self)
        self.source_text.setPlaceholderText('Source File Path')
        self.source_text.textChanged.connect(self.update_line_edit)
        layout.addWidget(self.source_text)

        self.destination_button = QtWidgets.QPushButton('Select Destination Path', self)
        self.destination_button.clicked.connect(self.select_destination)
        layout.addWidget(self.destination_button)

        self.destination_text = QtWidgets.QLineEdit(self)
        self.destination_text.setPlaceholderText('Destination Directory Path')
        layout.addWidget(self.destination_text)

        self.copy_button = QtWidgets.QPushButton('Copy', self)
        self.copy_button.setEnabled(False)
        self.copy_button.clicked.connect(self.start_copy_thread)
        layout.addWidget(self.copy_button)

        self.progress_bar = QtWidgets.QProgressBar(self)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def select_source(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Source File", "", "All Files (*)", options=options)
        if file_name:
            self.source_text.setText(file_name)
            self.progress_bar.setValue(0)
            self.enable_copy_button()

    def select_destination(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Destination Directory", options=options)
        if directory:
            self.destination_text.setText(directory)
            self.enable_copy_button()

    def enable_copy_button(self):
        if self.source_text.text() and self.destination_text.text():
            self.copy_button.setEnabled(True)

    def update_line_edit(self):
        current_text = self.source_text.text()
        q_line_edit_color_green = "background-color: rgb(85, 170, 0);"
        q_line_edit_color_red = "QLineEdit {background-color: rgb(255, 0, 0);}"
        q_line_edit_color_white = "QLineEdit {background-color: rgb(255, 255, 255);}"

        if len(current_text) == 0:
            self.source_text.setStyleSheet(q_line_edit_color_white)
        else:
            if os.path.exists(current_text):
                self.source_text.setStyleSheet(q_line_edit_color_green)
            else:
                self.source_text.setStyleSheet(q_line_edit_color_red)

    def start_copy_thread(self):
        self.source_path = self.source_text.text()
        self.destination_path = os.path.join(self.destination_text.text(), os.path.basename(self.source_path))
        self.total_size = os.path.getsize(self.source_path)
        if os.path.exists(self.destination_path):
            os.remove(self.destination_path)
            time.sleep(2)
        self.progress_bar.setValue(0)
        self.copy_thread = threading.Thread(target=self.copy_file)
        self.copy_thread.start()
        self.update_progress()

    def copy_file(self):
        if not os.path.exists(self.source_path):
            raise IOError("File path not found: %s" % self.source_path)
        shutil.copy2(self.source_path, self.destination_path)
        self.copy_button.setEnabled(False)

    def update_progress(self):
        while not os.path.exists(self.destination_path):
            time.sleep(2)
        destination_size = os.path.getsize(self.destination_path)
        while self.total_size != destination_size:
            destination_size = os.path.getsize(self.destination_path)
            progress = int((destination_size / self.total_size) * 100)
            self.progress_bar.setValue(progress)
            time.sleep(0.1)
        self.progress_bar.setValue(100)


def main():
    app = QtWidgets.QApplication(sys.argv)
    copy_file_app = CopyFileApp()
    copy_file_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
