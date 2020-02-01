#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser(description='Partition image datasets into train, validation, and test for maximum ML')
parser.add_argument('directory', help='Directory that contains the images that we need to partition')
parser.add_argument('--output', dest='output', default='output/', help='Output directory (default: output/)')

args = parser.parse_args()

if not os.path.isdir(args.directory):
  parser.error(f'{args.directory} is not a valid directory')

files = [f for f in os.listdir(args.directory) if os.path.isfile(os.path.join(args.directory, f))]

for f in files:
  print(f)
