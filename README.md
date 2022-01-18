# UW-Pollution-Detector 🤿

## Description of the Software

A object detector that has the capabilities to detect any type of pollution in any body of water and has the ability to work on any piece of hardware to be flexible depending on the user's hardware restrictions. Intended for research purposes to maintain a better ecosystem and free to use for any user.

## Usage

### How to use the Model Maker

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

### How to use the Application

```Python
from Application import Application

app = Application()
app.run_application()
```

Once you have launched the application, on the bottom left you are given the models and the labels that can be used. First click on the .h5 model to be used in the session of the application. Afterwards click on the .txt file with the labels for that model. After that is completed **take a picture** of the object needed to be classified. Once a photo is taken it will appear to the right of the camera. Which you can classify by pressing the **process image** button.

## About the Model Maker

With many model makers out for public use, there wasn't any that allowed for the user to make custom models easily. The main intentions of this model maker was to allow users to create custom image classifier models to use for their own use. With not many options for custom image classifiers I though the model maker would be a great idea to have for people that want their own custom models. The model maker application gives the users all the necessary inputs to create the model which once they are done entering those inputs can watch in the terminal to see the progress of creating the model. If the model is to their standards they can save the model or go back into it and add more photos, change inputs, etc.

[Go to the Repository](https://github.com/KKanda900/Model-Maker)

## About the Underwater Pollution Detector

The Underwater Pollution Detector was made for a research project I was working on in Rutgers University that involved helping in cleaning up the water to make for a safer and better environment. The primary intentions of the software was to be deployed along side an underwater robot equipped with a raspberry pi to monitor the water then if there pollution objects discovered the robot would take a picture of it, classify what the pollution is and send it to the right people to get more hands on to cleaning up that portion of the water. Given a model trained on all types of pollution in the water it would classify it based on that and via IoT it would transmit that information to a clean up crew that can recieve that information and do what they need to do. 

## How to Install U.W. Pollution Detector, the Model Maker and the Python libraries

***Note these instructions are only for Windows 10 users for now, updated instructions will be posted once completed.***

In either cmd, powershell or Windows Terminal, type in:

```shell, sh, zsh, bash 
python Setup.py
```

Once you execute the python script, the script will prompt you with installing all the necessary libraries to run the applications manually or to install the Application and Model Creator Application. Once you have setup what you need to setup, simply type in **quit** to quit the application.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
