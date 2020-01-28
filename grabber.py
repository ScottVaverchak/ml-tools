#!/usr/bin/env python3

import urllib.request
import os
import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Grab images from a ImageNET URL .. URL')
parser.add_argument('url', help='URL to the list of URLs from ImageNET')
parser.add_argument('--output', dest='output', default='output/', help='Output directory (default: output/)')
parser.add_argument('--count', dest='count', default=0, type=int, help='Maximum images amount to download - negative values will download all images (default: all of them)')
parser.add_argument('--crop', dest='crop', action='store_true', help='Crop the image to smallest dimension (ie: 20x10 will crop to 10x10)')
parser.add_argument('--resize', dest='resize', type=int, help='Resize the imahes in X and Y by the value. Requires cropping)')
args = parser.parse_args()

if args.resize and not args.crop:
  parser.error('--reszie requires that --crop is set')

if args.resize <= 0:
  parser.error('--resize requires a value greater than zero')

# "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04467665"
imageneturl = args.url 
urls = []

with urllib.request.urlopen(imageneturl) as f:
  data = f.read().decode('utf-8')
  urls = [x for x in data.splitlines() if x]

os.makedirs(args.output, exist_ok=True)

downloaded = 0
counter = 0

if args.count <= 0:
  args.count = len(urls)

for url in urls[:args.count]:
  try:
    counter += 1
    uout = urllib.request.urlopen(url).read()
    
    filename = url.rsplit('/', 1)[-1]
    outfile = f'{args.output}{downloaded:04}_{filename}'
    
    fbin = open(outfile, 'wb')
    fbin.write(uout)
    fbin.close()
    
    img = cv2.imread(outfile)
    imgout = np.empty((1,1))
    if args.crop:
      mindim = min(img.shape[:2])
      imgout = img[0:mindim, 0:mindim]
      if args.resize > 0:
        imgout = cv2.resize(imgout, (args.resize, args.resize))
    else:
      imgout = img

    cv2.imwrite(outfile, imgout)
    
    downloaded += 1
    print(f"Downloaded {filename} ({downloaded} / {counter} ({round((downloaded / counter) * 100.0)}% success)")
  except Exception as ex:
    print(ex)
    pass

print(f"Finished. {downloaded} out of {counter} files downloaded from {imageneturl}.")
