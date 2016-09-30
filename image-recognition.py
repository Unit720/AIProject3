import os                       # for directory/path manipulation
import time                     # to track performance
import sys                      # to process command-line args
import numpy as np              # to represent data for sklearn
from PIL import Image           # to handle images
from sklearn import svm         # to form a model and predict image classification
from scipy import misc


def main():

#    start_time = time.time()

#    home_dir = os.getcwd()

    # train - use directories as labeled items
#    training_list = list()

    # build training_dir to direct to Data in directory above .py
#    directory = os.path.split(home_dir)[0]
#    training_dir = os.path.join(directory, 'Data')

    # populate training_list with lists from each dataset
#    for training_set in os.listdir(training_dir):
 #       set_list = list()
#        os.chdir(training_dir)
 #       training_files = os.listdir(training_set)
        # print training_files

#        os.chdir(training_set)
#        for image_file in training_files:
            #image = Image.open(image_file)
            #arr = np.array(image)
            #set_list.append(arr)
#            set_list.append(misc.imread(image_file))

#        training_list.append(set_list)

    # os.chdir(home_dir)

##    data_smile = np.array(training_list[0])
#    data_hat = np.array(training_list[1])
#    data_hash = np.array(training_list[2])
#    data_heart = np.array(training_list[3])
#    data_dollar = np.array(training_list[4])

    #data = np.array(training_list, dtype=np.uint8)
#    data = np.array([data_smile, data_hat, data_hash, data_heart, data_dollar])
    # see sklearn svm
#    clf = svm.SVC()

#    clf.fit(data, ['smile', 'hat', 'hash', 'heart', 'dollar'])

#    test_dir = os.path.join(directory, 'Test')
#    os.chdir(test_dir)
#    submitted_image = misc.imread(sys.argv[1])
    # print ("Image is a " + clf.predict(np.array(Image.open(sys.argv[1]).getdata())))
#    print (clf.predict())
#    print ("Time taken: " + str(time.time() - start_time) + ' s')
    # sys.exit()
    print ("End")

main()  # sys.argv[1]
