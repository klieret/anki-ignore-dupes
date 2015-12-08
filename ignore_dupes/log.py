#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import sys

logger = logging.getLogger('ignore_dupes_logging')
logger.setLevel(logging.DEBUG)

sh_info = logging.StreamHandler(stream=sys.stdout)
sh_info.setLevel(logging.DEBUG)

# will be caught by anki and displayed in a 
# pop-up window
sh_error = logging.StreamHandler(stream=sys.stderr)
sh_error.setLevel(logging.ERROR)

addon_dir = os.path.dirname(__file__)
log_path = os.path.join(addon_dir, 'ignore_dupes.log')
fh = logging.FileHandler(log_path, mode="w")
fh.setLevel(logging.DEBUG)

logger.addHandler(fh)
logger.addHandler(sh_error)
logger.addHandler(sh_info)