#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Partition image datasets into train, validation, and test for maximum ML')
parser.add_argument('directory', help='Directory that contains the images that we need to partition')
parser.add_argument('--output', dest='output', default='output/', help='Output directory (default: output/)')

args = parser.parse_args()
