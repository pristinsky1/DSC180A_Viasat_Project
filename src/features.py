import pandas as pd
import numpy as np
import os
from scipy import signal

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
 
#Helper Function in order to prepare data for the features
#input is the raw data from network_stats
def modify_data(dataset):
    #we are separating the column "packet sizes"
    new_pksize = []
    for i in dataset["packet_sizes"]:
        arr = i.split(";")
        for j in arr[:-1]:
            new_pksize.append(j)

    #we are separating the column "packet dir"
    new_pkdir = []
    for i in dataset["packet_dirs"]:
        arr = i.split(";")
        for j in arr[:-1]:
            new_pkdir.append(j)

    modified_data = pd.DataFrame({'packet_sizes': pd.to_numeric(new_pksize), 'packet_dir': pd.to_numeric(new_pkdir)})
    return modified_data

#feature comparing proportions of upload/download packet sizes
#threshold1 parameter is 200
def prop_pksize_dir12(tbl, threshold1):
    proportion = tbl[tbl["packet_sizes"] < threshold1]["packet_dir"].value_counts()[2]/ tbl[tbl["packet_sizes"] < threshold1]["packet_dir"].value_counts()[1]
    return proportion

#feature comparing mean packet sizes
#threshold2 value is 400
def binarymean_packetsizes(tbl, threshold2):
    output = (tbl["packet_sizes"] > threshold2).replace({True: 1, False: 0})
    if output == 1:
        return "Streaming"
    else:
        return "Not Streaming"
 
#feature comparing the maximum packet sizes for
#threshold3 parameter is 1400
def binary_max_pksz(tbl, threshold3):
    num_packets = tbl[tbl["packet_sizes"] >= threshold3].size
    if num_packets > 0:
        return "Streaming"
    else:
        return "Not Streaming"
    
#feature looking at ratio of packet sizes in range 200-400 bytes  
#threshold4 = 200
#threshold5 = 600
def prop_range200_400_dir1(tbl, threshold4, threshold5):
    a = len(tbl[(tbl["packet_sizes"] > threshold4) & (tbl["packet_sizes"] < threshold5) & (tbl["packet_dir"] == 1)])
    b = len(tbl[tbl["packet_dir"] == 1])
    return a/b

#feature looking at ratio of byte size packets of 200 compareed to rest of packets
#threshold6 = 200
def prop_200toentire(tbl, threshold6):
    proportion = tbl[tbl["packet_sizes"] < threshold6]["packet_dir"].size/tbl["packet_sizes"].size
    return proportion

#feature looking at ratio by byte size of 1200 compared to rest of packets 
#threshold7 = 1200
def prop_1200toentire(tbl, threshold7):
    proportion = tbl[tbl["packet_sizes"] > threshold7]["packet_dir"].size/tbl["packet_sizes"].size
    return proportion
  
  # input: filepaths
# output: dataframe with columns -> associated file names, labels, feature1, feature2
# uses the big_byte_count_feature as a helper function
def features_labels(input_filepath, output_filepath):
    Dir1_ByteCount_0to300_feature = []
    Dir2_ByteCount_1200to1500_feature = []
    max_prominence_feature = []
    binary_min = []
    binary_max = []
    prop200_400 = []
    propall0_200 = []
    prop1200 = []
    labels = []
    file_names = []
    files = os.listdir(input_filepath)
    for file in files:
        #eliminates files that don't match the structure of the datasets we are working with
        if ('novpn' in file) or (file[:2] == '._'):
            continue
        if ('novideo' in file) or ('browsing' in file) or ('internet' in file):
            labels.append(0)
        else:
            labels.append(1)
        file_names.append(file)
        df = pd.read_csv(input_filepath + '/' + file)
        #checks to see if file is empty, then eliminates it if empty
        if len(df) == 0:
            labels.pop()
            file_names.pop()
            continue
        #this section creates the two bytecount features
        sum_values = big_byte_count_feature(df)
        #appends the created values to feature list
        Dir1_ByteCount_0to300_feature.append(sum_values[0])
        Dir2_ByteCount_1200to1500_feature.append(sum_values[1])
        #this section creates the max_prominence_feature value in a frequency domain for each dataset
        df_temp = df[['Time', '2->1Bytes']].set_index('Time')
        df_temp.index = pd.to_datetime(df_temp.index,unit='s')
        df_temp = df_temp.resample('500ms').sum()
        s = df_temp['2->1Bytes']
        fs = 2
        f, Pxx_den = signal.welch(s, fs, nperseg=len(s))
        peaks, properties = signal.find_peaks(np.sqrt(Pxx_den), prominence=1000)
        max_prominence = properties['prominences'].max()
        #appends the created value to feature list
        max_prominence_feature.append(max_prominence)
        
        #this section creates the binary_min feature
        modified_data = modify_data(df)
        binary_min_pksz_value = binarymin_packetsizes(modified_data, 32)
        binary_min.append(binary_min_pksz_value)

        #this section creates the binarymax_packetsizes feature
        binary_max_pksz_value = binary_max_pksz(modified_data, 1400)
        binary_max.append(binary_max_pksz_value)
      
        #this section creates the prop_range200_400_dir1
        prop200_400_value = prop_range200_400_dir1(modified_data, 200, 600)
        prop200_400.append(prop200_400_value)
          
        #this section creates the prop_200toentire
        propall0_200_value = prop_200toentire(modified_data, 200)
        propall0_200.append(propall0_200_value)
        
        #this section creates the prop_1200toentire
        prop1200_value = prop_1200toentire(modified_data, 1200)
        prop1200.append(prop1200_value)
        
    feature_label_df = pd.DataFrame(data={'input_file_name': file_names,'labels': labels,'Dir1_ByteCount_0to300_feature': Dir1_ByteCount_0to300_feature,
                                    'Dir2_ByteCount_1200to1500_feature': Dir2_ByteCount_1200to1500_feature, 'max_prominence_feature': max_prominence_feature,
                                          'Binary min' :binary_min, 'Binary_max' : binary_max, 
                                          'Prop200_400' : prop200_400, 'PropAll0_200' : propall0_200, 'Prop1200' : prop1200})

    #look into using index=False, not sure if I need it here but could be something important
    feature_label_df.to_csv(path_or_buf=output_filepath)
    return feature_label_df

