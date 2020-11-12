import pandas as pd
import numpy as np
import pylab as pl

def binarymean_packetsizes(modify_data(raw_data)):
    return (modified_data(raw_data)["packet_sizes"] > 500).replace({True: 1, False: 0})
  
  
  def binarymin_packetsizes(modify_data(raw_data)):
    return (modify_data(raw_data)["packet_sizes"].min() <= 32)


