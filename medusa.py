#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
sys.dont_write_bytecode = True

import time
import logging

SCRIPT_FILE = os.path.abspath(__file__)
SCRIPT_NAME = os.path.basename(SCRIPT_FILE)
SCRIPT_PATH = os.path.dirname(SCRIPT_FILE)
if os.path.islink(__file__):
    REAL_FILE = os.path.abspath(os.readlink(__file__))
    REAL_NAME = os.path.basename(REAL_FILE)
    REAL_PATH = os.path.dirname(REAL_FILE)

LOG_LEVEL = os.environ.get('LOG_LEVEL', logging.INFO)

logging.basicConfig(
    stream=sys.stdout,
    level=LOG_LEVEL,
    format='%(asctime)s %(name)s %(message)s')
logging.Formatter.converter = time.gmtime
logger = logging.getLogger(SCRIPT_NAME)

def main(args):
    logger.info('starting medusa operator')
    logger.info('args = {0}'.format(args))



if __name__ == '__main__':
    main(sys.argv[1:])

