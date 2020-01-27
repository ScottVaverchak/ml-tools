#!/usr/bin/env python3

import urllib.request
import os
import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Grab images from a ImageNET URL .. URL')
parser.add_argument('url', help='URL to the list of URLs from ImageNET')
parser.add_argument('--output', dest='output', default='output/', help='Output directory (default: output/)')
parser.add_argument('--crop', dest='crop', action='store_true', help='Crop the image to smallest dimension (ie: 20x10 will crop to 10x10)')

args = parser.parse_args()

# "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04467665"
imageneturl = args.url 
urls = []

with urllib.request.urlopen(imageneturl) as f:
  data = f.read().decode('utf-8')
  urls = [x for x in data.splitlines() if x]

os.makedirs(args.output, exist_ok=True)

downloaded = 0
counter = 0

for url in urls[:10]:
  try:
    counter += 1
    uout = urllib.request.urlopen(url).read()
    
    filename = url.rsplit('/', 1)[-1]
    outfile = f'{args.output}{downloaded:04}_{filename}'
    
    fbin = open(outfile, 'wb')
    fbin.write(uout)
    fbin.close()

    img = cv2.imread(outfile)
    mindim = min(img.shape[:2])
    cropped = img[0:mindim, 0:mindim]
    scaled = cv2.resize(cropped, (244, 244))
    cv2.imwrite(outfile, scaled)
    
    downloaded += 1
    print(f"Downloaded {filename} ({downloaded} / {counter} ({round((downloaded / counter) * 100.0)}% success)")
  except Exception as ex:
    print(ex)
    pass

print(f"Finished. {downloaded} out of {counter} files downloaded from {imageneturl}.")
