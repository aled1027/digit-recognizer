#!/home/alex/.virtualenv/data-analysis/bin/python

from PIL import Image
import csv
from utils import read_data, make_image, doWorkNumpy
import operator

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from sklearn import decomposition

# SKIP 0th INDEX -- starts with 1

def func():
    print "Reading train data"
    train, target = read_data("data/train.csv")

    pca_components = [1, 2, 3, 4, 5, 10, 20, 25, 30, 50, 70, 100]
    pca_components = [1, 20, 50, 75, 100]
    pca_fits = []

py    for comp_size in pca_components:
        print "Fitting pca with %d components" % comp_size
        pca_fits.append(decomposition.PCA(n_components=comp_size).fit(train))
        # essentially does SVD
        # http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

    figure = plt.figure()
    t = np.array(target)

    choosen_numbers = []
    choosen_numbers.append(np.argwhere(t == 0)[-3])
    choosen_numbers.append(np.argwhere(t == 1)[-3])
    choosen_numbers.append(np.argwhere(t == 2)[-3])
    choosen_numbers.append(np.argwhere(t == 3)[-3])
    choosen_numbers.append(np.argwhere(t == 4)[-3])
    choosen_numbers.append(np.argwhere(t == 5)[-3])
    choosen_numbers.append(np.argwhere(t == 6)[-3])
    choosen_numbers.append(np.argwhere(t == 7)[-3])
    choosen_numbers.append(np.argwhere(t == 8)[-3])
    choosen_numbers.append(np.argwhere(t == 9)[-3])

    pca_index = 1
    for n in choosen_numbers:
        for p in pca_fits:
            transformed = p.transform(train[n])
            # print "Shape of transformed: %d" % transformed.shape
            reconstructed = p.inverse_transform(transformed)
            f = figure.add_subplot(10, len(pca_components), pca_index).imshow(np.reshape(reconstructed, (28, 28)), interpolation='nearest', cmap=cm.hot)  # cmap=cm.Greys_r)
            for xlabel_i in f.axes.get_xticklabels():
                xlabel_i.set_visible(False)
                xlabel_i.set_fontsize(0.0)
            for xlabel_i in f.axes.get_yticklabels():
                xlabel_i.set_fontsize(0.0)
                xlabel_i.set_visible(False)
            for tick in f.axes.get_xticklines():
                tick.set_visible(False)
            for tick in f.axes.get_yticklines():
                tick.set_visible(False)
            pca_index += 1
    plt.savefig("fig.svg")
    plt.savefig("fig2.png")



def go():
    #train, labels = read_data("data/train.csv", quick=True)
    #test, tmpl = read_data("data/test.csv", test=True, quick=True)

    train, labels = read_data("data/train.csv")
    test, tmpl = read_data("data/test.csv", test=True)

if __name__ == "__main__":
    print "starting..."
    #func()
    print "exiting..."
    # to get time, run like: time ./main.py

