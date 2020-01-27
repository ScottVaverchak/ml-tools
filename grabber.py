#!/usr/bin/env python3

import urllib.request
import os
import cv2
import numpy as np

imageneturl = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04467665"
urls = []

with urllib.request.urlopen(imageneturl) as f:
  data = f.read().decode('utf-8')
  urls = [x for x in data.splitlines() if x]

os.makedirs("output/", exist_ok=True)

downloaded = 0
counter = 0

for url in urls[:10]:
  try:
    counter += 1
    uout = urllib.request.urlopen(url).read()
    
    filename = url.rsplit('/', 1)[-1]
    outfile = f'output/{downloaded:04}_{filename}'
    fbin = open(f'output/{downloaded:04}_{filename}', 'wb')
    fbin.write(uout)
    fbin.close()
    img = cv2.imread(outfile)
    mindim = min(img.shape[:2])
    cropped = img[0:mindim, 0:mindim]
    scaled = cv2.resize(cropped, (244, 244))
    cv2.imwrite(filename, scaled)
    downloaded += 1
    print(f"Downloaded {filename} ({downloaded} / {counter} ({round((downloaded / counter) * 100.0)}% success)")
  except Exception as ex:
    print(ex)
    pass

print(f"Finished. {downloaded} out of {counter} files downloaded from {imageneturl}.")
