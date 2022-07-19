## This code is for processing the video data
# 
# Data: The video-fMRI dataset are available online: 
# https://engineering.purdue.edu/libi/lab/Resource.html.
# 
# Environment requirement:  
# This code was developed under Red Hat Enterprise Linux environment.

# Reference: 
# Wen H, Shi J, Zhang Y, Lu KH, Cao J, and Liu Z. (2017) Neural Encoding
# and Decoding with Deep Learning for Dynamic Natural Vision. Cerebral
# Cortex, In press.
#
# Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). 
# Imagenet classification with deep convolutional neural networks.
# In Advances in neural information processing systems (pp. 1097-1105).

## History
# v1.0 (original version) --2017/09/13

## Extract the movie frames from video files
# Though the image size in Krizhevsky et al. 2012 is 224*224, the input to 
# the AlexNet Caffe model is images with resolution 227*227.
# Note that the framerate of the video is 30 frames/second, so the
# data size of frames will be very big. You can reduce the frame rate if
# storage space is of concern.

# compiled (from matlab to python) by bcha
# eddited by shhong

import os

imgsize = '227'

videofolder = '/local_raid1/03_user/sunghyoung/01_project/03_Encoding_decoding/01_NeuralEncodingDecoding/stimuli/video_fmri_dataset/stimuli'
framefolder = '/local_raid1/03_user/sunghyoung/01_project/03_Encoding_decoding/01_NeuralEncodingDecoding/stimuli/video_fmri_dataset/stimuli/frames/'

# training videos
for seg in range(18):
    videoname = f'seg{str(seg+1)}'
    impath = f'{framefolder}{videoname}/'
    os.makedirs(impath)

    #ffmpeg -i "/path/to/stimuli/seg1.mp4" -vf scale=227:227 "/path/to/stimuli/frames/seg1/im-#d.jpg"
    os.system(f'ffmpeg -i {videofolder}{videoname}.mp4 -vf scale={imgsize}:{imgsize}"{impath}im-%d.jpg"')
    
for test in range(5):
    videoname = f'test{str(test+1)}'
    impath = f'{framefolder}{videoname}/'
    os.makedirs(impath)

    #ffmpeg -i "/path/to/stimuli/test1.mp4" -vf scale=227:227 "/path/to/stimuli/frames/test1/im-#d.jpg"
    os.system(f'ffmpeg -i {videofolder}{videoname}.mp4 -vf scale={imgsize}:{imgsize} "{impath}im-%d.jpg"')

# Use the python code 'AlexNet_feature_extraction.py' to extract the hierachical feature maps from the video frames.
