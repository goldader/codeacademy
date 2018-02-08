#A quick script to update a list of postcodes for thoughtspot loading
import csv

input_file="/Users/jgoldader/Downloads/postcode.txt"
output_file="/Users/jgoldader/Downloads/postcode_upload.txt"


with open(input_file,"r",encoding='latin-1') as csvFile:
    csvReader = csv.reader(csvFile)
    with open(output_file,"w") as csvResult:
        csvWrite = csv.writer(csvResult,quotechar='"',quoting=csv.QUOTE_ALL)
        for row in csvReader:
            del_list=(0,1,3,4,5,8,11)
            for i in sorted(del_list,reverse=True):
                del row[i]
            csvWrite.writerow(row)
