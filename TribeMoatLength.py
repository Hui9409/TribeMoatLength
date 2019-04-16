# coding=utf-8
# !/usr/bin/env python
# @Project   :    TribeMoatLength
# @File name :    TribeMoatLength.py 
# @Author    :    AHUI
# @Contact   :    omegazhanghui@gmail.com
# @Date      :    2019-04-15 19:13
# @SITE      :    https://github.com/Hui9409


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from skimage import measure


def chooseTribe_computeLen(arr, coordinates):
    # step 1: Labeling different tribes
    labels = measure.label(arr, background=0)
    
    plt.figure()
    plt.subplot(121)
    plt.imshow(arr)
    plt.subplot(122)
    plt.imshow(labels)
    plt.show()
    
    # step 2: Pick the tribe that the given grid belongs to
    x, y = coordinates
    n = len(np.where(labels==labels[x, y])[0])
    labels[np.where(labels!=labels[x, y])] = 0
    
    # step 3: Get the number of adjacent sides (using convolve2d)
    kernel1 = np.array([[1, 1]])
    kernel2 = np.array([[1], [1]])
    filtered1 = signal.convolve2d(in1=arr, in2=kernel1, mode='same', boundary='fill', fillvalue=0)
    filtered2 = signal.convolve2d(in1=arr, in2=kernel2, mode='same', boundary='fill', fillvalue=0)
    
    filtered1[np.where(filtered1!=2)] = 0
    filtered2[np.where(filtered2 != 2)] = 0

    h_shared_sides = sum(sum(labels * filtered1)) # (the number of horizontally shared sides) * 2
    v_shared_sides = sum(sum(labels * filtered2)) # (the number of vertically shared sides) * 2
    sharedSides = (h_shared_sides + v_shared_sides)
    
    return n * 4 - sharedSides
    

if __name__ == '__main__':
    file = 'sample2.txt'
    with open(file, 'r') as f:
        # s2 = f.read()
        sample = f.readlines()
        coordinates = [int(s) - 1 for s in sample[0].split()[-2:]]
        arr  = [list(map(int, line.replace(".", '0').replace('#', "1").split())) for line in sample[1:]]
        arr = np.array(arr)
        
    res = chooseTribe_computeLen(arr, coordinates)
    print('Sample' + file.split(".")[0][-1])
    print("The length of the tribe's moat is:%d"%res)
    