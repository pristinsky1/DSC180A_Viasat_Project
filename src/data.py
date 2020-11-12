import pandas as pd

# This function returns a dataframe with the packets times, sizes, and directions for a single row of data.
# This will be used within our other functions to help create the features.
def three_cols(row):
    time = list(map(int, row['packet_times'].split(';')[0:-1]))
    size = list(map(int, row['packet_sizes'].split(';')[0:-1]))
    dirs = list(map(int, row['packet_dirs'].split(';')[0:-1]))
    dict1 = {'packet_time': time, 'packet_size': size, 'packet_dir': dirs}
    return pd.DataFrame(dict1)
