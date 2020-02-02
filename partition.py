#!/usr/bin/env python3

# this seems like a good rust project tbh

import os
import argparse
import math
import shutil

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

train_set = files[:train_count]
valid_set = files[train_count:train_count + valid_count]
test_set =  files[train_count + valid_count:]

train_dir = os.path.join(args.output, 'train/')
valid_dir = os.path.join(args.output, 'validation/')
test_dir = os.path.join(args.output, 'test/')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

for f in train_set:
  shutil.copy(os.path.join(args.directory, f), os.path.join(train_dir, f))

for f in valid_set:
  shutil.copy(os.path.join(args.directory, f), os.path.join(valid_dir, f))

for f in test_set:
  shutil.copy(os.path.join(args.directory, f), os.path.join(test_dir, f))

