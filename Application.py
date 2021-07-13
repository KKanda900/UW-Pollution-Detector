# Regular Python Libraries
import cv2, os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
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

# Note: This only works on categorical not binary (still have to update that portion)

class Application:

    classifier = None # default is None, but in the application the user chooses between binary and categorical
    model = None # default is None, but this is changed once the user selects the model

    # finds all the models and labels in the model directory
    def pick_model(self):
        models = [] # stores all the models and labels in models list
        # iterate the models directory
        for root, dirs, files in os.walk("./Models"):
            # iterate all the files in the directory
            for name in files:
                models.append(name) # append the file to show afterward

        return models # return the models at the end

    # main logic behind the application
    def run_application(self):
        models = self.pick_model() # get the list of all models and lists

        # define the window layout => video, image, classification on the bottom
        layout = [[sg.Image(filename='', key='_IMAGE_'), sg.Image(r'', key='IMAGE')], [sg.Text('Classification: ', key='label', font='Courier 9', size=(50, 1))], [sg.Listbox(values=models, size=(30, 6), key='LIST'), sg.Button('Take a Picture'), sg.Button('Process Image')]]

        # create the window and show it without the plot
        window = sg.Window('Pollution Detector', layout, location=(100, 100))

        # --- Event LOOP Read and display frames, operate the GUI --- #
        # Setup the OpenCV capture device (webcam)
        cap = cv2.VideoCapture(0)
        # iterate through infinitely until the user closes the application
        var_stop = 0 # variable to stop when model is chosen
        while True:
            # define these values for when there are certain events that occur in the application
            event, values = window.Read(timeout=20, timeout_key='timeout')
            
            # if there is something clicked and nothing was picked before, get the name of the model
            if len(window.FindElement('LIST').get()) != 0 and var_stop != 1:
                self.model = tf.keras.models.load_model('./Models/'+window.FindElement('LIST').get()[0]) # store the model in class' model
                var_stop += 1 # increment once to stop going into this conditional statement

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
                # first get the labels used previously
                labels_path = window.FindElement('LIST').get()[0] # get the labels path from the combobox
                f = open("./Models/{}".format(labels_path)) # open the file
                labels = f.read().splitlines() # get the list of labels from the file
                f.close() # close the file after your done to save memory
                self.classifier = img_classifier(False, labels, (200, 200), 10, 10) # create the categorical classifier object
                self.classifier.model = self.model # store the model into the object
                app_data_labels, app_data_images = self.classifier.set_data(directory_path='./App_Data') # get the labels and images from the app_data which should be empty afterwards
                classification = self.classifier.classify_image(image=app_data_images, model=self.classifier.model) # get the classification
                window.FindElement('label').Update(value="Classification: {}".format(classification)) # write the label for the user to see

            # Read image from capture device (camera)
            ret, frame = cap.read()
            # Convert the image to PNG Bytes
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()
            # Change the Image Element to show the new image
            window.FindElement('_IMAGE_').Update(data=imgbytes)

app = Application()
app.run_application()
