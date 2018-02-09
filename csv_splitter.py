import os
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
parser.add_argument('num_rows', type=int)
args = parser.parse_args()

print(args.input_file)
print(args.output_file)
print(args.num_rows)
