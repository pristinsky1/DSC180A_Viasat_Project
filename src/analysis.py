import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def no_streaming_viz(dataset):
  #Example of byte count feature extraction on the no streaming dataset:
  big_byte_no_streaming = big_byte_count_feature(dataset)
  print(big_byte_no_streaming[['Dir1_ByteCount_0to300', 'Dir2_ByteCount_1200to1500']].head(5))
  print("No Streaming Byte Count:")
  return big_byte_no_streaming[['Dir1_ByteCount_0to300', 'Dir2_ByteCount_1200to1500']].sum()

def streaming_viz(dataset):
  #Example of byte count feature extraction on the streaming dataset:
  big_byte_streaming = big_byte_count_feature(dataset)
  print(big_byte_streaming[['Dir1_ByteCount_0to300', 'Dir2_ByteCount_1200to1500']].head(5))
  print("Streaming Byte Count:")
  return big_byte_streaming[['Dir1_ByteCount_0to300', 'Dir2_ByteCount_1200to1500']].sum()
