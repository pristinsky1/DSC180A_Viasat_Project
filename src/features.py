
#modified_Data parameter still needs a function to have parameter actually work
def binarymin_packetsizes(modified_data):
    return (modified_data["packet_sizes"].min() <= 32)
