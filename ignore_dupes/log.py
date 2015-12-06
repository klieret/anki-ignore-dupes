#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path

logger = logging.getLogger('ignore_dupes_logging')
logger.setLevel(logging.DEBUG)

# everything that is handled by a StreamHandler will
# be caught by Anki and displayed in a warning window
# so we only use this for ERROR and CRITICAL level.
sh = logging.StreamHandler()
sh.setLevel(logging.ERROR)

addon_dir = os.path.dirname(__file__)
log_path = os.path.join(addon_dir, 'ignore_dupes.log')
fh = logging.FileHandler(log_path, mode="w")
fh.setLevel(logging.DEBUG)

logger.addHandler(fh)
logger.addHandler(sh)