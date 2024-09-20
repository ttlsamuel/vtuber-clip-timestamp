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
