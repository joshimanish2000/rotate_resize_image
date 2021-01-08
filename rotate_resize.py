#! /usr/bin/env python3

import os
from PIL import Image

try:
  os.mkdir("/home/user/Pictures/new_word_cloud")
except:
  pass

def process_image():
  """Rotates and resizes an image"""
  og_image_dir = "/home/user/Pictures/word_cloud"    #original images directory
  for image in os.listdir(og_image_dir):
    os.chdir(og_image_dir)
    name, ext = os.path.splitext(image)    # Get the name of the image (split name and extension)
    im = Image.open(image)    #open the image for processing (does not show the image, use im.show() to show)
    new = im.rotate(90).resize((128,128))    #rotate counter-clockwise and resize it according to the tuple
    os.chdir("/home/manish/Pictures/new_word_cloud")
    new.save(name+"_new"+".png")

if __name__ =="__main__":
  process_image()
