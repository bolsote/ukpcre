from csv import reader
from os import listdir

import pickle


def get_postcodes(datadir):
    for fn in listdir(datadir):
        with open(datadir + fn) as f:
            for row in reader(f):
                yield row[0]


if __name__ == '__main__':
    datadir = 'data/Data/CSV/'
    postcodes = list(get_postcodes(datadir))

    with open("OSpostcodes.db", "wb") as f:
        pickle.dump(postcodes, f, pickle.HIGHEST_PROTOCOL)
