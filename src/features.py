import pandas as pd
import numpy as np

# This function takes all the counts of the 0-300bytes for the 1->2 Direction and all the counts
# of the 1200-1500bytes for the 2->1 Direction and creates new columns based off this in the dataframe
def big_byte_count_feature(dataset):        
    df = dataset.copy()
    packet_size_count1 = []
    packet_size_count2 = []
    for i in range(df.shape[0]):
        row = three_cols(df.iloc[i])
        ones = row.loc[row['packet_dir'] == 1]['packet_size']
        twos = row.loc[row['packet_dir'] == 2]['packet_size']
        one_count=0
        two_count=0
        for packet in ones:
            if (int(packet) >= 0) and (int(packet) <= 300):
                one_count += 1
        for packet in twos:
            if (int(packet) >= 1200) and (int(packet) <= 1500):
                two_count += 1
        packet_size_count1.append(one_count)
        packet_size_count2.append(two_count)
    return df.assign(Dir1_ByteCount_0to300 = packet_size_count1, Dir2_ByteCount_1200to1500 = packet_size_count2)
