#!/usr/bin/python2.7 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# returns a list of absolute paths for special files in the given directory
def get_special_paths(dirs):

  abs_paths = []
  for d in dirs:
    filenames = os.listdir(d)
    for f in filenames:
      match = re.search(r'\w*__\w*__\w*.\w*', f)
      if match:
        abs_paths.append(os.path.abspath(f))
      
  return abs_paths

# copies files indicated by abs_paths to todir directory
def copy_files(abs_paths, todir):

  # create todir if not exists
  if not os.path.exists(todir):
    try:
      os.mkdir(todir)
    except:
      print 'Dir creation error:', sys.exc_info()[0], sys.exc_info()[1]
      sys.exit(-1)

  # copy files
  for path in abs_paths:
    try:
      shutil.copy(path, todir)
    except:
      print 'File copy error:', sys.exc_info()[0], sys.exc_info()[1]
      sys.exit(-1)

  return

# zips up files pointed by abs_paths using an external zip command 
def zip_files(abs_paths, tozip):
  
  # form the external command
  (status, cmd_path) = commands.getstatusoutput('which zip')
  if status != 0:
    print 'zip command does not exist on this platform. Unable to proceed!'
    sys.exit(status)
  
  cmd = cmd_path + ' -r ' + tozip + ' '+ ' '.join(abs_paths)
  
  print cmd

  (status, output) = commands.getstatusoutput(cmd)
  
  if status != 0:
    print 'Unable to zip - output:', output
    sys.exit(status)

  return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
  # get absolute paths from the given input dirs
  # print them if no todir and tozip options are provided
  dirs = args
  abs_paths = get_special_paths(dirs)
  if todir == '' and tozip == '':
    for p in abs_paths: print(p)

  # copy the files to the destination directory if todir is set
  # create the dir if needed
  if todir != '':
    copy_files(abs_paths, todir)

  #zip files to a new zip file if tozip is set
  if tozip != '':
    zip_files(abs_paths, tozip)  

if __name__ == "__main__":
  main()
