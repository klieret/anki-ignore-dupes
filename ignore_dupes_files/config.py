#!/usr/bin/env python
# -*- coding: utf-8 -*-

from examples import *

# Define the function ignore_duplicates to choose which duplicates should be
# ignored.
# Default:
#   ignore_duplicates = ignore_nothing
# (this does not ignore any duplicates)
# A lot of examples of how to ignore certain duplicates are given in the file
# examples.py (in this directory).
# E.g. set
#   ignore_duplicates = ignore_all
# to ignore all duplicates.
# You can also add your own function to the file examples.py and then set it
# in here.

ignore_duplicates = ignore_nothing
