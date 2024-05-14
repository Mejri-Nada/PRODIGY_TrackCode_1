import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt

class CaesarCipherGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Caesar Cipher')
        self.setFixedSize(400, 300)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove window frame

        # Widgets
        self.mode_label = QLabel('Mode:')
        self.mode_encrypt_btn = QPushButton('Encrypt')
        self.mode_decrypt_btn = QPushButton('Decrypt')

        self.message_label = QLabel('Message:')
        self.message_textedit = QTextEdit()

        self.shift_label = QLabel('Shift value:')
        self.shift_lineedit = QLineEdit()

        self.result_label = QLabel('Result:')
        self.result_textedit = QTextEdit()

        # Layout
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()

        hbox1.addWidget(self.mode_label)
        hbox1.addWidget(self.mode_encrypt_btn)
        hbox1.addWidget(self.mode_decrypt_btn)

        hbox2.addWidget(self.message_label)
        hbox2.addWidget(self.message_textedit)

        hbox3.addWidget(self.shift_label)
        hbox3.addWidget(self.shift_lineedit)

        hbox4.addWidget(self.result_label)
        hbox4.addWidget(self.result_textedit)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)

        # Connect signals
        self.mode_encrypt_btn.clicked.connect(lambda: self.cipher_operation('encrypt'))
        self.mode_decrypt_btn.clicked.connect(lambda: self.cipher_operation('decrypt'))

    def cipher_operation(self, mode):
        message = self.message_textedit.toPlainText()
        shift = self.shift_lineedit.text()

        if not shift.isdigit():
            QMessageBox.warning(self, 'Warning', 'Shift value must be an integer.')
            return

        shift = int(shift)

        result = self.caesar_cipher(message, shift, mode)
        self.result_textedit.setPlainText(result)

    def caesar_cipher(self, text, shift, mode):
        result = ""
        for char in text:
            if char.isalpha():
                if mode == 'encrypt':
                    shifted = ord(char) + shift
                elif mode == 'decrypt':
                    shifted = ord(char) - shift

                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26

                result += chr(shifted)
            else:
                result += char
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaesarCipherGUI()
    window.show()
    sys.exit(app.exec_())
