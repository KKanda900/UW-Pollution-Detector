# Regular Python Libraries
import cv2, os
import numpy as np
from PIL import Image

# Python GUI
import PySimpleGUI as sg

# Model Libraries
import tensorflow as tf

# Multi Image Classifier Library
from Multi_Classification.Multi_Image_Classification import Multi_Image_Classification as img_classifier

# Binary Image Classifier Library
from Binary_Classification.Image_Classification import Image_Classification as bin_classifier

class Application:

    classifier = None # default is None, but in the application the user chooses between binary and categorical
    model = None # default is None, but this is changed once the user selects the model

    def pick_model(self):
        models = []
        for root, dirs, files in os.walk("./Models"):
            for name in files:
                models.append(name)

        return models

    def run_application(self):
        models = self.pick_model()

        # define the window layout => video, image, classification on the bottom
        layout = [[sg.Image(filename='', key='_IMAGE_'), sg.Image(r'', key='IMAGE')], [sg.Text(
            'Classification: ', key='label', font='Courier 9', size=(50, 1))], [sg.Listbox(values=models, size=(30, 6), key='LIST'), sg.Button('Take a Picture'), sg.Button('Process Image')]]

        # create the window and show it without the plot
        window = sg.Window('Pollution Detector', layout, location=(100, 100))

        # --- Event LOOP Read and display frames, operate the GUI --- #
        # Setup the OpenCV capture device (webcam)
        cap = cv2.VideoCapture(0)
        # iterate through infinitely until the user closes the application
        while True:
            # define these values for when there are certain events that occur in the application
            event, values = window.Read(timeout=20, timeout_key='timeout')
            
            if len(window.FindElement('LIST').get()) != 0:
                self.model = tf.keras.models.load_model('./Models/'+window.FindElement('LIST').get()[0])
                print(self.model.__dict__)

            # if there is no more events the application isn't running
            if event is None:
                break

            # if the user clicks the 'Take a Picture' button clear the directory then take a picture
            if event == 'Take a Picture':
                cv2.imwrite('./App_Data/file.png', frame) # write the image to the directory
                img = cv2.imencode('.png', np.float32(Image.open("./App_Data/file.png")))[1].tobytes() # to display the image in the GUI convert it to float32
                window.FindElement('IMAGE').Update(data=img) # replaces the image and add it to the GUI according to the key

            # if the user clicks 'Process Image' button then classify the image that was just taken
            if event == 'Process Image':
                self.classifier = img_classifier(False, labels, (h_size, v_size), epoch, batch_size)

            # Read image from capture device (camera)
            ret, frame = cap.read()
            # Convert the image to PNG Bytes
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()
            # Change the Image Element to show the new image
            window.FindElement('_IMAGE_').Update(data=imgbytes)

app = Application()
app.run_application()
