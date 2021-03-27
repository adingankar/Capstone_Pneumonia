#import all necessary packages
import os
#initialise the base path for the lisa dataset
BASE_PATH = "C:\\Users\MURLI\\Documents\\Spyder Projects\\Capstone\\"

#Build the path to the annotation file
ANNOT_PATH = os.path.sep.join([BASE_PATH, "stage_2_train_labels_check.csv"])

#Build the path to the output training and testing path
#along with the class label file
TRAIN_RECORD = os.path.sep.join([BASE_PATH, "records\\training1.record"])
TEST_RECORD = os.path.sep.join([BASE_PATH, "records\\testing1.record"])
CLASSES_FILE = os.path.sep.join([BASE_PATH, "records\\classes.pbtxt"])

#Initialize the test split size
TEST_SIZE = 0.25

# Initialize the class lable dictionary
CLASSES = {"Pneumonia":1}
