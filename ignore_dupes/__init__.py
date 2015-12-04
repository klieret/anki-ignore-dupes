#!/usr/bin/env python
# -*- coding: utf-8 -*-

from anki.notes import Note
from ignore_dupes import ignore_dupes

# overwrite Anki's dupeOrEmpty function
Note.dupeOrEmpty = ignore_dupes

import log

print "Info: Plugin 'ignore_dupes' active. Some duplicated card wanrings may be surpressed."