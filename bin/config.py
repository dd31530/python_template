#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
+----------------------------------------------------------------------------+
| config:  the project configuration module                                  |
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


from ConfigParser import ConfigParser


##############################################################################
# local modules
##############################################################################


from messagesUtils import header, banner, footer
from pathUtils import currentPath


##############################################################################
# classes 
##############################################################################




##############################################################################
# functions 
##############################################################################


def read():
   CFG = ConfigParser()
   cwd = currentPath()
   CFG.read(cwd.cfg('default.conf'))
   return CFG


##############################################################################
# main
##############################################################################


if __name__ == '__main__':
   header()
   banner("Extract log file name from conf file...")
   test = read()
   print("log file: %s" % test.get('log', 'LOG_FILE'))
   footer()


##############################################################################
# eof
##############################################################################
