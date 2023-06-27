from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from tkinter import filedialog
import gzip
import os

if hasattr(sys, 'frozen'):
    icon_path = sys._MEIPASS + r'C:\Users\stech\OneDrive\Desktop\python_programming_internship\Python Internship Task 2\icon\applicationicon.ico'  # Specify the correct path to your icon file
else:
    icon_path = r'C:\Users\stech\OneDrive\Desktop\python_programming_internship\Python Internship Task 2\icon\applicationicon.ico'  # Specify the correct path to your icon file


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.compressBtn = QtWidgets.QPushButton(Dialog)
        self.compressBtn.setGeometry(QtCore.QRect(130, 150, 75, 23))
        self.compressBtn.setObjectName("compressBtn")
        self.decompressBtn = QtWidgets.QPushButton(Dialog)
        self.decompressBtn.setGeometry(QtCore.QRect(220, 150, 75, 23))
        self.decompressBtn.setObjectName("decompressBtn")
        self.statusText = QtWidgets.QLineEdit(Dialog)
        self.statusText.setGeometry(QtCore.QRect(110, 210, 211, 31))
        self.statusText.setObjectName("statusText")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(133, 50, 171, 71))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setAlignment(Qt.AlignCenter)
        self.statusText.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "File Compression & Decompression"))
        Dialog.setWindowIcon(QIcon(r"C:\Users\stech\OneDrive\Desktop\python_programming_internship\Python Internship Task 2\icon\applicationicon.ico"))
        self.label.setText(_translate("Dialog", "Upload File: "))
        self.compressBtn.setText(_translate("Dialog", "Compress"))
        self.decompressBtn.setText(_translate("Dialog", "Decompress"))

        self.compressBtn.clicked.connect(self.compressFiles)
        self.decompressBtn.clicked.connect(self.decompressFiles)

    def compressFiles(self):
        filenames = filedialog.askopenfilenames(filetypes=[('All Files', '*.*')])
        for fname in filenames:
            file_name = os.path.basename(fname)
            self.textEdit.append(file_name)
            self.textEdit.append("{ for compression }")

        for file_path in filenames:
            with open(file_path, 'rb') as file:
                compressed_path = file_path + ".gz"
                with gzip.open(compressed_path, 'wb') as compressed_file:
                    compressed_file.writelines(file)

        self.statusText.setText("Successfully Compressed")

    def decompressFiles(self):
        filenames = filedialog.askopenfilenames(filetypes=[('All Files', '*.*')])
        for fname in filenames:
            file_name = os.path.basename(fname)
            self.textEdit.append(file_name)
            self.textEdit.append("{ for decompression }")

        for file_path in filenames:
            with gzip.open(file_path, 'rb') as compressed_file:
                decompressed_path = os.path.splitext(file_path)[0]

                with open(decompressed_path, 'wb') as decompressed_file:
                    decompressed_file.write(compressed_file.read())

        self.statusText.setText("Successfully Decompressed")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
