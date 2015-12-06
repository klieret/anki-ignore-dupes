#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('ignore_dupes_logging')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('ignore_dupes.log', mode="w")
fh.setLevel(logging.DEBUG)

# everything that is handled by a StreamHandler will
# be caught by Anki and displayed in a warning window
# so we only use this for ERROR and CRITICAL level.
sh = logging.StreamHandler()
sh.setLevel(logging.ERROR)

logger.addHandler(fh)
logger.addHandler(sh)