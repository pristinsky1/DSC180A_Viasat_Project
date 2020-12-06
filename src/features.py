import pandas as pd
import numpy as np
import os

# This function returns a dataframe with the packets times, sizes, and directions for a single row of data.
# This will be used within our other functions to help create the features.
def three_cols(row):
    time = list(map(int, row['packet_times'].split(';')[0:-1]))
    size = list(map(int, row['packet_sizes'].split(';')[0:-1]))
    dirs = list(map(int, row['packet_dirs'].split(';')[0:-1]))
    dict1 = {'packet_time': time, 'packet_size': size, 'packet_dir': dirs}
    return pd.DataFrame(dict1)

# This function takes all the counts of the 0-300bytes for the 1->2 Direction and all the counts
# of the 1200-1500bytes for the 2->1 Direction and creates sum values for the two features per dataset.
# uses the three_cols function as a helper function
def big_byte_count_feature(dataset):        
    packet_size_count1 = []
    packet_size_count2 = []
    for i in range(dataset.shape[0]):
        row = three_cols(dataset.iloc[i])
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
    return [sum(packet_size_count1), sum(packet_size_count2)]
  
  
  # input: filepaths
# output: dataframe with columns -> associated file names, labels, feature1, feature2
# uses the big_byte_count_feature as a helper function
def features_labels(filepath):
    Dir1_ByteCount_0to300_feature = []
    Dir2_ByteCount_1200to1500_feature = []
    labels = []
    files = os.listdir(filepath)
    for file in files:
        if ('novpn' in file) or (file[:2] == '._'):
            continue
        if 'novideo' in file:
            labels.append(0)
        else:
            labels.append(1)
        df = pd.read_csv(filepath + '/' + file)
        sum_values = big_byte_count_feature(df)
        Dir1_ByteCount_0to300_feature.append(sum_values[0])
        Dir2_ByteCount_1200to1500_feature.append(sum_values[1])
    feature_label_df = pd.DataFrame(data={'labels': labels, 'Dir1_ByteCount_0to300_feature': Dir1_ByteCount_0to300_feature,
                                    'Dir2_ByteCount_1200to1500_feature': Dir2_ByteCount_1200to1500_feature})
    return feature_label_df 

# accesses the data file found within the data folder and creates the features and label for it
# uses the big_byte_count_feature as a helper function
def input_feature_label(input_filepath, output_filepath):
    Dir1_ByteCount_0to300_feature = []
    Dir2_ByteCount_1200to1500_feature = []
    labels = []
    file_names = []
    files = os.listdir(input_filepath)
    for file in files:
        if ('novpn' in file) or (file[:2] == '._'):
            return "File Invalid. Must be vpn data, nor can it be empty."
        if 'novideo' in file:
            labels.append(0)
        else:
            labels.append(1)
        file_names.append(file)
        df = pd.read_csv(input_filepath + file)
        sum_values = big_byte_count_feature(df)
        Dir1_ByteCount_0to300_feature.append(sum_values[0])
        Dir2_ByteCount_1200to1500_feature.append(sum_values[1])
    feature_label_df = pd.DataFrame(data={'input_file_name': file_names,'labels': labels,'Dir1_ByteCount_0to300_feature': Dir1_ByteCount_0to300_feature,
                                    'Dir2_ByteCount_1200to1500_feature': Dir2_ByteCount_1200to1500_feature})
    feature_label_df.to_csv(path_or_buf=output_filepath
    return feature_label_df





# Functions Arely Created --> Plz comment these once you get the chance
def binarymean_packetsizes(modify_data(raw_data), mean_num):
    return (modified_data(raw_data)["packet_sizes"] > mean_num).replace({True: 1, False: 0})
  
  
def binarymin_packetsizes(modify_data(raw_data), min_num):
    return (modify_data(raw_data)["packet_sizes"].min() <= min_num)