# accesses the data file found within the data folder and creates the features and label for it
# uses the big_byte_count_feature as a helper function
def input_feature_label(input_filepath, output_filepath):
    Dir1_ByteCount_0to300_feature = []
    Dir2_ByteCount_1200to1500_feature = []
    max_prominence_feature = [] 
    binary_min = []
    binary_max = []
    prop200_400 = []
    propall0_200 = []
    prop1200 = []
    labels = []
    file_names = []
    files = os.listdir(input_filepath)
    for file in files:
        #eliminates files that don't match the structure of the datasets we are working with
        if ('novpn' in file) or (file[:2] == '._'):
            return "File Invalid. Must be vpn data, nor can it be empty."
        if ('novideo' in file) or ('browsing' in file) or ('internet' in file):
            labels.append(0)
        else:
            labels.append(1)
        file_names.append(file)
        df = pd.read_csv(input_filepath + file)
        #checks to see if file is empty, then eliminates it if empty
        if len(df) == 0:
            labels.pop()
            file_names.pop()
            return "File is empty!"
        #this section creates the two bytecount features
        sum_values = big_byte_count_feature(df)
        #appends the created values to feature list
        Dir1_ByteCount_0to300_feature.append(sum_values[0])
        Dir2_ByteCount_1200to1500_feature.append(sum_values[1])
        #this section creates the max_prominence_feature value in a frequency domain for each dataset
        df_temp = df[['Time', '2->1Bytes']].set_index('Time')
        df_temp.index = pd.to_datetime(df_temp.index,unit='s')
        df_temp = df_temp.resample('500ms').sum()
        s = df_temp['2->1Bytes']
        fs = 2
        f, Pxx_den = signal.welch(s, fs, nperseg=len(s))
        peaks, properties = signal.find_peaks(np.sqrt(Pxx_den), prominence=1000)
        max_prominence = properties['prominences'].max()
        
         #this section creates the binary_min feature
        modified_data = modify_data(df)
        binary_min_pksz_value = binarymin_packetsizes(modified_data, 32)
        binary_min.append(binary_min_pksz_value)

        #this section creates the binarymax_packetsizes feature
        binary_max_pksz_value = binary_max_pksz(modified_data, 1400)
        binary_max.append(binary_max_pksz_value)
      
        #this section creates the prop_range200_400_dir1
        prop200_400_value = prop_range200_400_dir1(modified_data, 200, 600)
        prop200_400.append(prop200_400_value)
          
        #this section creates the prop_200toentire
        propall0_200_value = prop_200toentire(modified_data, 200)
        propall0_200.append(propall0_200_value)
        
        #this section creates the prop_1200toentire
        prop1200_value = prop_1200toentire(modified_data, 1200)
        prop1200.append(prop1200_value)
 
        #appends the created value to feature list
        max_prominence_feature.append(max_prominence)
    feature_label_df = pd.DataFrame(data={'input_file_name': file_names,'labels': labels,'Dir1_ByteCount_0to300_feature': Dir1_ByteCount_0to300_feature,
                                    'Dir2_ByteCount_1200to1500_feature': Dir2_ByteCount_1200to1500_feature, 'max_prominence_feature': max_prominence_feature,
                                          'Binary min' :binary_min, 'Binary_max' : binary_max,'Prop200_400' : prop200_400, 'PropAll0_200' : propall0_200, 'Prop1200' : prop1200})

 
    feature_label_df.to_csv(path_or_buf=output_filepath)
    return feature_label_df

    

