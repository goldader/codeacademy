#A quick script to update a list of postcodes for thoughtspot loading
import csv
from itertools import islice

input_file="/Users/jgoldader/Downloads/postcode.txt"
output_file="/Users/jgoldader/Downloads/postcode_upload.txt"
input_length=0
slice_start=0
increment=10
slice_end=slice_start+increment

#print("Input file has %d rows." % file_length(input_file))

def file_length(fname):
    length=0
    with open(fname, "r", newline='') as f:
        fname = csv.reader(f)
        for i in islice(fname, 0, None):
            length += 1
        if f.closed == False:
            f.close()
    return length

with open(input_file,"r",newline='') as f:
    my_line = csv.reader(f)
    for i in my_line:
        print('"%s","%s","%s","%s","%s"' % (i[2],i[6],i[7],i[9],i[10]))
