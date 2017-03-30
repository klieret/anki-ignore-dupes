#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import sys

logger = logging.getLogger('ignore_dupes_logging')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('IgnoreDupes:%(levelname)s:%(message)s')

sh_info = logging.StreamHandler(stream=sys.stdout)
sh_info.setLevel(logging.DEBUG)
sh_info.setFormatter(formatter)

# will be caught by anki and displayed in a
# pop-up window
sh_error = logging.StreamHandler(stream=sys.stderr)
sh_error.setLevel(logging.ERROR)
sh_error.setFormatter(formatter)

addon_dir = os.path.dirname(__file__)
log_path = os.path.join(addon_dir, 'ignore_dupes.log')
fh = logging.FileHandler(log_path, mode="w")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh_error)
logger.addHandler(sh_info)

logger.warning("Plugin 'ignore_dupes' active. Some duplicated card warnings "
               "may be surpressed.")
logger.warning("Verbose Log will be saved at {}".format(
    os.path.abspath(log_path)))
