import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from scipy import signal
from features import big_byte_count_feature

def no_streaming_viz(dataset):
    #Example of byte count feature extraction on the no streaming dataset:
    big_byte_no_streaming = big_byte_count_feature(dataset)
    d = {'0-300bytesCount_Direction1': [big_byte_no_streaming[0]], '1200-1500bytesCount_Direction2': [big_byte_no_streaming[1]]}
    df = pd.DataFrame(data=d)
    print("No Streaming Byte Count: ")
    return df

def streaming_viz(dataset):
    #Example of byte count feature extraction on the streaming dataset:
    big_byte_streaming = big_byte_count_feature(dataset)
    d = {'0-300bytesCount_Direction1': [big_byte_streaming[0]], '1200-1500bytesCount_Direction2': [big_byte_streaming[1]]}
    df = pd.DataFrame(data=d)
    print("Streaming Byte Count: ")
    return df


def pktdir_vs_pktsze_int(modified_data):
    modified_data[modified_data["packet_dir"] == 1]["packet_sizes"].plot(kind = "hist")
    modified_data[modified_data["packet_dir"] == 2]["packet_sizes"].plot(kind = "hist")
    pl.title('Packet Directions vs Packet Size: internet browsing data with VPN')
    pl.xlabel('Packet Size')
    pl.ylabel('Frequency')
    pl.legend(["1->2", "2->1"])

def pktdir_vs_pktsze_vid(modified_data):
    modified_data[modified_data["packet_dir"] == 1]["packet_sizes"].plot(kind = "hist")
    modified_data[modified_data["packet_dir"] == 2]["packet_sizes"].plot(kind = "hist")
    pl.title('Packet Directions vs Packet Size: video streaming data with VPN')
    pl.xlabel('Packet Size')
    pl.ylabel('Frequency')
    pl.legend(["1->2", "2->1"])

def prominence_analysis(dataset):    
    df1 = dataset[['Time', '2->1Bytes']].set_index('Time')
    df1.index = pd.to_datetime(df1.index,unit='s')
    df1 = df1.resample('500ms').sum()
    s = df1['2->1Bytes']
    fs = 2
    f, Pxx_den = signal.welch(s, fs, nperseg=len(s))
    peaks, properties = signal.find_peaks(np.sqrt(Pxx_den), prominence=100000)
    max_prominence_feature = properties['prominences'].max()
    plt.plot(np.sqrt(Pxx_den))
    plt.plot(peaks, np.sqrt(Pxx_den)[peaks], "x")
    plt.plot(np.zeros_like(np.sqrt(Pxx_den)), "--", color="gray")
    plt.show()
    return ("Max Prominence Value: " + str(max_prominence_feature))
