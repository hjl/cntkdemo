# helper functions for working with convnet visualization images

from PIL import Image as PILImage
import numpy as np
import sys, os

import cv2
from matplotlib import pyplot as plt


def make_filter_weight_image(filter_weights, image_file_name, dim=11):
    imstack = np.dstack((filter_weights[0], filter_weights[1], filter_weights[2]))
    # hacky range normalization so we can see something
    immean = imstack.mean()
    #print(immean)
    imstack -= immean
    imstack = imstack * (255.0/imstack.max())
    imstack += 127.
    #print (imstack[0])
    imstack = np.clip(imstack, 0., 255.)
    imint = (imstack * (255.0 / imstack.max())).astype('uint8')
    #imint = imstack.astype('uint8')
    #print(imint[0])
    try:
        os.remove(image_file_name)
    except OSError:
        pass

    im = PILImage.fromarray(imint)
    im2 = im.resize((224,224))
    im2.save(image_file_name)

def read_conv1_filter_values(filter_json_file_name):
    f = open (filter_json_file_name)
    filters = list()
    for line in f:
        filters.append(json.loads(line))

    print(filters)
    return filters

def demo_minoru_stereo():
    cap1 = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(2)

    # reasonable setting for daylight in office is exposure = -10.0, brightness = -10.0, contrast = 15.0
    exposure = -10.0 # minoru range is 0.0 max to -10.0 min
    brightness = -10.0 # minoru range is 10.0 max to -10.0 min
    contrast = 15.0 # minoru range is 20.0 max to 0.0 min
    count = 0
    while True:
        count = count + 1
        print("count is " + repr(count))
        cap1.set(cv2.CAP_PROP_EXPOSURE, exposure)
        cap2.set(cv2.CAP_PROP_EXPOSURE, exposure)
        print("exposure is " + repr(exposure) + ", read back " + repr(cap1.get(cv2.CAP_PROP_EXPOSURE)))
    #    exposure = exposure - 1.0
        cap1.set(cv2.CAP_PROP_BRIGHTNESS, brightness)
        cap2.set(cv2.CAP_PROP_BRIGHTNESS, brightness)
        print("brightness is " + repr(brightness), ", read back " + repr(cap1.get(cv2.CAP_PROP_BRIGHTNESS)))
        #brightness = brightness - 1.0

        cap1.set(cv2.CAP_PROP_CONTRAST, contrast)
        cap2.set(cv2.CAP_PROP_CONTRAST, contrast)
        print("contrast is " + repr(contrast) + ", read back " + repr(cap1.get(cv2.CAP_PROP_CONTRAST)))
        #contrast = contrast - 1.0

        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        #img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB) 
        #img2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

        cv2.imshow('cap1', frame1)
        cv2.imshow('cap2', frame2)

        if count == 5:
            cv2.imwrite('.\\data\\minoru-left.png', frame1)
            cv2.imwrite('.\\data\\minoru-right.png', frame2)

        cv2.waitKey(100)

    cap1.release()
    cap2.release()

    return

