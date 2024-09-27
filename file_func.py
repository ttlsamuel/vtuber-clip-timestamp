import os

# read file name from directories with one item
def name_extract(path):
    filename = str(os.listdir(path)[0])
    name = os.path.join(path, filename)
    return name

# remove contents in directories
def cleaning(path):
    for filename in os.listdir(path):
        os.remove(os.path.join(path, filename))

def time_output(timestamp):
    time_amount = timestamp; time_amount = time_amount % (24 * 3600); hour = time_amount // 3600
    time_amount %= 3600; minutes = time_amount // 60; time_amount %= 60; seconds = time_amount
    print("The approximate timestamp is: " + str(int(hour))
          + " hour(s) " + str(int(minutes)) + " minute(s) " + str("{:.1f}".format(seconds)) + " second(s).")
