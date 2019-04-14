import numpy as np
import pandas as pd
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
file_path=tf.constant('/home/yash/hk/unifiedDLModel/unifieddataset.csv')

# df=pd.read_csv(file_path)
# print(df.columns)

# training_dataset = (
#     tf.data.Dataset.from_tensor_slices(
#         (
#             tf.cast(df['line'].values, tf.string),
#             tf.cast(df['category'].values, tf.string)
#         )
#     )
# )

# for features_tensor, target_tensor in training_dataset:
#     print(features_tensor,target_tensor)


dataset=tf.data.experimental.CsvDataset(
    file_path,
    record_defaults=['tf.float64','tf.string','tf.string'],
    # field_delim=",",
    na_value='',
    header=True)
for element in dataset:
  print(element)
  break
