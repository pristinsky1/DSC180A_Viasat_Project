import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Example of byte count feature extraction on the no streaming dataset:
big_byte_no_streaming = big_byte_count_feature(yes_0)
print(big_byte_no_streaming[['Dir1_ByteCount_0to300', 'Dir2_ByteCount_1200to1500']].head(5))
print("No Streaming Byte Count:")
big_byte_no_streaming[['Dir1_ByteCount_0to300', 'Dir2_ByteCount_1200to1500']].sum()

