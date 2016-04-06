import itertools
import sys
import os

def name_list(sample_file):
    names = []
    for line in sample_file:
            names.append(line.split('.')[1])
    return names

def tissue_extract(names, tissue_file):
    tissue_dict={}
    line_counter=0
    for line in tissue_file:
    	if line_counter == 0:
    		line_counter = line_counter + 1 
    		continue
        tissue_dict[line.split()[0]] = line.split()[1:]
    sample_dict={}
    for item in names:
        try:
            sample_dict[item] = tissue_dict[item]
            print sample_dict[item]
        except KeyError:
            print "key not found, ", item
    return sample_dict

outfile=open('./tissue_samples.txt', 'w')
sample_file = open('./sample.txt', 'r')
name = name_list(sample_file)
index_file = open('./tissue_index.txt', 'r')
result = tissue_extract(name, index_file)
for key,value in result.iteritems():
    dummy_line = key + "\t" + value + "\n"
    outfile.write(dummy_line)
outfile.close()


