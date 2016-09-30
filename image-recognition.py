import os                       # for directory/path manipulation
import time                     # to track performance
import sys                      # to process command-line args
import numpy as np              # to represent data for sklearn
from PIL import Image           # to handle images
from sklearn import svm         # to form a model and predict image classification
from scipy import misc


def main():

    start_time = time.time()

    directory = os.getcwd()     #get current directory
    print (directory)
    training_dir = os.path.join(directory, os.path.relpath('Data', directory))
    print (training_dir)
    training_collection = os.listdir(training_dir)

    training_list = list()

    # populate training_list with lists from each dataset
    for training_set in training_collection:
        print (training_set)



        training_path = os.path.join(training_dir, training_set)
        print (training_path)

        image_files =  [ image_file for image_file in os.listdir(training_path) if os.path.isfile(os.path.join(training_path, image_file)) ]
        # print image_files

        set_list = list()               #initialize a list for the numpy arrays containing images
        for image_file in image_files:
            image = Image.open(os.path.join(training_path, image_file))
            arr = np.array(image)
            set_list.append(arr)

        training_list.append(set_list)

    # os.chdir(home_dir)

    data_smile = np.array(training_list[0])
    data_hat = np.array(training_list[1])
    data_hash = np.array(training_list[2])
    data_heart = np.array(training_list[3])
    data_dollar = np.array(training_list[4])




    # see sklearn svm
    clf = svm.SVC()

    data = np.array([data_smile, data_hat, data_hash, data_heart, data_dollar])
    labels = ['smile', 'hat', 'hash', 'heart', 'dollar']

    #clf.fit(clf, data, labels)


#    test_dir = os.path.join(directory, 'Test')
#    os.chdir(test_dir)
#    submitted_image = misc.imread(sys.argv[1])
    # print ("Image is a " + clf.predict(np.array(Image.open(sys.argv[1]).getdata())))
#    print (clf.predict())
    print ("End")
    print ("Time taken: " + str(time.time() - start_time) + ' s')


    sys.exit()

main()  # sys.argv[1]
