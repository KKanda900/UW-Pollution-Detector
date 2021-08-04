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

Once you have launched the model maker application, the application lists some inputs needed in order to create the model:

1. The type of model (binary or categorical)
2. The horizontal size for when the application does image resizing
3. The vertical size for when the application does image resizing
4. The labels for the model
5. The epochs for when you train the model
6. The batch size for when you train the model

Once you have inserted all the necessary inputs, you have to create the model first. Then if the training went well and you have accurate results in the training the user is given the option to save the model to use in their own application.

## How to use the Application

```Python
from Application import Application

app = Application()
app.run_application()
```

Once you have launched the application, on the bottom left you are given the models and the labels that can be used. First click on the .h5 model to be used in the session of the application. Afterwards click on the .txt file with the labels for that model. After that is completed **take a picture** of the object needed to be classified. Once a photo is taken it will appear to the right of the camera. Which you can classify by pressing the **process image** button.

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
