import tensorflow as tf
from Multi_Classification.Multi_Image_Classification import Multi_Image_Classification as classifier

img_classifier = classifier(False, ['Garbage', 'Oil', 'Sewage'], (200,200), 50, 10)

img_classifier.model = tf.keras.models.load_model('./Models/Pollution_Model_Categorical.h5')

app_data_labels, app_data_images = img_classifier.set_data(directory_path='./App_Data')

classification = img_classifier.classify_image(image=app_data_images[0], model=img_classifier.model)