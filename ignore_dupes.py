#!/usr/bin/env python
# -*- coding: utf-8 -*-

from anki.notes import Note
from ignoredupes.ignore_dupes_ import ignore_dupes

# overwrite Anki's dupeOrEmpty function
Note.dupeOrEmpty = ignore_dupes