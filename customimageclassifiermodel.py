# -*- coding: utf-8 -*-
"""CustomImageClassifierModel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/googlecodelabs/odml-pathways/blob/main/ImageClassificationMobile/colab/CustomImageClassifierModel.ipynb
"""

# Install Model maker
!pip install -q tflite-model-maker &> /dev/null

# Imports and check that we are using TF2.x
import numpy as np
import os

from tflite_model_maker import configs
from tflite_model_maker import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader

import tensorflow as tf
assert tf.__version__.startswith('2')
tf.get_logger().setLevel('ERROR')

data_path = tf.keras.utils.get_file(
      '/content/drive/MyDrive/FACULTADES',
      'https://drive.google.com/drive/folders/1kuTBu7LNnuZsiNxCaE3PLv7CU0U6g-DX?usp=share_link',
      untar=True)

from google.colab import drive
drive.mount('/content/drive')

data = DataLoader.from_folder(data_path)
train_data, test_data = data.split(0.9)

model = image_classifier.create(train_data)

loss, accuracy = model.evaluate(test_data)

model.export(export_dir='/mm_flowers')