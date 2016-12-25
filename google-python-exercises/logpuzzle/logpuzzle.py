#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

# sort on the second word
def url_sort_key(url):
  match = re.search(r'-(\w+)-(\w+)\.\w+', url)
  if match:
    return match.group(2)
  else:
    return url

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  f_h = open(filename, 'r')

  # get the servername from the input file name
  server_name = re.search(r'(\w)_(.*)', filename).group(2)

  # find all groups of tuples matching the URL
  tuples = re.findall(r'(GET)\s(.*puzzle.*)\s(HTTP)', f_h.read())

  # filter the duplicates using a dictionary
  URL_dict = {}
  for t in tuples:
    URL = 'http://'+server_name+t[1]
    if URL not in URL_dict:
      URL_dict[URL] = 1
    else:
      URL_dict[URL] += 1        
    
  # return sorted list
  return sorted(URL_dict.keys(), key = url_sort_key)

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  # create todir if not exists
  if not os.path.exists(dest_dir):
    try:
      os.mkdir(dest_dir)
    except:
      print 'Dir creation error:', sys.exc_info()[0], sys.exc_info()[1]
      sys.exit(-1)  

  # download the files from the URLs and prepare the <img> tag
  file_index = 1
  src_list = ''
  for url in img_urls:
    print 'Retrieving URL - ', url
    urllib.urlretrieve(url, dest_dir+'/img'+str(file_index))
    src_list = src_list + '<img src="img' + str(file_index) + '">'
    file_index += 1
    #print src_list
  
  # create the HTML file that concatenates the images
  f_h = open(dest_dir+'/index.html', 'w+')
  html = ['<html>', '<body>', src_list, '<html/>', '<body/>']
  f_h.write('\n'.join(html))

  return

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
