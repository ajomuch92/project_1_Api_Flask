import os
from os import path

def get_extra_files():
  extra_dirs = ['./static','./templates']
  extra_files = extra_dirs[:]
  for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
      for filename in files:
        filename = path.join(dirname, filename)
        if path.isfile(filename):
          extra_files.append(filename)
  return extra_files