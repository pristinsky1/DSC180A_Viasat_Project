import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from features import big_byte_count_feature

def no_streaming_viz(dataset):
  #Example of byte count feature extraction on the no streaming dataset:
  big_byte_no_streaming = big_byte_count_feature(dataset)
 
  print("No Streaming Byte Count: ")
  return big_byte_no_streaming.sum()

def streaming_viz(dataset):
  #Example of byte count feature extraction on the streaming dataset:
  big_byte_streaming = big_byte_count_feature(dataset)
 
  print("Streaming Byte Count: ")
  return big_byte_streaming.sum()


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
