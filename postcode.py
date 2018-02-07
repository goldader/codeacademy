#A quick script to update a list of postcodes for thoughtspot loading
import csv
from itertools import islice
import subprocess

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

start=0
end=787
step=end
num_loops=1000

for i in range(num_loops):
    with open(input_file,"r",newline='') as in_file:
        new_row=csv.reader(in_file)
        for i in islice(new_row,start,end):
            #input_length+=1
            #print('"%s","%s","%s","%s","%s"' % (i[2],i[6],i[7],i[9],i[10]))
            #output_file.write('"%s","%s","%s","%s","%s"\n' % (i[2],i[6],i[7],i[9],i[10]))
            with open(output_file,"a") as out_file:
                out_file.write('"%s","%s","%s","%s","%s"\n' % (i[2],i[6],i[7],i[9],i[10]))
        if out_file.closed==False:
            out_file.close()
        if in_file.closed==False:
            in_file.close()
    start=end
    end+=step


numlist=[]
lines=1308781
for n in range(1,2000):
    x=(lines % n)
    if x==0:
        numlist.append(n)
loops=max(numlist)
loop_size=lines/loops
print("%s loops are required of size %d" % (loops,loop_size))
print(numlist)

#print("The input file has %s rows" % file_length(input_file))
#print("The output file has %s rows" % file_length(output_file))

print(subprocess.run(["wc","-l",output_file]))