#pip install tensorflow tensorflow-datasets keras matplotlib pathlib
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import collections
import pathlib

import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization

import tensorflow_datasets as tfds

loaded = tf.saved_model.load('bin.tf')
print(loaded.serve(tf.constant(['How do you sort a list?'])).numpy())