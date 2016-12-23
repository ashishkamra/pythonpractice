#!/usr/bin/python2.7  
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f_h = open(filename, 'r')

  #reg-ex for rank, male name, female name
  other_re = '(<tr align="right"><td>)\d(</td><td>)([a-z][A-Z]+)(</td><td>)([a-z][A-Z]+)(</td>)'

  year_match = True
  f_dict = {}
  for line in f_h:
    #print line
    if year_match:
      match_y = re.search(r'(Popularity in) (\d\d\d\d)', line)

    if match_y and year_match:
      year = match_y.group(2)
      year_match = False
      #print year

    match_o = re.search(r'(<tr align="right"><td>)(\d?\d?\d?\d?)(</td><td>)(\w*)(</td><td>)(\w*)', line)
    if match_o:
      rank = match_o.group(2)
      name_male = match_o.group(4)
      name_female = match_o.group(6)
      f_dict[name_male] = rank
      f_dict[name_female] = rank

  sorted_list_names = sorted(f_dict.items())
  sorted_list_names.insert(0,(year))

  return sorted_list_names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    sf_h = open('summary.txt','w+')
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for f in args:
    summary_list = extract_names(f)  
    if summary == True:
      print >> sf_h, summary_list
    else:
      print summary_list

  if summary == True:
    sf_h.close()

if __name__ == '__main__':
  main()
