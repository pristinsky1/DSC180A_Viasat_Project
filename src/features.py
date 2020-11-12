import pandas as pd
import numpy as np

# This function returns a dataframe with the packets times, sizes, and directions for a single row of data.
# This will be used within our other functions to help create the features.
def three_cols(row):
    time = list(map(int, row['packet_times'].split(';')[0:-1]))
    size = list(map(int, row['packet_sizes'].split(';')[0:-1]))
    dirs = list(map(int, row['packet_dirs'].split(';')[0:-1]))
    dict1 = {'packet_time': time, 'packet_size': size, 'packet_dir': dirs}
    return pd.DataFrame(dict1)

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

def binarymean_packetsizes(modify_data(raw_data), mean_num):
    return (modified_data(raw_data)["packet_sizes"] > mean_num).replace({True: 1, False: 0})
  
  
  def binarymin_packetsizes(modify_data(raw_data), min_num):
    return (modify_data(raw_data)["packet_sizes"].min() <= min_num)
