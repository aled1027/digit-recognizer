
import csv
import numpy as np
from PIL import Image

# loading csv data into numpy array
def read_data(file_path, header=True, test=False, quick=False):
    data = []
    labels = []
    csv_reader = csv.reader(open(file_path, "r"), delimiter=",")
    index = 0
    for row in csv_reader:
        index = index + 1
        if header and index == 1:
            continue
        if not test:
            labels.append(int(row[0]))
            row = row[1:]
        data.append(np.array(np.int64(row)))

    # data::list<numpy.ndarray<numpy.int64>>
    print "data size " , len(data)
    return (data, labels)

def make_image(ndarr, path):
    # make_image(test[1], "1.jpg")
    new_image = Image.new("L", (28,28))
    new_data = new_image.load()
    for x in range(28):
        for y in range(28):
            new_data[x,y] = ndarr[x + y*28]
    new_image.save(path)

def doWorkNumpy(train, test, labels):
    k = 100
    train_mat = np.mat(train)
    output_file = open("output-numpy2.csv", "w", 0)
    idx = 1
    size = len(test)
    for test_sample in test:
        knn = np.argsort(np.sum(np.power(np.subtract(train_mat, test_sample), 2), axis=1), axis=0)[:k]
        # axis=0 => sum over cols
        # axis=1 => sum over rows
        prediction = majority_vote(knn, labels)
        output_file.write(str(prediction))
        output_file.write("\n")
        print "Done: %f" % (float(idx) / size)
        idx += 1
    output_file.close()
    output_file = open("done.txt", "w")
    output_file.write("DONE")
    output_file.close()

def majority_vote(knn, labels):
    knn = [k[0,0] for k in knn]
    # what is k[0,0]
    # extracts the (0,0) pixel?
    a = {} # a map<[0..9],int> # tracks the votes for each number
    for idx in knn:
        if labels[idx] in a.keys():
            a[labels[idx]] = a[labels[idx]] + 1
        else:
            a[labels[idx]] = 1
    return sorted(a.iteritems(), key=operator.itemgetter(1), reverse=True)[0][0]


