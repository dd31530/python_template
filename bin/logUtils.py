#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
'''
+----------------------------------------------------------------------------+
| logUtils:  toolbox for logging functionalities                             |
+---------+----------+----------+--------------------------------------------+
| version | datecode | author   | history                                    |
+---------+----------+----------+--------------------------------------------+
| 1.0     | 151217   | DD       | creation                                   |
+---------+----------+----------+--------------------------------------------+
'''

VERSION = 'v1.0_151217'

##############################################################################
# external modules
##############################################################################


import logging.config


##############################################################################
# local modules
##############################################################################


from messagesUtils import header, banner, footer
from pathUtils import currentPath
 

##############################################################################
# functions 
##############################################################################


def singleton(cls):
   instances = {}
   def get_instance():
      if cls not in instances:
         instances[cls] = cls()
      return instances[cls]
   return get_instance()


##############################################################################
# classes 
##############################################################################


@singleton
class Logger():
   def __init__(self):
      cwd = currentPath()
      config = cwd.cfg('log.conf')
      logging.config.fileConfig(config)
      self.logr = logging.getLogger('root')


##############################################################################
# main
##############################################################################


if __name__ == '__main__':
   header()
   banner('Autotest...')
   Logger.logr.debug('this is an autotest for debug message')
   Logger.logr.info('this is an autotest for info message')
   Logger.logr.warning('this is an autotest for warning message')
   Logger.logr.error('this is an autotest for error message')
   Logger.logr.critical('this is an autotest for critical message')
   footer()


##############################################################################
# eof
##############################################################################
