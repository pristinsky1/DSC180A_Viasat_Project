import pandas as pd
import numpy as np
import pylab as pl 


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
