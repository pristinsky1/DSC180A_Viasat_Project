import pandas as pd

# This function returns a dataframe with the packets times, sizes, and directions for a single row of data.
# This will be used within our other functions to help create the features.
def three_cols(row):
    time = list(map(int, row['packet_times'].split(';')[0:-1]))
    size = list(map(int, row['packet_sizes'].split(';')[0:-1]))
    dirs = list(map(int, row['packet_dirs'].split(';')[0:-1]))
    dict1 = {'packet_time': time, 'packet_size': size, 'packet_dir': dirs}
    return pd.DataFrame(dict1)

def modify_data(raw_data):
    #we are separating the column "packet sizes"
    new_pksize = []
    for i in raw_data["packet_sizes"]:
        arr = i.split(";")
        for j in arr[:-1]:
            new_pksize.append(j)

    #we are separating the column "packet dir"
    new_pkdir = []
    for i in raw_data["packet_dirs"]:
        arr = i.split(";")
        for j in arr[:-1]:
            new_pkdir.append(j)

    modified_data = pd.DataFrame({'packet_sizes': pd.to_numeric(new_pksize), 'packet_dir': pd.to_numeric(new_pkdir)})
    return modified_data
