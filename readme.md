### TODO ###
- https://github.com/dzhibas/kaggle-digit-recognizer/blob/master/py-knn/experiment1-custom-knn-brute-force.py
- https://www.kaggle.com/c/digit-recognizer/data

- figure out and prototype a better method
- employ the philsophy and tools of Nate Silver.
- Keep it simple.

### NOTES ### 
- train::list<numpy.ndarray<numpy.int64>>
- train and test contain gray-scale images of hand-drawn digits, zero through nine.
- each image is 28 pixels by 28 pixels --> total of 784 pixels
- each pixel is [0,255] (gray-scale value)
- label tells us what the image is.
- for example, the image train[3] should be the number labels[3]

- https://www.kaggle.com/c/digit-recognizer/forums/t/9538/beginner-s-results-data-exploration-benchmarks-pre-processing

- things to consider:
    - rotated images
    - gT

- some ideas:
    - dilating (opencv)
    - eroding  (opencv)
    - average image of each number (see link above)
    - then compare to those
    - convert to bits and use bit operations?

    - if 7 or 1, move long segments to be complete horizontal or vertical
        - 7s with no cross-line are read as 1s



- train size: 42000
- test size: 28000

- lables[:10] = [1, 0, 1, 4, 0, 0, 7, 3, 5, 3]


- first 5 images:
- img[1]:2
- img[2]:0
- img[3]:9
- img[4]:0
- img[5]:3

- knn gives with k=20
- img[1]:2
- img[2]:0
- img[3]:9
- img[4]:9 --- MISS
- img[5]:3

- knn gives with k=100
- img[1]:2
- img[2]:0
- img[3]:9
- img[4]:7 --- MISS
- img[5]:3
