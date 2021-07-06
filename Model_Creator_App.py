# GUI Libraries
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QComboBox, QTextEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import sys

# Multi Image Classifier Library
from Multi_Classification.Multi_Image_Classification import Multi_Image_Classification as img_classifier

# Binary Image Classifier Library
from Binary_Classification.Image_Classification import Image_Classification as bin_classifier

class Model_Creator(QWidget):

    h_size_input = None
    v_size_input = None
    labels_input = None
    model_type_input = None

    classifier = None
    
    def __init__(self, parent=None):
        super().__init__(parent)

        widget = QWidget()

        self.h_size_input = QLineEdit()
        self.h_size_input.setValidator(QIntValidator())
        self.h_size_input.setMaxLength(3)
        self.h_size_input.setAlignment(Qt.AlignRight)
        self.h_size_input.setFont(QFont("Arial", 20))

        self.v_size_input = QLineEdit()
        self.v_size_input.setValidator(QIntValidator())
        self.v_size_input.setMaxLength(3)
        self.v_size_input.setAlignment(Qt.AlignRight)
        self.v_size_input.setFont(QFont("Arial", 20))

        self.labels_input = QLineEdit()
        self.labels_input.setAlignment(Qt.AlignRight)
        self.labels_input.setFont(QFont("Arial", 20))

        self.epoch_input = QLineEdit()
        self.epoch_input.setValidator(QIntValidator())
        self.epoch_input.setAlignment(Qt.AlignRight)
        self.epoch_input.setFont(QFont("Arial", 20))

        self.batch_size_input = QLineEdit()
        self.batch_size_input.setValidator(QIntValidator())
        self.batch_size_input.setAlignment(Qt.AlignRight)
        self.batch_size_input.setFont(QFont("Arial", 20))

        self.name_of_model_input = QLineEdit()
        self.name_of_model_input.setAlignment(Qt.AlignRight)
        self.name_of_model_input.setFont(QFont("Arial", 20))

        button = QPushButton(widget)
        button.setText("Save Model")
        button.clicked.connect(self.save_model_clicked)
        
        self.button1 = QPushButton(widget)
        self.button1.setText("Submit")
        self.button1.clicked.connect(self.submit_clicked)

        self.model_type_input = QComboBox()
        self.model_type_input.addItem("Binary")
        self.model_type_input.addItem("Categorical")

        self.textEdit = QTextEdit()

        flo = QFormLayout()
        flo.addRow(self.model_type_input)
        flo.addRow("Horizontal Image Size", self.h_size_input)
        flo.addRow("Vertical Image Size", self.v_size_input)
        flo.addRow("Enter All The Labels (w/ spaces in between)", self.labels_input)
        flo.addRow("Enter the epoch (default 50)", self.epoch_input)
        flo.addRow("Enter the batch size (default 10)", self.batch_size_input)
        flo.addRow("Enter the name of the model", self.name_of_model_input)
        flo.addRow(button, self.button1)
        flo.addRow(self.textEdit)

        self.setLayout(flo)
        self.setWindowTitle("Image Classifier Model Creator")

    def save_model_clicked(self):
        name_of_model = self.name_of_model_input.text()
        model = None
        if self.model_type_input.currentText() == "Binary":
            model = self.classifier.model
        else:
            model = self.classifier.model['model']
        self.classifier.save_model(name_of_model, model)
        self.textEdit.append('Model Saved Successfully')

    def submit_clicked(self):
        # print(self.model_type_input.currentText())
        if self.model_type_input.currentText() == 'Categorical':
            h_size = int(self.h_size_input.text())
            v_size = int(self.v_size_input.text())
            labels = (self.labels_input.text()).split(" ")
            epoch = int(self.epoch_input.text())
            batch_size = int(self.batch_size_input.text())
            self.classifier = img_classifier(True, labels, (h_size, v_size), epoch, batch_size)
            self.textEdit.append('Model Created. Press save to save the model to be used in the classifier application.')
        elif self.model_type_input.currentText() == "Binary":
            size = int(self.h_size_input.text())
            labels = (self.labels_input.text()).split(" ")
            epoch = int(self.epoch_input.text())
            self.classifier = bin_classifier(size, True, True, labels, epoch)
            self.textEdit.append('Model Created. Press save to save the model to be used in the classifier application.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Model_Creator()
    win.show()
    sys.exit(app.exec_())
