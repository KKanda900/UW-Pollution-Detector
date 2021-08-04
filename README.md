# UW-Pollution-Detector 🤿

## Description of the Software

A object detector that has the capabilities to detect any type of pollution in any body of water and has the ability to work on any piece of hardware to be flexible depending on the user's hardware restrictions. Intended for research purposes to maintain a better ecosystem and free to use for any user.

## Usage

## How to use the Model Maker

To start the model maker:
```Python
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QPushButton, QComboBox, QTextEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
from Model_Creator_App import Model_Creator
import sys

app = QApplication(sys.argv)
win = Model_Creator()
win.show()
sys.exit(app.exec_())
```

Explain more specific stuff about the model creator.

## How to use the Application

```Python
from Application import Application

app = Application()
app.run_application()
```

Explain more specific stuff about the Application

## About the Model Maker

Write description of the intentions of the model maker and why it is used or important.

With many image classifiers out for public use, there wasn't any that allowed for the user to make custom models. The main intentions of this model maker was to allow users to create custom image classifier models to use for their own use. The model maker application takes in ....

Insert link to model maker github here.

### How to Install The Model Maker

Write instructions on how to install the model maker **probably going to be some sort of exe file**

## About the Underwater Pollution Detector

Write description of the intentions of the application and why it is used or important.

### How to Install the UW Pollution Detector

Write instructions on how to install the application **probably going to be some sort of exe file**

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
