#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
'''
+----------------------------------------------------------------------------+
| logUtils:  toolbox for logging functionalities                             |
+---------+----------+----------+--------------------------------------------+
| version | datecode | author   | history                                    |
+---------+----------+----------+--------------------------------------------+
| 1.0     | 151216   | DD       | creation                                   |
+---------+----------+----------+--------------------------------------------+
'''

VERSION = 'v1.0_151216'

##############################################################################
# external modules
##############################################################################

import logging
from logging.handlers import RotatingFileHandler


##############################################################################
# local modules
##############################################################################


import config
from messagesUtils import header, banner, footer
from pathUtils import currentPath as cwd
 

##############################################################################
# classes 
##############################################################################




##############################################################################
# functions 
##############################################################################




##############################################################################
# main
##############################################################################


CONFIG = config.read()

logfile = cwd().log(CONFIG.get('log', 'LOG_FILE'))
maxsize = CONFIG.get('log', 'MAX_SIZE')
rot = CONFIG.get('log', 'ROT_NUMBER')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s :: %(levelname)5s :: %(filename)s :: %(funcName)s :: %(message)s')
file_handler = RotatingFileHandler(logfile, 'a', maxsize, rot)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

console_formatter = logging.Formatter('[%(levelname)5s] %(funcName)s> %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

if __name__ == '__main__':
   header()
   banner('Autotest...')
   logger.debug('autotest:')
   logger.debug('logfile: %s', logfile)
   footer()


##############################################################################
# eof
##############################################################################

