import pandas as pd
import numpy as np
import pylab as pl

def binarymean_packetsizes(modify_data(raw_data), mean_num):
    return (modified_data(raw_data)["packet_sizes"] > mean_num).replace({True: 1, False: 0})
  
  
  def binarymin_packetsizes(modify_data(raw_data), min_num):
    return (modify_data(raw_data)["packet_sizes"].min() <= min_num)


