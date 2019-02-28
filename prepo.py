# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/dc_tts
'''

from __future__ import print_function

from utils import load_spectrograms
import os
from data_load import load_data
import numpy as np
import tqdm

# Load data
fpaths, _, _ = load_data() # list

for fpath in tqdm.tqdm(fpaths):
    fname, mel, mag = load_spectrograms(fpath)
    if not os.path.exists("/output/mels"): os.mkdir("/output/mels")
    if not os.path.exists("/output/mags"): os.mkdir("/output/mags")

    np.save("/output/mels/{}".format(fname.replace("wav", "npy")), mel)
    np.save("/output/mags/{}".format(fname.replace("wav", "npy")), mag)