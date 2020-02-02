#!/usr/bin/env python3

# this seems like a good rust project tbh

import os
import argparse
import math

parser = argparse.ArgumentParser(description='Partition image datasets into train, validation, and test for maximum ML')
parser.add_argument('directory', help='Directory that contains the images that we need to partition')
parser.add_argument('--output', dest='output', default='output/', help='Output directory (default: output/)')

args = parser.parse_args()

if not os.path.isdir(args.directory):
  parser.error(f'{args.directory} is not a valid directory')

files = [f for f in os.listdir(args.directory) if os.path.isfile(os.path.join(args.directory, f))]

if len(files) < 3:
  parser.error(f'{args.directory} only contains {len(files)} files.')

file_count = len(files)
train_count = math.ceil(file_count * 0.33)
valid_count = math.ceil((file_count - train_count) * 0.5)
test_count = file_count - (train_count + valid_count)

print(f'Train count: {train_count}')
print(f'Valid count: {valid_count}')
print(f'Test count: {test_count}')

print(file_count)

#for f in files:
#  print(f)
