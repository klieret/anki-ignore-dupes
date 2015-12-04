#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('ignore_dupes_logging')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('ignore_dupes.log')
fh.setLevel(logging.DEBUG)

# logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("write something")