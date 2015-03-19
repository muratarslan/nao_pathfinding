import os
import sys
import fnmatch
import getopt
import cv2
import numpy as np

from sklearn import svm


number_of_bins = 64
positive = 'dataset/positive'
negative = 'dataset/negative'
ds = 'dataset'


# Get all 'png' images from 'negative' and 'positive' folder
def get_images():
    image_files = []
    for i in range(2):
        if i == 0:
            path = positive
        elif i == 1:
            path = negative
        for j in sorted(os.listdir(path)):
            if fnmatch.fnmatch(j, '*.png'):
                image_files.append(j)
        i += 1
    return image_files


# Returns histogram result
def get_histogram(image_files):
    image = cv2.imread(image_files)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histogram = cv2.calcHist([gray],[0],None,[number_of_bins],[0,number_of_bins])
    transp = histogram.transpose()
    return transp.astype(np.float64)


# Gets all pictures' histograms
def get_histograms():
    images = get_images()
    histogram_map = {}
    for i in images:
        im = positive +'/'+ i
        histogram_map[im] = get_histogram(im)
    for i in images:
        im = negative +'/'+ i
        histogram_map[im] = get_histogram(im)
    return histogram_map.values()


# Sets the values positive 1 negative 0 for svm values
def get_values():
    values = []
    for i in range(2):
        if i == 0:
            path = positive
            j = 0
        elif i == 1:
            path = negative
            j = 1
        for i in sorted(os.listdir(path)):
            values.append((j,))
    return values


# Splits the matrix in desired format
def split(mtx,num):
    matrix = np.array(mtx)
    matrix_splitted = np.array(np.split(matrix, num))
    return np.fliplr(matrix_splitted)
    
    
# SVM learn and classify
def train():
    pf = []
    train_data = map(lambda x: x[0], get_histograms())
    value = get_values()

    classify = svm.SVC(kernel='linear')
    classify.fit(train_data, value)


    for j in range(768):
        predict = get_histogram(ds +'/'+ str(j)+'.png')
        result = classify.predict(predict)

        if result == [1]:
            i = 1
        else:
            i = 0
        pf.append(i)
    return split(pf,32)
    

